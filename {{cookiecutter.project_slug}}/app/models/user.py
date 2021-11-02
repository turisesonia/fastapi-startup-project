import sqlalchemy as sa
from sqlalchemy.orm import relationship
from sqlalchemy.ext.hybrid import hybrid_method

from .. import models


class User(models.Model):
    __tablename__ = "users"

    __repr_attrs__ = ["uid"]

    id = sa.Column(sa.BigInteger, primary_key=True, index=True)
    uid = sa.Column(sa.String(255))
    status = sa.Column(sa.Boolean, default=True)

    # rooms = relationship(
    #     "Room",
    #     secondary=room_user.table,
    #     overlaps="users",
    #     lazy="dynamic",
    # )
