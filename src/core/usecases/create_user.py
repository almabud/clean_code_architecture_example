from src.core.repositories.user_repo import IUserRepo


class CreateUserUseCase:
    def __init__(self, user_repo: IUserRepo):
        self.user_repo = user_repo

    def execute(self, data):
        return self.user_repo.create(data)
