from uuid import UUID

from src.core.entities.response import Response
from src.core.usecases.retrieve_post import RetrievePostUseCase
from src.infrastructure.repositories.sqlalchemy.post_repo import PostRepo
from src.interface_adapter.base_controller import BaseController


class RetrievePostController(BaseController):
    def dispatch(self):
        return Response(
            status='success',
            data=RetrievePostUseCase(
                post_repo=PostRepo(),
                identifier=UUID(self.request.kwargs.get('identifier'))
            ).execute(),
            status_code=200
        )
