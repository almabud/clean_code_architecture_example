import uuid
from datetime import datetime
from typing import List

from sqlalchemy import (
    String, create_engine, Table, Column, Integer, ForeignKey, Boolean,
    DateTime, Uuid, Text
)
from sqlalchemy.orm import Mapped, mapped_column, declarative_base, relationship

Base = declarative_base()


class AbstractBaseModel(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True)
    identifier: Mapped[Uuid] = mapped_column(
        Uuid, unique=True, default=uuid.uuid4
    )
    updated_at: Mapped[DateTime] = mapped_column(
        DateTime, default=datetime.now, onupdate=datetime.now
    )
    created_at: Mapped[DateTime] = mapped_column(
        DateTime, default=datetime.now
    )


class User(AbstractBaseModel):
    __tablename__ = 'user'
    __table_args__ = {'extend_existing': True}

    name: Mapped[str] = mapped_column(String(50))
    email: Mapped[str] = mapped_column(String(50))
    password: Mapped[str] = mapped_column(String(100))
    posts: Mapped[List['Post']] = relationship(
        'Post', back_populates="author"
    )


class Post(AbstractBaseModel):
    __tablename__ = 'post'
    __table_args__ = {'extend_existing': True}

    title: Mapped[str] = mapped_column(String(100))
    content: Mapped[str] = mapped_column(Text)
    author_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    author: Mapped[User] = relationship(User, back_populates='posts')
