import os
from pydantic import BaseSettings


class _Settings(BaseSettings):
    APP_ENV: str = ""
    APP_NAME: str = ""
    ROOT_PATH = os.path.abspath("")
    APP_PATH = os.path.abspath("app")
    RESOURCE_DIR = f"{ROOT_PATH}/resources"
    LOG_PATH = f"{ROOT_PATH}/logs"

    MONGO_HOST: str = ""
    MONGO_PORT: int = 27017
    MONGO_DATABASE: str = ""
    MONGO_USERNAME: str = ""
    MONGO_PASSWORD: str = ""

    SQL_HOST: str = ""
    SQL_PORT: int = 3306
    SQL_DATABASE: str = ""
    SQL_USERNAME: str = ""
    SQL_PASSWORD: str = ""

    REDIS_HOST: str = ""
    REDIS_PORT: int = 6379

    SERVICE_ACCOUNT_JSON: str = ""

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


settings = _Settings()