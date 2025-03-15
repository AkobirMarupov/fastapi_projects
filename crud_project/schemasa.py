from pydantic import BaseModel
from datetime import date

class UserSchema(BaseModel):

    id: int
    name: str
    email: str | None = None
    birthday: date

    class Config:
        orm_mode = True


class UserName(BaseModel):
    name:str
    email:str
    birthday:date