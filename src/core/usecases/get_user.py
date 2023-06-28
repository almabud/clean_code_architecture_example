from src.core.repositories.user_repo import AbstractUserRepo


class GetUserUseCase:
    def __init__(self, user_repo: AbstractUserRepo):
        self.user_repo = user_repo

    def execute(self, **filters):
        if not filters:
            raise ValueError('filter not provided.')
        return self.user_repo.get(**filters)
