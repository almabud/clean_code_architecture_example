import uuid
from datetime import datetime
from typing import List, Optional

from sqlalchemy import (
    String, create_engine, ForeignKey, DateTime, Uuid, Text, Boolean
)
from sqlalchemy.orm import (
    Mapped, mapped_column, declarative_base, relationship, sessionmaker
)

from src.config import config

Base = declarative_base()
engine = create_engine(config.DB_URL)
Session = sessionmaker(engine)


class AbstractBaseModel(Base):
    __abstract__ = True

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    identifier: Mapped[Uuid] = mapped_column(
        Uuid, unique=True, default=uuid.uuid4
    )
    updated_at: Mapped[Optional[DateTime]] = mapped_column(
        DateTime, default=None, onupdate=datetime.now
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
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False)

    def __init__(self, **kwargs):
        # Remove any extra arguments that are not mapped to model columns
        extra_args = {k: v for k, v in kwargs.items() if hasattr(self, k)}
        super().__init__(**extra_args)


class Post(AbstractBaseModel):
    __tablename__ = 'post'
    __table_args__ = {'extend_existing': True}

    title: Mapped[str] = mapped_column(String(100))
    content: Mapped[str] = mapped_column(Text)
    author_id: Mapped[int] = mapped_column(ForeignKey('user.id'))
    author: Mapped[User] = relationship(User, back_populates='posts')
