from fastapi import APIRouter
from pydantic import BaseModel

router = APIRouter()

class User(BaseModel):
    name: str
    email: str
    age: int

@router.post("/create")
def create_user(user: User):
    return {
        "message": f"User {user.name} created successfully!",
        "user": user
    }
