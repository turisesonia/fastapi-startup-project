from fastapi import FastAPI, Request
from .core.settings import settings
from .routes import user

app = FastAPI(title=settings.APP_NAME, description="", version="0.1.0")


@app.get("/")
def index(request: Request):
    return {"hello": "world"}


app.include_router(
    user.router,
    prefix="/api/v1/users",
    tags=["User Management API"],
)
