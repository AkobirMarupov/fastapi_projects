from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

DATABASE_URL = 'postgresql+psycopg2://postgres:akobir2004@localhost/users_base'

engine = create_engine(DATABASE_URL)

Base = declarative_base()
session = sessionmaker(bind=engine)

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()


