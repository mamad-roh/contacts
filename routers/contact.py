
from jwt_token import jwt
from typing import List
from fastapi import Depends, status
from sqlalchemy.orm import Session
from contact import schemas, repository
from database import database

from fastapi import APIRouter


router = APIRouter(
    tags=['Contact'],
    prefix='/contact'
)

get_db = database.get_db




@router.post('/', status_code= status.HTTP_201_CREATED)
def create_contacts(
    request: schemas.ContactPost,
    db: Session = Depends(get_db),
    current_user = Depends(
        jwt.get_current_active_user
    )
    
):
    return repository.create(current_user, db, request)


#get all contacts
@router.get('/', status_code= status.HTTP_200_OK, response_model= List[schemas.ShowContacts])
def all_contacts(
        db: Session = Depends(get_db),
        s: str = None,
        limit: int = 0,
        page: int = 1,
        current_user = Depends(
            jwt.get_current_active_user
        )
    ):
    options = dict()
    if s is not None:
        options['search'] = s
    if limit is not 0 and limit > 0:
        options['limit'] = limit
    if page is not 0 and page > 0 :
        options['page'] = page
    
    return repository.all_contact(db, current_user, options)


#remove contact
@router.delete('/{id}', status_code= status.HTTP_200_OK)
def delete(
    id: int,
    db: Session = Depends(get_db),
    current_user = Depends(
        jwt.get_current_active_user
    )
):
    return repository.destroy(db, current_user, id)
