from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

dialect = "postgresql"
driver = "psycopg2"
username = "psql"
password = "psql"
host = "localhost"
port = "5432"
database = "psql"
url = f"{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}"

engine = create_engine(url, echo=True)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
