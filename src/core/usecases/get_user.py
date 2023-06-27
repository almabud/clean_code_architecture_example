from src.core.repositories.user_repo import UserRepo


class GetUserUseCase:
    def __init__(self, user_repo: UserRepo, **filters):
        if not filters:
            raise ValueError('filter not provided.')
        self.user_repo = user_repo
        self.filters = filters

    def execute(self):
        return self.user_repo.get(**self.filters)
