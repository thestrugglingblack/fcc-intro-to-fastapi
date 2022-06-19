from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from .config import settings

# import psycopg2
# from psycopg2.extras import RealDictCursor
# import time
'''
RAW DATABASE CONNECTION METHOD
'''
# while True:
#     try:
#         conn = psycopg2.connect(
#             host="localhost",
#             database="fcc-python-api-tutorial",
#             user='postgres',
#             password='',
#             cursor_factory=RealDictCursor
#         )
#         print("Database connection was successful!")
#         cursor = conn.cursor()
#         break
#     except Exception as error:
#         print("Connecting to the database failed!")
#         print("Error: ", error)
#         time.sleep(3)


# Typical format for Database URL
# 'postgresql://<username>:<password>@<ip-address/hostname>/<database_name>'
# 'postgresql://postgres:PASSWORD@localhost:5432/fcc-python-api-tutorial'
SQLALCHEMY_DATABASE_URL = f'postgresql://{settings.db_username}:{settings.db_password}@{settings.db_hostname}:{settings.db_port}/{settings.db_name}'

# responsible fo connecting to sqlalchemy connect to the DB
engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

'''
Estalbishes DB connection and closes once query has been executed
'''
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()