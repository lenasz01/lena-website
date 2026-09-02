from fastapi import APIRouter

router = APIRouter()

@router.get("/api/bio")
def get_bio():
    #public route, no token needed
    return {"bio": []}