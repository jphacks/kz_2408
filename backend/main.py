# api routing
from fastapi import FastAPI, Path, Body, Depends
import uvicorn
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
import crud
import schemas
from database import SessionLocal, engine
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()


# オリジン間リソース共有の設定

origins = [
    # "http://localhost.tiangolo.com",
    # "https://localhost.tiangolo.com",
    # "http://localhost",
    # "http://localhost:8080",
    # "http://192.168.3.2",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=False,
    allow_methods=["*"],
    allow_headers=["*"],
)


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# test entry posint
@app.get("/")
def get():
    return {"HelloWorld": "This is Operation confirmation Entrypoint"}


# CREATE
@app.post("/users/params")
def create_params_json(
    body: schemas.RequestBodySelfIntroduction, db: Session = Depends(get_db)
):
    params_json = crud.create_json_params(db, body.self_introduction)
    return params_json


# READ
@app.get("/users/params/{user_id}", response_model=schemas.ResponseUserModel)
def get_params_json(user_id: int, db: Session = Depends(get_db)):
    params_json = crud.read_json_params(db, user_id)
    return params_json


# UPDATE
@app.put("/users/params/{user_id}", response_model=schemas.ResponseUserModel)
def put_params_json(
    user_id: int,
    body: schemas.RequestBodySelfIntroduction,
    db: Session = Depends(get_db),
):
    params_json = crud.update_json_params(db, body.self_introduction)
    return params_json


# DELETE
@app.delete("/users/params/{user_id}")
def delete_params_json(user_id: int, db: Session = Depends(get_db)):
    crud.delete_params_json(db, user_id)
    return {"StatusMessage": "Success Delete Params"}
