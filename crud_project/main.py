from fastapi import FastAPI, Depends
from sqlalchemy.orm import Session
from fastapi import HTTPException
import schemasa
import database
import models

app = FastAPI()


@app.get('/')
async def root():
    return {'massage': 'Asosiy sahifa'}


@app.post('/create/username')
async def create_user(username: schemasa.UserName, session: Session = Depends(database.get_db)):
    db_user = models.Users_db(
        name = username.name,
        email = username.email,
        birthday = username.birthday
    )
    session.add(db_user)
    session.commit()
    session.refresh(db_user)
    return db_user
    

@app.get('/username', response_model=schemasa.UserSchema)
async def user_list(name: str, db: Session = Depends(database.get_db)):
    user_db = db.query(models.Users_db).filter(models.Users_db.name == name).first()
    if user_db is None:
        raise HTTPException(status_code=404, detail='Bunday username topilmadi')
    return user_db
