from typing import Any

from .base import BaseModel
from .user import User


class Post(BaseModel):
    title: str
    content: Any = ...
    author: User

    @property
    def author_id(self):
        return self.author.id
