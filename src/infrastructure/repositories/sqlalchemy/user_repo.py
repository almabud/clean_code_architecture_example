from sqlalchemy import select

from src.core.entities.user import User as UserEntity
from src.core.exceptions.exceptions import NotFound
from src.core.repositories.user_repo import UserRepo as DefaultUserRepo
from src.infrastructure.repositories.sqlalchemy.models import Session, User
from src.infrastructure.repositories.sqlalchemy.sql_alchemy_base_repo import (
    SqlAlchemyBaseRepo
)


class UserRepo(SqlAlchemyBaseRepo, DefaultUserRepo):
    def list_(self, filters=None):
        res = []
        with Session() as session:
            res = session.execute(
                select(User).order_by(User.created_at.desc())
            ).scalars().all()

            res = [self.build_entity_obj(orm_obj) for orm_obj in res]

        return res

    def get(self, **filters):
        filters = self.build_filters(model=User, filters=filters)
        res = None
        with Session() as session:
            res = session.execute(
                select(User).where(*filters)
            ).scalar()

        if not res:
            raise NotFound('User not found.')

        return self.build_entity_obj(res)

    def create(self, user: UserEntity):
        new_user = User(**user.dict(), password=user.password)
        with Session() as session:
            session.add(new_user)
            session.commit()
            session.refresh(new_user)

        return self.build_entity_obj(new_user)

    def delete(self, **filters):
        pass

    def build_entity_obj(self, data):
        return UserEntity.from_orm(data)
