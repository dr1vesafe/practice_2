import requests
from database import Session, Base, engine
from bs4 import BeautifulSoup


def create_tables():
    Base.metadata.create_all(engine)


def delete_tables():
    Base.metadata.drop_all(engine)


def get_bulletins():
    url = 'https://spimex.com/markets/oil_products/trades/results/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    bulletins = []

    for a_tag in soup.find_all("a", href=True):
        href = a_tag["href"]
        if href.endswith(".xlsx") and "bulletin" in href:
            result_url = f"https://spimex.com{href}"
            bulletins.append(result_url)

    return bulletins