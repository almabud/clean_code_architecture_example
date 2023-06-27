from src.core.entities.response import Response
from src.core.usecases.login import LoginUseCase
from src.infrastructure.repositories.sqlalchemy.user_repo import UserRepo
from src.infrastructure.repositories.token_repo import JwtTokenRepo
from src.interface_adapter.base_controller import BaseController
from src.interface_adapter.permission import UnAuthenticated


class LoginController(BaseController):
    permissions = (UnAuthenticated,)

    def dispatch(self):
        return Response(
            status='success',
            data=LoginUseCase(
                user_repo=UserRepo(), token_repo=JwtTokenRepo()
            ).execute(**self.request.data),
            status_code=200
        )
