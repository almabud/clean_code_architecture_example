from src.core.entities.response import Response
from src.core.usecases.create_post import CreatePostUseCase
from src.infrastructure.repositories.sqlalchemy.post_repo import PostRepo
from src.interface_adapter.base_controller import BaseController
from src.interface_adapter.permission import Authenticated


class CreatePostController(BaseController):
    permissions = (Authenticated,)

    def dispatch(self):
        return Response(
            status='success',
            data=CreatePostUseCase(
                post_repo=PostRepo(),
            ).execute({'author': self.request.user, **self.request.data}),
            status_code=201
        )
