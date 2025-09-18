import uuid
from datetime import datetime

import sqlalchemy as sa
from sqlalchemy.orm import Mapped, mapped_column


class UuidPrimaryKeyMixin:
    id: Mapped[uuid.UUID] = mapped_column(
        sa.Uuid(), default=uuid.uuid4, primary_key=True
    )


class BigIntegerPrimaryKeyMixin:
    id: Mapped[int] = mapped_column(sa.BigInteger(), primary_key=True)

class IntegerPrimaryKeyMixin:
    id: Mapped[int] = mapped_column(sa.Integer(), primary_key=True)


class CreatedAtMixin:
    created_at: Mapped[datetime] = mapped_column(
        sa.TIMESTAMP(), default=sa.func.now(), nullable=True
    )


class UpdatedAtMixin:
    updated_at: Mapped[datetime] = mapped_column(
        sa.TIMESTAMP(), default=sa.func.now(), nullable=True, onupdate=sa.func.now()
    )


class TimestampMixin(CreatedAtMixin, UpdatedAtMixin):
    pass


class SoftDeleteMixin:
    deleted_at: Mapped[datetime] = mapped_column(sa.TIMESTAMP(), nullable=True)
