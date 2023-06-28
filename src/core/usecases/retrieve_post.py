from uuid import UUID

from src.core.repositories.post_repo import AbstractPostRepo


class RetrievePostUseCase:
    def __init__(self, post_repo: AbstractPostRepo):
        self.post_repo = post_repo

    def execute(self, **filters):
        if not filters:
            raise ValueError('filter not provided.')
        if filters.get('identifier') and not isinstance(
                filters['identifier'], UUID
        ):
            raise ValueError('identifier should be UUID instance.')

        return self.post_repo.get(**filters)
