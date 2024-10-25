from sqlalchemy.orm import Session
from sqlalchemy import text
from sqlalchemy.exc import SQLAlchemyError
import models
import schemas
import openai_api
import json


# CREATE
def create_json_params(db: Session, self_introduction: str, client):
    # gptのAPI呼び出し
    params_json = openai_api.convert2params_json(
        self_introduction, client
    )  # params_jsonに自己紹介文から得られたパラメータが入る
    q = text(
        "insert into users (self_introduction,params_json,is_compiled) values (:self_introduction, :params, :is_compiled)"
    )
    params = {
        "self_introduction": self_introduction,
        "params": json.dumps(params_json),
        "is_compiled": True,
    }
    try:
        result = db.execute(q, params)
        db.commit()
        return params_json
    except SQLAlchemyError as e:
        db.rollback()
        print("Error occurred:", e)
        return None
    finally:
        return None


# READ
def read_json_params(db: Session, user_id: int):
    q = text("select params_json from users where id = :id")
    params = {"id": user_id}
    try:
        result = db.execute(q, params)
        db.commit()
        params_json = result.fetchone()[0]
        # 結果取得
        return params_json
    except SQLAlchemyError as e:
        db.rollback()
        print("Error occurred:", e)
        return None
    finally:
        return None


# UPDATE
def update_json_params(user_id: int, client, db: Session, self_introduction: str):
    # gptの呼び出し
    params_json = openai_api.convert2params_json(self_introduction, client)
    q = text(
        # "insert into users (self_introduction, params_json, is_compiled) values (:self_introduction, :params, :is_compiled)"
        "update users set self_introduction = :self_introduction, params_json = :params, is_compiled = :is_compiled where id = :user_id"
    )
    params = {
        "self_introduction": self_introduction,
        "params": json.dumps(params_json),
        "is_compiled": True,
        "user_id": user_id,
    }
    try:
        result = db.execute(q, params)
        db.commit()
        return params_json
    except SQLAlchemyError as e:
        db.rollback()
        print("Error occured:", e)
        return None
    finally:
        return None


# DELETE
def delete_params_json(db: Session, user_id: int):
    q = text("delete from users where id = :id ")
    params = {"id": user_id}
    try:
        result = db.execute(q, params)
        db.commit()

        # 消された要素の数を表示
        print(f"Deleted {result.rowcount}")
        return params
    except SQLAlchemyError as e:
        db.rollback()
        print("Error occured:", e)
        return None
    finally:
        return None
