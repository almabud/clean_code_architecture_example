from src.core.entities.response import Response
from src.core.usecases.signup import SignUpUseCase
from src.infrastructure.repositories.sqlalchemy.user_repo import UserRepo
from src.interface_adapter.base_controller import BaseController
from src.interface_adapter.permission import UnAuthenticated


class SignUpController(BaseController):
    permissions = (UnAuthenticated,)

    def dispatch(self):
        return Response(
            status='success',
            data=SignUpUseCase(user_repo=UserRepo()).execute(self.request.data),
            status_code=201
        )
