from src.core.repositories.token_repo import TokenRepo


class TokenVerifyUseCase:
    def __init__(self, token_repo: TokenRepo, token: str):
        self.token_repo = token_repo
        self.token = token

    def execute(self):
        return self.token_repo.verify_token(self.token)