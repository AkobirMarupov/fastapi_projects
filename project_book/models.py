from sqlalchemy import Column, Integer, String, DateTime
from database import Base
from datetime import datetime

class BookModels(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    isbn = Column(String, unique=True, nullable=False)
    written_date = Column(DateTime, default=datetime.utcnow)
    language = Column(String, nullable=False)
    published_year = Column(Integer, nullable=False)
