# api routing
from fastapi import FastAPI
import uvicorn
from models import User
from sqlalchemy import create_engine

app = FastAPI()

dialect = "postgresql"
driver = "default"
username = "psql"
host = "localhost"
port = "5432"
database = "psql"
charset_type = "utf8"
engine = create_engine(f"{dialect}+{driver}://{username}:{}")


@app.get("/")
def read_root():
    return {"Hello": "World"}
