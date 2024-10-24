# api routing
from fastapi import FastAPI, Path, Body
import uvicorn
from sqlalchemy import create_engine
from schemas import ResponseUserModel

app = FastAPI()


@app.post("/api/{user_id}", response_model=ResponseUserModel)
def read_root(user_id: int = Path(..., title="The ID of the user to get", ge=1)):
    return {"Hello": "World"}
