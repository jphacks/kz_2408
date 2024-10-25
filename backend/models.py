from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, Text, JSON
from sqlalchemy.orm import relationship
from database import Base


class User(Base):
    """Userテーブルのモデルクラス

    Args:
        Base (_type_): _description_
    """

    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)

    self_introduction = Column(Text)
    # self_introduction = Column(String)

    params_json = Column(JSON)

    # json parameter にコンパイルされたかどうか
    is_compiled = Column(Boolean, default=False)
