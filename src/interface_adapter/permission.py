from abc import ABC, abstractmethod

from src.core.entities.request import Request


class BasePermission(ABC):
    def __init__(self, request: Request):
        self.request = request

    @abstractmethod
    def has_permission(self) -> bool:
        pass


class AllowAny(BasePermission):
    def has_permission(self) -> bool:
        return True


class Authenticated(BasePermission):
    def has_permission(self) -> bool:
        return self.request.user.is_authenticated


class UnAuthenticated(BasePermission):
    def has_permission(self) -> bool:
        return not self.request.user.is_authenticated
