from abc import ABC, abstractmethod


class BaseRepo(ABC):
    @abstractmethod
    def create(data):
        pass

    @abstractmethod
    def list_(filters=None):
        pass

    @abstractmethod
    def get(filters):
        pass

    @abstractmethod
    def delete(filters):
        pass