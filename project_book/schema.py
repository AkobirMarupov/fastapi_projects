from pydantic import BaseModel
from datetime import date

class BookSxema(BaseModel):

    id: int
    title: str
    author: str
    isbn: str
    written_date: date
    language: str
    published_year: int

    class Config:
        orm_mode = True


class BookUpdate(BaseModel):

    id: int
    title: str
    author: str
    isbn: str
    written_date: date
    language: str
    published_year: int

    