from abc import ABC, abstractmethod


class AbstractBaseRepo(ABC):
    @abstractmethod
    def create(self, data):
        pass

    @abstractmethod
    def list_(self, **filters):
        """
        Fetch list of data from the database.
        """
        pass

    @abstractmethod
    def get(self, **filters):
        """
        Fetch only one data based on filters.
        """
        pass

    @abstractmethod
    def delete(self, **filters):
        """
        Delete data from the database.
        """
        pass

    @abstractmethod
    def exists(self, **filters):
        """
        Check a specific object is present in database or not.

        Returns:
             bool: return whether the item is exists or not
        """
        pass

    @abstractmethod
    def build_entity_obj(self, data):
        """
        Convert database data to entity object.
        """
        pass
