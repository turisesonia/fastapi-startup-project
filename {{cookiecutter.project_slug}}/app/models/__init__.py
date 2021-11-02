from sqlalchemy import create_engine, orm
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy_mixins import AllFeaturesMixin, TimestampsMixin

from ..core.settings import settings

# MySQL version
connect_url = f"mysql+pymysql://{settings.SQL_USERNAME}:{settings.SQL_PASSWORD}@{settings.MYSQL_HOST}:{settings.MYSQL_PORT}/{settings.SQL_DATABASE}?charset=utf8mb4"

# PostgreSQL version
# connect_url = f"postgresql+psycopg2://{settings.SQL_USERNAME}:{settings.SQL_PASSWORD}@{settings.SQL_HOST}:{settings.SQL_PORT}/{settings.SQL_DATABASE}"

# Cloud SQL connector version
# connect_url = engine.url.URL.create(
#     drivername="mysql+pymysql",
#     username=settings.SQL_USERNAME,
#     password=settings.SQL_PASSWORD,
#     database=settings.SQL_DATABASE,
#     query={"unix_socket": f"/cloudsql/{settings.CLOUDSQL_CONNECTION_NAME}"},
# )

engine = create_engine(
    connect_url,
    pool_size=20,
    echo=False,
)


session = orm.scoped_session(orm.sessionmaker(bind=engine, autocommit=True))

Base = declarative_base()

Base.metadata.create_all(engine)


class Model(Base, AllFeaturesMixin, TimestampsMixin):
    __abstract__ = True

    @classmethod
    def flush(cls):
        cls.session.flush()


Model.set_session(session)

# from .user import User