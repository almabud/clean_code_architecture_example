from pydantic import EmailStr

from .base import BaseModel


class User(BaseModel):
    name: str
    email: EmailStr
    password: str
