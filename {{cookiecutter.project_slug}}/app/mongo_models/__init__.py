from pymongo import MongoClient
from ..core.settings import settings


class Mongo:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self):
        if settings.APP_ENV == "local":
            mongo_dsn = f"mongodb://{settings.MONGO_HOST}:{settings.MONGO_PORT}/{settings.MONGO_DATABASE}"
        else:
            mongo_dsn = f"mongodb://{settings.MONGO_USERNAME}:{settings.MONGO_PASSWORD}@{settings.MONGO_HOST}:{settings.MONGO_PORT}/{settings.MONGO_DATABASE}"

        self.connect = MongoClient(mongo_dsn, connect=False)
        self.database = self.connect[settings.MONGO_DATABASE]


class BaseMongodb(object):
    _database = Mongo().database

    _collection = ""

    collection_name = None

    indexes = []

    def __init__(self):
        self._collection = self.collection_name

        self.create_indexes()

    @property
    def db(self):
        return self._database[self._collection]

    def collection_exists(self):
        collection_names = self._database.list_collection_names(
            filter={"name": self._collection}
        )
        return len(collection_names) > 0

    def create_indexes(self):
        if self.collection_exists():
            return

        if len(self.indexes) <= 0:
            return

        self._database[self._collection].create_indexes(self.indexes)

    def drop(self):
        self._database.drop_collection(self._collection)


from .sample import Sample
