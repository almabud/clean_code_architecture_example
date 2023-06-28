from src.core.entities.request import Request
from src.core.exceptions.exceptions import AuthenticationError
from src.core.repositories.token_repo import AbstractTokenRepo
from src.core.repositories.user_repo import AbstractUserRepo


class LoginUseCase:
    def __init__(
            self, user_repo: AbstractUserRepo, token_repo: AbstractTokenRepo
    ):
        self.user_repo = user_repo
        self.token_repo = token_repo

    def execute(self, email, password):
        user = self.user_repo.get(email=email)
        if not user.check_password(password):
            raise AuthenticationError
        # Generate access_token.
        # Here error not handled. As because system should raise the error of
        # token generation. We could use logger perhaps I like to throw this
        # error.
        return self.token_repo.generate_token(user)
