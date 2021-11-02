from fastapi import APIRouter, HTTPException, Request


router = APIRouter()


@router.get("/")
async def index():

    return {"name": "demo"}
