from sqlalchemy import create_engine, text, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, declarative_base
from decouple import config

Base = declarative_base()

username=config('MYSQL_USER')
password=config('MYSQL_PASSWORD')
host=config('MYSQL_HOST')
port=config('MYSQL_PORT')
database=config('MYSQL_DATABASE')

engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

