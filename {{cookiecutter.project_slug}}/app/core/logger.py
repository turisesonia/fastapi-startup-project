from loguru import logger

from .settings import settings

logger.add(f"{settings.LOG_PATH}/{settings.APP_NAME}.log", rotation="1 days")