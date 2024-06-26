import datetime

from pydantic import validator, EmailStr
from sqlmodel import SQLModel, Field, Relationship
from typing import Optional


class User(SQLModel, table=True):
    id: Optional[int] = Field(primary_key=True)
    username: str = Field(index=True)
    password: str = Field(max_length=256, min_length=6)
    email: EmailStr
    create_at: datetime.datetime = datetime.datetime.now()
    is_seller: bool = False


class UserInput(SQLModel):
    username: str
    password: str = Field(max_length=256, min_length=6)
    password2: str
    email: EmailStr
    is_seller: bool = False

    @validator('password2')
    def password_match(cls, v, values, **kwargs):
        if 'password' in values and v != values['password']:
            raise ValueError('password don\'t match')
        return v

class UserLogin(SQLModel):
    username: str
    password: str
