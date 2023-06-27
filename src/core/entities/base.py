from uuid import uuid4
from datetime import datetime

from pydantic import BaseModel as DefaultModel, UUID4


class BaseModel(DefaultModel):
    id: int = None
    identifier: UUID4 = uuid4()
    created_at: datetime = datetime.now()
    updated_at: datetime = None

    class Config:
        orm_mode = True

