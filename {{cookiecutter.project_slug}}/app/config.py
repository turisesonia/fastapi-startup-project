import os
from pathlib import Path

from pydantic_settings import BaseSettings, SettingsConfigDict


class _Settings(BaseSettings):
    APP_NAME: str = ""
    APP_ENV: str = "develop"
    APP_DEBUG: bool = False

    ROOT_PATH: Path = Path(os.path.abspath(""))
    APP_PATH: Path = Path(os.path.abspath("app"))
    LOG_PATH: Path = ROOT_PATH / "logs"
    RESOURCE_PATH: Path = ROOT_PATH / "resources"
    STORAGE_PATH: Path = RESOURCE_PATH / "storage"

    DB_HOST: str
    DB_PORT: int = 5432
    DB_DATABASE: str
    DB_USERNAME: str
    DB_PASSWORD: str

    @property
    def RUN_IN_CLOUDRUN(self) -> bool:
        return os.getenv("K_SERVICE") is not None

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8", extra="ignore"
    )


settings = _Settings()
