from fastapi import FastAPI
# from fastapi.params import Body
# from pydantic import BaseModel
# from typing import Optional, List
# from random import randrange
# import psycopg2
# from psycopg2.extras import RealDictCursor
# from sqlalchemy.orm import Session
# import time
from .database import engine
from . import models
from .routers import post, user, auth, vote
from .config import settings

from fastapi.middleware.cors import CORSMiddleware

# print(settings.database_password)

# models.Base.metadata.create_all(bind=engine)

app = FastAPI()

origins = ["*"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# while True:
#     try:
#         conn = psycopg2.connect(
#             database="postgres",
#             user="postgres",
#             password="tushar3549",
#             host="localhost",
#             port=5432,
#             cursor_factory=RealDictCursor
#         )
#         cursor = conn.cursor()
#         print("connected to database")
#         break
#     except Exception as e: 
#         print("Failed to connect to database")
#         print("Error: ", e)
#         time.sleep(2)


app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get('/') 
# @app.get('/', status_code=status.HTTP_201_CREATED) # for testing 
async def root():
    return {"message": "welcome to api"}

# @app.get("/sqlalchemy")
# def test_posts(db: Session = Depends(get_db)):
#     posts = db.query(models.Post).all()
#     return {"status": posts}

# @app.post('/createposts')
# def create_posts(payload: dict = Body(...)):
#     print(payload)
#     # return {"message": "successfully created post"}
#     return {"new_post": f"title: {payload['title']} and content: {payload['content']}"}

# def create_posts(new_post: Post):
#     print(new_post.title)
#     print(new_post.dict())
#     return {"data": new_post}

# my_posts = [
#     {
#         "title": "title number 1",
#         "content": "content number 1",
#         "id": 1
#     },
#     {
#         "title": "title number 2",
#         "content": "content number 2",
#         "id": 2
#     }
# ]

# def find_post(id):
#     for p in my_posts:
#         if p['id'] == id:
#             return p 

# def find_index_post(id):
#     for i, p in enumerate(my_posts):
#         if p['id'] == id:
#             return i 

# @app.get("posts/latest")
# def get_latest_post():
#     post = my_posts[len(my_posts)]

