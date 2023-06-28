from src.core.exceptions.exceptions import NotFound
from src.core.repositories.base_repo import AbstractBaseRepo


class SqlAlchemyAbstractBaseRepo(AbstractBaseRepo):
    def build_filters(self, filters: dict, **kwargs) -> set:
        model = kwargs['model']
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
