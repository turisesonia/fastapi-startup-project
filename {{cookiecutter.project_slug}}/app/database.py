from sqlalchemy import create_engine, orm
from sqlalchemy.engine import URL

from app.config import settings


def _connection_url(
    host: str = settings.DB_HOST,
    username: str = settings.DB_USERNAME,
    password: str = settings.DB_PASSWORD,
    database: str = settings.DB_DATABASE,
    port: int = settings.DB_PORT,
) -> str:
    return URL.create(
        drivername="postgresql+psycopg",
        host=host,
        username=username,
        password=password,
        database=database,
        port=port,
    )


engine = create_engine(
    _connection_url(),
    echo=settings.APP_DEBUG,  # show sql execute log
    future=True,
    pool_size=20,
    pool_recycle=3600,  # pool close connection time
)

session_factory = orm.sessionmaker(bind=engine)

ScopedSession = orm.scoped_session(session_factory)
