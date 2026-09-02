from fastapi import APIRouter, Depends
from pydantic import BaseModel
from auth import verify_tokens

router = APIRouter()

class Work(BaseModel):
    title: str
    description: str
    year: int

@router.get("/api/works")
def get_works():
    #public route, no token needed
    return {"works": []}

@router.post("/api/works", response_model=Work)
def add_work(work: Work, user=Depends(verify_tokens)):
    #protected route, token needed
    return work