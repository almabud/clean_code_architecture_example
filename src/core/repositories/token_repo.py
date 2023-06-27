from abc import ABC, abstractmethod

from src.core.entities.token import Token
from src.core.entities.user import User


class TokenRepo(ABC):
    @abstractmethod
    def generate_token(self, user: User) -> Token:
        pass

    @abstractmethod
    def verify_token(self, token: str):
        pass

    @abstractmethod
    def build_entity_obj(self, data):
        pass
