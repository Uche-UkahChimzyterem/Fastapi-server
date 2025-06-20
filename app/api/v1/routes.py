from fastapi import APIRouter
from .endpoints import users, auth

router = APIRouter()

# Include individual routers
router.include_router(users.router, prefix="/users", tags=["Users"])
router.include_router(auth.router, prefix="/auth", tags=["Auth"])
