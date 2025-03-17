
from sqlalchemy import Column, Integer, String, Date
from database import Base

class BookModel(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    isbn = Column(String, unique=True, nullable=False)
    published_at = Column(Date, nullable=True)
