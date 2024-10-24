from typing import List, Optional
from pydantic import BaseModel


class ResponseUserModel(BaseModel):
    params_json: dict
