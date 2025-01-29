from pydantic import BaseModel, EmailStr, ConfigDict
from datetime import datetime
from typing import Optional, Union
from pydantic.types import conint

# Base class for posts
class PostBase(BaseModel):
    title: str
    content: str
    published: bool = True

# Post creation schema
class PostCreate(PostBase):
    pass

# User schema to output
class UserOut(BaseModel):
    id: int
    email: EmailStr
    created_at: datetime

    model_config = ConfigDict(from_attributes=True)  # Correct usage for Pydantic v2

# Post schema that includes a user as owner
class Post(PostBase):
    id: int
    created_at: datetime
    owner_id: int
    owner: UserOut

    model_config = ConfigDict(from_attributes=True)

# Schema to create users
class UserCreate(BaseModel):
    email: EmailStr
    password: str

# User login schema
class UserLogin(BaseModel):
    email: EmailStr
    password: str

# Token schema for authentication
class Token(BaseModel):
    access_token: str
    token_type: str

# Token data that includes user ID
class TokenData(BaseModel):
    id: Union[str, int]

# Vote schema to track votes on posts
class Vote(BaseModel):
    post_id: int
    dir: conint(le=1)

# Output schema for posts with votes
class PostOut(BaseModel):
    Post: Post
    votes: int

    model_config = ConfigDict(from_attributes=True)













# from pydantic import BaseModel, EmailStr
# from datetime import datetime
# from typing import Optional, Union
# from pydantic.types import conint
# # class Post(BaseModel):
# #     title: str
# #     content: str
# #     published: bool = True
# #     # rating: Optional[int] = None

# class PostBase(BaseModel):
#     title: str
#     content: str
#     published: bool = True

# class PostCreate(PostBase):
#     pass

# class UserOut(BaseModel):
#     id: int
#     email: EmailStr
#     created_at: datetime
#     class Config:
#         # orm_mode = True
#         from_attributes = True

# class Post(PostBase):
#     id: int 
#     created_at: datetime
#     owner_id: int 
#     owner: UserOut
    
#     class Config:
#         # orm_mode = True
#         from_attributes = True

# class UserCreate(BaseModel):
#     email: EmailStr
#     password: str

# class UserLogin(BaseModel):
#     email: EmailStr
#     password: str

# class Token(BaseModel):
#     access_token: str
#     token_type: str

# class TokenData(BaseModel):
#     # id: Optional[str] = None
#     id: Union[str, int]

# class Vote(BaseModel):
#     post_id: int
#     dir: conint(le=1)

# class PostOut(BaseModel):
#     Post: Post  
#     votes: int 

#     class Config:
#         from_attributes = True