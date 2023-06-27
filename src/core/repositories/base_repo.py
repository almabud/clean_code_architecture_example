from abc import ABC, abstractmethod


class BaseRepo(ABC):
    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def list_(self, **filters):
        pass

    @abstractmethod
    def get(self, **filters):
        pass

    @abstractmethod
    def delete(self, **filters):
        pass

    @abstractmethod
    def exists(self, **filters):
        pass

    @abstractmethod
    def build_entity_obj(self, data):
        pass
