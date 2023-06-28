from src.core.repositories.post_repo import AbstractPostRepo


class ListPostUseCase:
    def __init__(self, post_repo: AbstractPostRepo):
        self.post_repo = post_repo

    def execute(self, **filters):
        return self.post_repo.list_(**filters)
