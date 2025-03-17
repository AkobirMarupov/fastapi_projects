from pydantic import BaseModel, ConfigDict
from datetime import date

class BookSchema(BaseModel):

    id: int
    title: str
    isbn: str
    published_at: date  

    model_config = ConfigDict(from_attributes=True)  


class BookUpdate(BaseModel):

    title: str
    isbn: str
    published_at: date
