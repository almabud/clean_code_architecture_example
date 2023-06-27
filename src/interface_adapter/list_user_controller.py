from src.core.entities.response import Response
from src.core.usecases.list_user import ListUserUseCase
from src.infrastructure.repositories.sqlalchemy.user_repo import UserRepo
from src.interface_adapter.base_controller import BaseController
from src.interface_adapter.permission import Authenticated


class ListUserController(BaseController):
    permissions = (Authenticated,)

    def dispatch(self):
        return Response(
            status='success',
            data=ListUserUseCase(user_repo=UserRepo()).execute(),
            status_code=200
        )
