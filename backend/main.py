# api routing
from fastapi import FastAPI
import uvicorn
from models import User
from sqlalchemy import create_engine

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}
