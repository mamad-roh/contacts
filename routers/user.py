from fastapi import Depends, status
from sqlalchemy.orm.session import Session
from user import schemas
from database import database
from user import repository

from fastapi import APIRouter

router = APIRouter(
    tags=['User'],
    prefix='/user'
)

get_db = database.get_db

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.UserPost, db: Session= Depends(get_db)):
    return repository.create(db, request)