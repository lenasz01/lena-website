import os
import jwt
import datetime
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel

router = APIRouter()
SECRET_KEY = os.getenv("SECRET_KEY")

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/api/login")
def login(payload: LoginRequest):
    admin_user = os.getenv("ADMIN_USERNAME")
    admin_pass = os.getenv("ADMIN_PASSWORD")

    if payload.username != admin_user or payload.password != admin_pass:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = jwt.encode(
        {
            "sub": payload.username,
            "exp": datetime.datetime.now(datetime.timezone.utc) + datetime.timedelta(hours=2),
        },
        SECRET_KEY,
        algorithm="HS256",
    )
    return{"token": token}

