from typing import Any

from .base import BaseModel


class Post(BaseModel):
    title: str
    content: Any = ...
    author: User

    @property
    def author_id(self):
        return author.id
