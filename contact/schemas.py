
from pydantic import BaseModel
from fastapi import Query

class ContactSchemas(BaseModel):
    class Config:
        orm_mode =True
    id : int
    user_id : int
    name : str
    family : str
    address : str
    phone : str
    tel : str
    telegram : str
    instagram : str
    email : str

class ContactPost(BaseModel):
    
    name : str = Query(None, min_length=3, max_length=50)
    family : str = Query(None, min_length=3, max_length=50)
    address : str = Query(None,max_length=100)
    phone : str = Query(None, max_length=15)
    tel : str = Query(None, max_length=15)
    telegram : str = Query(None, max_length=50)
    instagram : str = Query(None, max_length=50)
    email : str = Query(None,max_length=50)


class ShowContacts(BaseModel):
    class Config:
        orm_mode =True
    id : int = Query(None)
    name : str = Query(None, min_length=3, max_length=50)
    family : str = Query(None, min_length=3, max_length=50)
    address : str = Query(None,max_length=100)
    phone : str = Query(None, max_length=15)
    tel : str = Query(None, max_length=15)
    telegram : str = Query(None, max_length=50)
    instagram : str = Query(None, max_length=50)
    email : str = Query(None,max_length=50)