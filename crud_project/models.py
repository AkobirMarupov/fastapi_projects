from sqlalchemy import Column, Integer, String,Date
from database import Base


class Users_db(Base):
    __tablename__ = 'users'  
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True, nullable=True)
    birthday = Column(Date, nullable=True)