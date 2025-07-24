from database import Base, engine
from parser import db_load_data


def create_tables():
    Base.metadata.create_all(engine)


def delete_tables():
    Base.metadata.drop_all(engine)


def main():
    delete_tables()
    create_tables()

    db_load_data()


main()
