from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
import os

# user = 'academy'  # os.environ['USER']
# password = 'academy'  # os.environ['PASSWORD']
# postgres_host = '127.0.0.1'  # os.environ['POSTGRES_HOST']
# postgres_port = '5433'  # os.environ['POSTGRES_PORT']
# db_name = 'academy'
# db_string = f'postgresql+psycopg2://{user}:{password}@{postgres_host}:{postgres_port}/{db_name}'

user = os.environ['POSTGRES_USER']
password = os.environ['POSTGRES_PASSWORD']
postgres_host = os.environ['POSTGRES_HOST']
postgres_port = os.environ['POSTGRES_PORT']
db_name = os.environ['POSTGRES_DB']
db_string = f'postgresql+psycopg2://{user}:{password}@{postgres_host}:{postgres_port}/{db_name}'



engine = create_engine(db_string, echo=True)
DeclarativeBase = declarative_base(engine)