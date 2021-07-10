from sqlalchemy import Column, Integer, String, Boolean
from database.database import Base


class UserModels(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    fullname = Column(String(50))
    username = Column(String(50), index=True)
    password = Column(String)
    status = Column(Boolean, default=True)
