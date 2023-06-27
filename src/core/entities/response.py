from typing import Any

from pydantic import BaseModel as DefaultModel, Field


class Response(DefaultModel):
    status: str
    data: Any
    error: Any
    status_code: int = Field(..., exclude=True)

    def json(self, *args, **kwargs):
        kwargs.pop('exclude_none', None)
        return super().json(exclude_none=True, *args, **kwargs)

    def dict(self, *args, **kwargs):
        kwargs.pop('exclude_none', None)
        return super().dict(exclude_none=True, *args, **kwargs)
