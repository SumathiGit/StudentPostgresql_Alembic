  
from typing import Optional
from pydantic import BaseModel
import datetime
from fastapi import Body
from sqlalchemy_utils.types import email

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    username: Optional[str] = None

class User(BaseModel):
    username: str
    is_active: Optional[bool] = None

class UserInDB(User):
    hashed_password: str


class UserCreate(User):
    password: str
    email : str