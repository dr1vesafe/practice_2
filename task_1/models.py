from sqlalchemy import Column, Integer, String, Float, ForeignKey
from database import Base


class Genre(Base):
    __tablename__ = "genre"

    genre_id = Column(Integer, primary_key=True)
    name_genre = Column(String)


class Author(Base):
    __tablename__ = "author"

    author_id = Column(Integer, primary_key=True)
    name_author = Column(String)


class Book(Base):
    __tablename__ = "book"

    book_id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey("author.author_id"))
    genre_id = Column(Integer, ForeignKey("genre.genre_id"))
    price = Column(Float)
    amount = Column(Integer)


class City(Base):
    __tablename__ = "city"

    city_id = Column(Integer, primary_key=True)
    name_city = Column(String)
    days_delivery = Column(Integer)


class Client(Base):
    __tablename__ = "client"

    client_id = Column(Integer, primary_key=True)
    name_client = Column(String)
    city_id = Column(Integer, ForeignKey("city.city_id"))
    email = Column(String)