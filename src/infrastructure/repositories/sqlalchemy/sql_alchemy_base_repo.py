from src.core.exceptions.exceptions import NotFound
from src.core.repositories.base_repo import BaseRepo


class SqlAlchemyBaseRepo(BaseRepo):
    def build_filters(self, model, filters={}) -> set:
        if not filters:
            raise ValueError('No filter provided.')

        generated_filters = set()
        for key, val in filters.items():
            generated_filters.add(getattr(model, key) == val)

        return generated_filters

    def exists(self, **filters):
        try:
            self.get(**filters)
        except NotFound:
            return False
        else:
            return True
