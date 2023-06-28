from src.core.entities.response import Response
from src.core.usecases.list_post import ListPostUseCase
from src.infrastructure.repositories.sqlalchemy.post_repo import PostRepo
from src.interface_adapter.base_controller import BaseController


class ListPostController(BaseController):
    def dispatch(self):
        return Response(
            status='success',
            data=ListPostUseCase(post_repo=PostRepo()).execute(),
            status_code=200
        )
