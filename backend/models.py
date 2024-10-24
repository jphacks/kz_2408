from pydantic import BaseModel


class User(BaseModel):
    """ユーザーを扱うオブジェクト

    Args:
        BaseModel (_type_): _description_
    """

    id: int  # Id
    name: str  # 名前
    self_introduction: float  # 自己紹介
    params_json: str  # パラメータ
    is_compile: bool = None  # json parameter にコンパイルされたかどうか
