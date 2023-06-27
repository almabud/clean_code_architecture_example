from src.core.exceptions.exceptions import AuthenticationError
from src.core.repositories.token_repo import TokenRepo
from src.core.repositories.user_repo import UserRepo


class LoginUseCase:
    def __init__(self, user_repo: UserRepo, token_repo: TokenRepo):
        self.user_repo = user_repo
        self.token_repo = token_repo

    def execute(self, email: str, password: str):
        user = self.user_repo.get(email=email)
        if not user.check_password(password):
            raise AuthenticationError
        # Generate access_token.
        # Here error not handled. As because system should raise the error of
        # token generation. We could use logger perhaps I like to throw this
        # error.
        return self.token_repo.generate_token(user)
