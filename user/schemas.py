
from pydantic import BaseModel
from fastapi import Query

class UserSchemas(BaseModel):
    class Config:
        orm_mode =True
    username: str
    password: str
    fullname: str
    status: bool

class UserPost(BaseModel):
    class Config:
        orm_mode =True
    username: str = Query(None, min_length=3, max_length=50)
    password: str = Query(None, min_length=3, max_length=50)
    fullname: str = Query(None, min_length=3, max_length=50)

