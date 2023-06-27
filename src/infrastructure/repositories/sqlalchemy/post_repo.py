from sqlalchemy import select

from src.core.entities.post import Post as PostEntity
from src.core.exceptions.exceptions import NotFound
from src.core.repositories.post_repo import PostRepo as BasePostRepo
from src.infrastructure.repositories.sqlalchemy.models import (
    Session, Post, User
)
from src.infrastructure.repositories.sqlalchemy.sql_alchemy_base_repo import (
    SqlAlchemyBaseRepo
)


class PostRepo(SqlAlchemyBaseRepo, BasePostRepo):
    def list_(self, filters=None):
        res = []
        with Session() as session:
            res = session.execute(
                select(Post, User).join(Post.author).order_by(
                    Post.created_at.desc()
                )
            ).scalars().all()

            res = [self.build_entity_obj(orm_obj) for orm_obj in res]

        return res

    def get(self, **filters):
        filters = self.build_filters(model=Post, filters=filters)
        res = None
        with Session() as session:
            res = session.execute(
                select(Post).where(*filters)
            ).scalar()
            if not res:
                raise NotFound('User not found.')

            return self.build_entity_obj(res)

    def create(self, post: PostEntity):
        new_post = Post(
            **post.dict(exclude={'author'}), author_id=post.author_id
        )
        with Session() as session:
            session.add(new_post)
            session.commit()
            session.refresh(new_post)

            return self.build_entity_obj(new_post)

    def delete(self, **filters):
        pass

    def build_entity_obj(self, data):
        return PostEntity.from_orm(data)
