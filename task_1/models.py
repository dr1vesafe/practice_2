from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.sql import func
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


class Buy(Base):
    __tablename__ = "buy"

    buy_id = Column(Integer, primary_key=True)
    buy_description = Column(String, nullable=True)
    client_id = Column(Integer, ForeignKey("client.client_id"))


class BuyBook(Base):
    __tablename__ = "buy_book"

    buy_book_id = Column(Integer, primary_key=True)
    buy_id = Column(Integer, ForeignKey("buy.buy_id"))
    book_id = Column(Integer, ForeignKey("book.book_id"))
    amount = Column(Integer, default=1)


class Step(Base):
    __tablename__ = "step"

    step_id = Column(Integer, primary_key=True)
    name_step = Column(String)


class BuyStep(Base):
    __tablename__ = "buy_step"

    buy_step_id = Column(Integer, primary_key=True)
    buy_id = Column(Integer, ForeignKey("buy.buy_id"))
    step_id = Column(Integer, ForeignKey("step.step_id"))
    date_step_beg = Column(DateTime(timezone=True), server_default=func.now())
    date_step_end = Column(DateTime(timezone=True), nullable=True, onupdate=func.now())