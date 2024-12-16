from .. import models, schemas, oauth2
from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from typing import Optional
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List
from sqlalchemy import func

router = APIRouter(
    prefix="/posts",
    tags=['Posts']
)

# @app.get("/posts")
# @router.get("/", response_model=List[schemas.Post])
@router.get("/", response_model=List[schemas.PostOut])
# def get_posts():
def get_posts(db: Session = Depends(get_db), curr_user: int = Depends(oauth2.get_current_user), limit: int = 10, skip: int = 0, search: Optional[str] = ""):
    # cursor.execute("SELECT * FROM posts")
    # posts = cursor.fetchall()
    # print(limit)
    # posts = db.query(models.Post).all()
    posts = db.query(models.Post).filter(models.Post.title.contains(search)).limit(limit).offset(skip).all()
    # return {"data": my_posts}
    # return {"data": posts}

    results = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).all()
    # print(results)
    return results
    # return posts

    
    
# @app.post("/posts", status_code=status.HTTP_201_CREATED)
# def create_posts(post: Post):
#     # post_dict = post.dict()
#     # post_dict['id'] = randrange(0, 100000000)
#     # my_posts.append(post_dict)
#     # return {"data": post_dict}"
#     cursor.execute(
#     """INSERT INTO posts (title, content, published) VALUES (%s, %s, %s) RETURNING *""",
#     (post.title, post.content, post.published))
#     new_post = cursor.fetchone()
#     conn.commit()
#     return {"data": new_post}


# @app.post("/posts", status_code=status.HTTP_201_CREATED)
@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), curr_user : int = Depends(oauth2.get_current_user)):
    # print(post.dict())
    # new_post = models.Post(title=post.title, content=post.content, published=post.published)
    # print(curr_user.email)

    # new_post = models.Post(**post.dict())
    new_post = models.Post(owner_id = curr_user.id, **post.dict())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


# @router.get("/{id}", response_model=schemas.Post)
@router.get("/{id}", response_model=schemas.PostOut)
# def get_post(id: int, response: Response):

# def get_post(id: int):
#     # post = find_post(int(id))
#     # print(post)
#     cursor.execute("""SELECT * FROM posts WHERE id = %s""", (str(id)))
#     post = cursor.fetchone()
#     if not post:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with id: {id} not found") 
#         # response.status_code = status.HTTP_404_NOT_FOUND
#         # return {'messsage': f"post with id: {id} not found"}
#     return {"post details": post}


def get_post(id: int, db: Session = Depends(get_db), curr_user : int = Depends(oauth2.get_current_user)):
    # post = db.query(models.Post).filter(models.Post.id == id).first()
    post = db.query(models.Post, func.count(models.Vote.post_id).label("votes")).join(models.Vote, models.Vote.post_id == models.Post.id, isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail= f"post with id: {id} not found") 
    return post


@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
# def delete_post(id: int):
#     # index = find_index_post(id)
#     # if index == None:
#     #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
#     # my_posts.pop(index)
#     # # return {"message": "post deleted successfully"}
#     # return Response(status=status.HTTP_204_NO_CONTENT)

#     cursor.execute("""DELETE FROM posts WHERE id = %s RETURNING *""", (str(id),))
#     deleted_post = cursor.fetchone()
#     conn.commit()
#     if deleted_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
#     return Response(status=status.HTTP_204_NO_CONTENT)


def delete_post(id: int, db: Session = Depends(get_db), curr_user : int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
    if post.owner_id != curr_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform request action.")
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)


@router.put('/{id}', response_model=schemas.Post)
# def update_post(id: int, post: Post):
#     # index = find_index_post(id)
#     # if index == None:
#     #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
#     # my_posts[index] = post.dict()
#     # return {"data": post.dict}

#     cursor.execute("""UPDATE posts SET title = %s, content = %s, published = %s WHERE id = %s RETURNING *""", (post.title, post.content, post.published, str(id)))
#     updated_post = cursor.fetchone()
#     conn.commit()
#     if updated_post == None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
#     return {"data": updated_post}

def update_post(id: int, up_post: schemas.PostCreate, db: Session = Depends(get_db), curr_user : int = Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post = post_query.first()
    if post == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"post with id: {id} not found")
    if post.owner_id != curr_user.id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail=f"Not authorized to perform request action.")
    post_query.update(up_post.dict(), synchronize_session=False)
    db.commit()
    return post_query.first()