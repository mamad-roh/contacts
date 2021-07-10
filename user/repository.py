
from starlette import status
from user import models, schemas
from sqlalchemy.orm import Session
from fastapi import HTTPException
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


#create user
def create(db: Session, request: schemas.UserPost):
    check_user = check_existing_user(request.username, db)
    
    if check_user:
        request.password = get_password_hash(request.password)
        new_user = models.UserModels(**request.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return {
            'details': 'user created'
        }
    else:
        raise HTTPException(
            status_code= status.HTTP_406_NOT_ACCEPTABLE,
            detail= f"this username {request.username} exist"
        )


#check existing user
def check_existing_user(username: str, db: Session):
    user = db.query(models.UserModels).filter(
        models.UserModels.username == username
    ).first()
    
    if user is None:
        return True
    else:
        return False