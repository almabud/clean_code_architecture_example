from src.core.entities.post import Post
from src.core.repositories.post_repo import AbstractPostRepo


class CreatePostUseCase:
    def __init__(self, post_repo: AbstractPostRepo):
        self.post_repo = post_repo

    def execute(self, data: dict):
        post = Post(**data)

        return self.post_repo.create(post)
