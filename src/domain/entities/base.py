from uuid import uuid4
from datetime import datetime

from pydantic import BaseModel as DefaultModel, EmailStr, UUID4


class BaseModel(DefaultModel):
    id: int
    identifier: UUID4 = uuid4()
    created_at: datetime = datetime.now()
    updated_at: datetime = None
