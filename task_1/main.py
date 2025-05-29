from sqlalchemy import select
from database import Session, Base, engine
from models import Genre, Author, Book


def create_tables():
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    

def insert_genres(genres: list):
    with Session() as session:
        for genre_name in genres:
            genre = Genre(name_genre=genre_name)
            session.add(genre)
        session.commit()


def insert_authors(authors: list):
    with Session() as session:
        for author_name in authors:
            author = Author(name_author=author_name)
            session.add(author)
        session.commit()


def insert_books(books: list):
    with Session() as session:
        for book_item in books:
            book = Book(
                title=book_item.get('title'), 
                author_id=book_item.get('author_id'), 
                genre_id=book_item.get('genre_id'), 
                price=book_item.get('price'),
                amount=book_item.get('amount')
                )
            session.add(book)
        session.commit()

def select_books_authors():
    with Session() as session:
        query = (
            select(Book.book_id, Book.title, Author.name_author)
        ).outerjoin(Author, Author.author_id == Book.author_id).order_by(Author.name_author)

        result = session.execute(query).all()
        print(result)

create_tables()

genres = ['Детектив', 'Роман', 'Фантастика', 'Научная литература', 'Детская литература']
insert_genres(genres)

authors = ['Артур Конан Дойл', 'Эрих Мария Ремарк', 'Дуглас Адамс', 'Александр Сергеевич Пушкин']
insert_authors(authors)

books = [
        {
        'title': 'Собака Баскервилей', 
        'author_id': 1,
        'genre_id': 1,
        'price': 400.0,
        'amount': 2000
        },
        {
        'title': 'Три товарища', 
        'author_id': 2,
        'genre_id': 2,
        'price': 599.99,
        'amount': 1540
        },
        {
        'title': 'Приют грёз', 
        'author_id': 2,
        'genre_id': 2,
        'price': 250.0,
        'amount': 400
        },
        {
        'title': 'Автостопом по галактике', 
        'author_id': 3,
        'genre_id': 3,
        'price': 660.0,
        'amount': 3520
        },
        {
        'title': 'Евгений Онегин', 
        'author_id': 4,
        'genre_id': 2,
        'price': 550.0,
        'amount': 12000
        },
        ]

insert_books(books)

select_books_authors()