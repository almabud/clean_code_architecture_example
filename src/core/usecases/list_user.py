from src.core.repositories.user_repo import AbstractUserRepo


class ListUserUseCase:
    def __init__(self, user_repo: AbstractUserRepo):
        self.user_repo = user_repo
    
    def execute(self, filter=None):
        return self.user_repo.list_()
    