from fastapi import FastAPI, Request, status
from fastapi.responses import JSONResponse

from app.logger import logger
from app.config.settings import settings
from app.exceptions import AppException, ErrorResponse

app = FastAPI(title=settings.APP_NAME)

@app.exception_handler(status.HTTP_500_INTERNAL_SERVER_ERROR)
async def internal_server_error_handler(request, exc: Exception):
    logger.critical(exc)

    response = ErrorResponse(details={"message": "Internal Server Error"})

    return JSONResponse(
        status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
        content=response.model_dump(exclude_none=True),
    )


@app.exception_handler(AppException)
async def backend_exception_handler(
    request: Request, exc: AppException
) -> JSONResponse:
    logger.warning(exc.message, exc=exc.__class__.__name__, path=request.url.path)

    response = ErrorResponse(details={"message": exc.message, "errors": exc.errors})

    return JSONResponse(
        status_code=exc.status_code,
        headers=exc.headers,
        content=response.model_dump(exclude_none=True),
    )



def api_app(app: FastAPI):
    from app.api.v1.routes import health

    app.include_router(health.router, prefix="/api/v1/health", tags=["Health"])


api_app(app)
