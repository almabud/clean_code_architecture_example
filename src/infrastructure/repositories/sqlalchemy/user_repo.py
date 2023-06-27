from operator import or_
from typing import Optional, List

from sqlalchemy import select

from src.core.entities.user import User as UserEntity
from src.core.exceptions.exceptions import NotFound
from src.core.repositories.user_repo import UserRepo as BaseUserRepo
from src.infrastructure.repositories.sqlalchemy.models import Session, User


class UserRepo(BaseUserRepo):
    def list_(self, filters=None) -> Optional[List[UserEntity]]:
        res = []
        with Session() as session:
            res = session.execute(
                select(User).order_by(User.created_at.desc())
            ).scalars().all()

            res = [UserEntity.from_orm(orm_obj) for orm_obj in res]

        return res

    def get(self, **filters):
        filters = self.build_filters(filters)
        res = None
        with Session() as session:
            res = session.execute(
                select(User).where(**filters)
            ).scalar()

        if not res:
            raise NotFound('User not found.')

        return res

    def create(self, data):
        pass

    def delete(self, **filters):
        pass

    def build_entity_obj(self, data):
        return UserEntity.from_orm(data)

    def build_filters(self, filters):
        if not filters:
            raise ValueError('No filter provided.')

        for key, val in filters.items:
            filters[f'User.{key}'] = val
            filters.pop(key)

        return filters
