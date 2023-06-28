from pydantic import error_wrappers, ValidationError

from src.core.entities.user import User
from src.core.repositories.user_repo import AbstractUserRepo


class SignUpUseCase:
    def __init__(self, user_repo: AbstractUserRepo):
        self.user_repo = user_repo

    def execute(self, data):
        user = User(**data)
        if self.user_repo.exists(email=user.email):
            validation_errors = [
                error_wrappers.ErrorWrapper(
                    exc=ValueError('This Email already exists.'),
                    loc='email'
                )
            ]
            raise ValidationError(validation_errors, model=User)
        user.set_password()
        user = self.user_repo.create(user)

        return user
