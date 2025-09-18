import typing as t

from sqlalchemy.orm import DeclarativeBase, Session


class ActiveRecord:
    @classmethod
    def delete(cls, session: Session, pk: t.Any, autocommit: bool = True):
        model = session.get(cls, pk)

        if not model:
            raise ValueError(f"Model with pk {pk} not found")

        session.delete(model)

        if autocommit:
            session.commit()

    def save(self, session: Session, autocommit: bool = True):
        session.add(self)

        if autocommit:
            session.commit()
            session.refresh(self)

    def destroy(self, session: Session, autocommit: bool = True):
        session.delete(self)

        if autocommit:
            session.commit()


class Base(DeclarativeBase, ActiveRecord):
    __repr_attrs__ = ()

    def __repr__(self) -> str:
        """Returns representation of the object"""

        return "{name}({attrs})".format(
            name=self.__class__.__name__,
            attrs=", ".join(
                f"{attr}={getattr(self, attr)}"
                for attr in self.__repr_attrs__
                if hasattr(self, attr)
            ),
        )
