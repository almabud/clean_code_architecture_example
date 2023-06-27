from src.core.entities.post import Post
from src.core.repositories.post_repo import PostRepo
from src.core.repositories.user_repo import UserRepo


class CreatePostUseCase:
    def __init__(self, post_repo: PostRepo, data: dict):
        self.post_repo = post_repo
        # self.user_repo = user_repo
        self.post = Post(**data)

    def execute(self):
        return self.post_repo.create(self.post)
