from contextlib import contextmanager
from sqlalchemy.orm import sessionmaker
from models import db

SessionLocal = sessionmaker(bind=db)

def pegar_sessao():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()