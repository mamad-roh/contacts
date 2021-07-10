from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import CheckConstraint, ForeignKey
from database.database import Base


class ContactModels(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    name = Column(String, nullable=True)
    family = Column(String, nullable=True)
    address = Column(String, nullable=True)
    phone = Column(String, nullable=True)
    tel = Column(String, nullable=True)
    telegram = Column(String, nullable=True)
    instagram = Column(String, nullable=True)
    email = Column(String, nullable=True)
    # parent = relationship("UserModels", back_populates="children")

