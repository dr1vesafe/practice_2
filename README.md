# practice_2
# Установка:

1. Клонируйте репозиторий:
```bash
git clone https://github.com/dr1vesafe/practice_2.git
```

2. Создайте виртуальное окружение:
```bash
python -m venv venv
venv\Scripts\activate
```

3. Установите зависимости:
```bash
pip install -r requirements.txt
```

4. Созадайте .env файлы в папках task_1 и task_2 следующего формата:
```bash
DB_NAME = your_db_name 
DB_HOST = localhost
DB_PORT = 5432
DB_USER = your_db_user
DB_PASS = your_db_password
```