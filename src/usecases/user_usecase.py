from .repositories.user_repo import UserRepo

class CreateUserUseCase:
    def __init__(self, user_repo: UserRepo):
        self.user_repo = user_repo

    def execute(self, data):
        return self.user_repo.create(data)
