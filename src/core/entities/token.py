from typing import Optional
from pydantic import BaseModel, Field, UUID4


class TokenPayload(BaseModel):
    identifier: UUID4


class Token(BaseModel):
    access_token: str
    is_validate: bool = Field(False, exclude=True)
    payload: Optional[TokenPayload] = Field(exclude=True)
