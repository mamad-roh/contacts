from os import stat
from typing import List

from sqlalchemy.sql.expression import delete
from contact import models, schemas
from starlette import status
from sqlalchemy.orm import Session, contains_alias
from fastapi import HTTPException
from user import repository
from sqlalchemy import or_

#create contact
def create(current_user, db:Session, request: schemas.ContactPost):
    id = current_user.id
    find_user = repository.check_existing_user_by_id(id, db)
    exist_contact = check_exist_contact(db, id, request)
    if find_user and exist_contact:
        new_request=request.dict()
        new_request['user_id'] = id

        new_contact = models.ContactModels(**new_request)
        db.add(new_contact)
        db.commit()
        db.refresh(new_contact)
        return {'details': 'contact created'}
    
    raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST,
        detail='contact not created'
    )


#check existing contact
def check_exist_contact(db: Session,user_id: int, request):
    contact = db.query(models.ContactModels).filter(
        models.ContactModels.name == request.name,
        models.ContactModels.family == request.family,
        models.ContactModels.user_id == user_id
    ).first()

    if contact is None:
        return True
    else:
        return False


#get all contacts
def all_contact(db: Session, current_user, options : dict):
    contacts = db.query(models.ContactModels).filter(
        models.ContactModels.user_id == current_user.id
    )
    page = 0
    limit = 15
    print(contacts)
    if options.get('search') != None:
        search = '%'+options['search']+'%'
        contacts = contacts.filter(
           or_(models.ContactModels.name.like(search),models.ContactModels.family.like(search))
        )
        print(contacts)
    
    if options.get('page') is not None:
        page = options['page']
        if page < 0 | page == 0 :
            page = 0
        else:
            page = page - 1
    
    if options.get('limit') is not None:
        limit = options['limit']
        if limit < 0 | limit == 0:
            limit = 15
    
    contacts = contacts.offset(page).limit(limit).all()
    return contacts


#remove contacts
def destroy(db: Session, current_user, contact_id: int):
    user_id = current_user.id
    delete = db.query(models.ContactModels).filter(
        models.ContactModels.id == contact_id,
        models.ContactModels.user_id == user_id
    ).delete()

    db.commit()
    if delete :
        return {
            'details': 'contact deleted'
        }


    raise HTTPException(
        status_code= status.HTTP_404_NOT_FOUND, 
        detail='contact not found'
    )


#get contact details
def details(db: Session, current_user, contact_id: int):
    user_id = current_user.id
    contact = db.query(models.ContactModels).filter(
        models.ContactModels.id == contact_id,
        models.ContactModels.user_id == user_id
    ).first()

    if contact is not None:
        return contact
    else:
        raise HTTPException(
            status_code= status.HTTP_400_BAD_REQUEST,
            detail= 'contact not found'
        )

