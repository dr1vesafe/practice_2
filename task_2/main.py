import requests
import pandas
import datetime
from database import Session, Base, engine
from bs4 import BeautifulSoup
from io import BytesIO
from models import SpimexTradingResults


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
        if href.endswith(".xls"):
            result_url = f"https://spimex.com{href}"
            bulletins.append(result_url)

    return bulletins

def parse_bulletin(url):
    with Session() as session:
        try:
            response = requests.get(url)
            response.raise_for_status()
        except Exception as e:
            print(f"Ошибка: {e}")
            return 
        
        try:
            excel_data = BytesIO(response.content)
            xls = pandas.ExcelFile(excel_data)
        except Exception as e:
            print(f'Ошибка: {e}')
            return

        for sheet_name in xls.sheet_names:

            df = xls.parse(sheet_name)
            df.columns = [str(col).strip() for col in df.columns]
                
            required_columns = [
                "Код Инструмента",
                "Наименование Инструмента",
                "Базис поставки",
                "Объем Договоров в единицах измерения",
                "Обьем Договоров, Руб.",
                "Количество Договоров, шт."
            ]

            if not all(col in df.columns for col in required_columns):
                continue

            df = df[required_columns]
            
            try:
                for i, row in df.iterrows():
                    result = SpimexTradingResults(
                        exchange_product_id = str(row["Код Инструмента"]),
                        exchange_product_name = row["Наименование Инструмента"],
                        oil_id = str(row["Код Инструмента"])[:4],
                        delivery_basis_id = str(row["Код Инструмента"])[4:7],
                        delivery_basis_name = row["Базис поставки"],
                        delivery_type_id = str(row["Код Инструмента"])[-1],
                        volume = row["Объем Договоров в единицах измерения"],
                        total = row["Обьем Договоров, Руб."],
                        count = row["Количество Договоров, шт."],
                        date = datetime.datetime.utcnow()
                    )

                    session.add(result)
            except Exception as e:
                print(f"Ошибка: {e}")
            
        session.commit()


def main():
    create_tables()
    bulletin_links = get_bulletins()
    for link in bulletin_links:
        parse_bulletin(link)


main()