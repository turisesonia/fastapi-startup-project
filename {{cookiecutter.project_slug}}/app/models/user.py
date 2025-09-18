import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column

from ._base import Base
from ._mixin import TimestampMixin, UuidPrimaryKeyMixin


class User(Base, UuidPrimaryKeyMixin, TimestampMixin):
    __tablename__ = "users"

    __repr_attrs__ = ("id", "email", "name")

    uid: Mapped[str] = mapped_column(sa.String(120), unique=True)
    email: Mapped[str] = mapped_column(sa.String(), unique=True)
    password: Mapped[str] = mapped_column(sa.String(150), nullable=True)
    name: Mapped[str] = mapped_column(sa.String(100), nullable=True)


