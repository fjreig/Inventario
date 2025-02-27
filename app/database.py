from contextlib import contextmanager
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

Base = declarative_base()

### Postgres Database
MONGO_USER = os.environ['MONGO_INITDB_ROOT_USERNAME']
MONGO_PASSWORD = os.environ['MONGO_INITDB_ROOT_PASSWORD']
MONGO_DB = os.environ['POSTGRES_DB']
MONGO_HOST = os.environ['MONGO_HOST']
MONGO_PORT = os.environ['MONGO_PORT']

#engine = create_engine(“mongodb:///?Server=MyServer&;Port=27017&Database=test&User=test&Password=Password”)

SQLALCHEMY_DATABASE_URL = f'mongodb:///?Server={MONGO_HOST}&;Port={MONGO_PORT}&Database={MONGO_DB}&User={MONGO_USER}&Password={MONGO_PASSWORD}'
engine = create_engine(SQLALCHEMY_DATABASE_URL)

Session = sessionmaker(bind=engine)
session = Session()