from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import database
import schemas
import models

app = FastAPI()



@app.get('/book', response_model=list[schemas.BookSchema])
async def read_book(session: Session = Depends(database.get_db)):
    get_information = session.query(models.BookModel).all()
    return get_information

@app.post('/book', response_model=schemas.BookSchema)
async def create_book(book: schemas.BookSchema, session: Session = Depends(database.get_db)):
    new_book = models.BookModel(

        title= book.title,
        isbn= book.isbn,
        published_at= book.published_at
    )

    session.add(new_book)
    session.commit()
    session.refresh(new_book)
    return new_book

@app.put('/book/{book_id}', response_model=schemas.BookSchema)
async def update_book(book_id: int, book: schemas.BookUpdate, session: Session = Depends(database.get_db)):
    book_md = session.query(models.BookModel).filter(models.BookModel.id == book_id).first()

    if not book_md:
        raise HTTPException(status_code=404, detail="Bunday id dagi kitob topilmadi...")
    
    book_md.title = book.title
    book_md.isbn = book.isbn    
    book_md.published_at = book.published_at

    session.commit()
    session.refresh(book_md)
    return book_md


@app.delete('/book/{book_id}')
async def delete_book(book_id: int, session: Session = Depends(database.get_db)):
    delete_id = session.query(models.BookModel).filter(models.BookModel.id == book_id).first()

    if not delete_id:
        raise HTTPException(status_code=404, detail="Bunday id dagi kitob topilmadi...")

    session.delete(delete_id)
    session.commit()
    return {"muvaffaqiyatli ochirildi."}
