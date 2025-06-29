from fastapi import APIRouter, status, HTTPException
from pydantic import BaseModel

router = APIRouter()

# Static credentials (mock only)
STATIC_USER = {
    "username": "janet",
    "password": "1234",
    "token": "mock-token-abc123"
}

class LoginRequest(BaseModel):
    username: str
    password: str

@router.post("/login")
def login(login_request: LoginRequest):
    if (
        login_request.username == STATIC_USER["username"]
        and login_request.password == STATIC_USER["password"]
    ):
        return {"message": "Login successful", "token": STATIC_USER["token"]}
    
    raise HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Invalid username or password"
    )
