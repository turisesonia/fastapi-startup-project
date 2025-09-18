from fastapi import APIRouter, HTTPException, Request


router = APIRouter()


@router.get("/check")
async def check():
    return {"status": "healthy"}
