from uuid import UUID

from src.core.repositories.post_repo import PostRepo


class RetrievePostUseCase:
    def __init__(self, post_repo: PostRepo, identifier: UUID):
        self.post_repo = post_repo
        self.identifier = identifier

    def execute(self):
        return self.post_repo.get(identifier=self.identifier)