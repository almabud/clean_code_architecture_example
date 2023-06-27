import base64
import hashlib

import bcrypt
from pydantic import EmailStr, SecretStr, Field

from .base import BaseModel


class User(BaseModel):
    name: str
    email: EmailStr
    password: SecretStr = Field(..., exclude=True)
    is_superuser: bool = False

    def set_password(self):
        self.password = bcrypt.hashpw(
            base64.b64encode(
                hashlib.sha256(
                    self.password.get_secret_value().encode()
                ).digest()
            ),
            bcrypt.gensalt()
        )

    def check_password(self, password):
        return bcrypt.checkpw(
            base64.b64encode(hashlib.sha256(password.encode()).digest()),
            self.password
        )
