import logging

import structlog
from structlog_cloudrun import CloudRunProcessor
from app.config import settings


def configure_structlog():
    """Configure structlog with custom processors and formatters."""

    processors = [
        structlog.contextvars.merge_contextvars,
        structlog.processors.StackInfoRenderer(),
        structlog.dev.set_exc_info,
    ]

    if settings.RUN_IN_CLOUDRUN:
        processors += [
            CloudRunProcessor(),
            structlog.processors.JSONRenderer(),
        ]
    else:
        processors += [
            structlog.processors.TimeStamper(fmt="%Y-%m-%d %H:%M:%S", utc=True),
            structlog.dev.ConsoleRenderer(),
        ]

    # Configure processors for structured logging
    structlog.configure(
        processors=processors,
        wrapper_class=structlog.make_filtering_bound_logger(
            logging.DEBUG if settings.APP_DEBUG else logging.INFO
        ),
        cache_logger_on_first_use=True,
    )


# Configure structlog
configure_structlog()

# Create logger instance
logger = structlog.get_logger()
