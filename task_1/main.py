from database import Session, Base, engine
from models import Book


def create_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    

create_tables()