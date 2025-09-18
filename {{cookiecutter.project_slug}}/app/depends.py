import typing as t
from contextlib import asynccontextmanager

from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session

from app.database import session_factory


@asynccontextmanager
async def lifespan(app: FastAPI):
    yield


def session_handler():
    session = session_factory()

    try:
        yield session
    except Exception as e:
        session.rollback()
        raise e
    finally:
        session.close()


DatabaseSession = t.Annotated[Session, Depends(session_handler)]


class Provider:
    def __init__(self, cls):
        self.cls = cls

    def __call__(self, session: Session = Depends(session_handler)):
        yield self.cls(session=session)
