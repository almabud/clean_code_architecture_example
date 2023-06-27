from datetime import datetime
from typing import Optional

from pydantic import BaseModel, SecretStr, Field

from src.core.entities.enums import RequestMethod
from src.core.entities.user import User


class RequestUser(User):
    is_authenticated: bool = True
    password: SecretStr = Field(None, exclude=True)


class AnonymousUser(RequestUser):
    id: int = None
    name: str = None
    email: str = None
    created_at: datetime = None
    updated_at: datetime = None
    is_authenticated: bool = False


class Request(BaseModel):
    method: RequestMethod
    user: Optional[User]
    query_params: dict = {}
    kwargs: dict = {}
    data: dict = {}
    created_at: datetime = datetime.now()
    headers: dict = {}
