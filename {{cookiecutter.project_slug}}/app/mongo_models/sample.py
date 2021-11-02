from pymongo import IndexModel, ASCENDING
from . import BaseMongodb


class Sample(BaseMongodb):
    """
    {
        "sample" : str,
        "name" : str,
        "age" : int
    }
    """

    indexes = [
        IndexModel([("name", ASCENDING)], name="name_index"),
    ]
