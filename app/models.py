from sqlalchemy import Column, Integer, String
from .database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False, index=True)
    surname = Column(String, nullable=False, index=True)
    name = Column(String, nullable=False, index=True)
