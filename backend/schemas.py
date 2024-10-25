from typing import List, Optional
from pydantic import BaseModel


class RequestBodySelfIntroduction(BaseModel):
    self_introduction: str


class ResponseUserModel(BaseModel):
    interests: int
    skills: int
    approach: int
