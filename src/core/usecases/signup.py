from pydantic import validator, error_wrappers, ValidationError

from src.core.entities.user import User
from src.core.repositories.user_repo import UserRepo


class SignUpUseCase:
    def __init__(self, user_repo: UserRepo, user: User):
        self.user_repo = user_repo
        self.user = user

    def execute(self):
        if self.user_repo.exists(email=self.user.email):
            validation_errors = [
                error_wrappers.ErrorWrapper(
                    exc=ValueError('This Email already exists.'),
                    loc='email'
                )
            ]
            raise ValidationError(validation_errors, model=User)
        self.user.set_password()
        user = self.user_repo.create(self.user)

        return user
