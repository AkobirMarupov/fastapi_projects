from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import database as database
from models import BookModels
from schema import BookSxema, BookUpdate

app = FastAPI()



@app.get("/")
async def read_root():
    return {"message": "Asosiy sahifa"}


@app.get("/book", response_model=list[BookSxema])
async def get_books( session: Session = Depends(database.get_db)):
    books = session.query(BookModels).all()
    return books


@app.post('/book', response_model=BookSxema)
async def post_books(books: BookSxema, session: Session = Depends(database.get_db)):
    new_book = BookModels(

        title=books.title,
        author=books.author,
        isbn=books.isbn,
        written_date=books.written_date,
        language=books.language,
        published_year=books.published_year
    )

    session.add(new_book)
    session.commit()
    session.refresh(new_book)
    return new_book


@app.put('/book/{book_id}', response_model=BookSxema)
async def update_book(book_id: int, book: BookUpdate, session: Session = Depends(database.get_db)):
    update_db = session.query(BookModels).filter(BookModels.id == book_id).first()
    if not update_db:
        raise HTTPException(status_code=404, detail="Bunday id dagi kitob topilmadi...db")

    update_db.title = book.title
    update_db.author = book.author
    update_db.isbn = book.isbn
    update_db.written_date = book.written_date
    update_db.language = book.language
    update_db.published_year = book.published_year

    session.commit()
    session.refresh(update_db)
    return update_db


@app.delete('/book/{book_id}')
async def delete_book(book_id: int, session: Session = Depends(database.get_db)):
    delete = session.query(BookModels).filter(BookModels.id == book_id).first()
    if not delete:
        raise HTTPException(status_code=404, detail="Bunday id dagi kitob topilmadi...")

    session.delete(delete)
    session.commit()
    return {"message": "Kitob muvaffaqiyatli ochirildi"}