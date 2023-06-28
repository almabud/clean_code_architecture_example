from src.core.repositories.token_repo import AbstractTokenRepo


class TokenVerifyUseCase:
    def __init__(self, token_repo: AbstractTokenRepo):
        self.token_repo = token_repo

    def execute(self, token: str):
        return self.token_repo.verify_token(token)
