from src.core.repositories.post_repo import PostRepo


class ListPostUseCase:
    def __init__(self, post_repo: PostRepo):
        self.post_repo = post_repo

    def execute(self):
        return self.post_repo.list_()
