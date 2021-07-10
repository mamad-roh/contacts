from sqlalchemy.sql.expression import false, true
from user import models
from sqlalchemy.orm import Session

def create(db: Session, request):
    pass


#check existing user
def check_existing_user(username: str, db: Session):
    user = db.query(models.UserModels).filter(
        models.UserModels.username == username
    ).first()

    if not user:
        return true
    else:
        return false