from sqlalchemy import create_engine, Table, Column, Integer, String, MetaData
from settings import LOGIN, PASSWORD, DATABASE_URL, DBNAME

login = LOGIN
password = PASSWORD
database_url = DATABASE_URL
dbname = DBNAME


# Строка подключения к базе данных
db_connection_string = f"postgresql://{login}:{password}@{database_url}:5432/{dbname}"
db = create_engine(db_connection_string)

# Базовый класс для моделей
metadata = MetaData()


# Модель студента
student = Table(
    'student', metadata,
    Column('user_id', Integer, primary_key=True),
    Column('level', String),
    Column('education_form', String),
    Column('subject_id', Integer)
)

# Создаем сессию для взаимодействия с базой данных
connection = db.connect()
connection.close()
