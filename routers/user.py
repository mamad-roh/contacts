from jwt_token import jwt
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

@router.get('/me', status_code= status.HTTP_200_OK, response_model= schemas.UserSchemas)
def me_details(
    current_user: schemas.UserSchemas = Depends(
        jwt.get_current_active_user
    )
):
    return repository.get_user(current_user)