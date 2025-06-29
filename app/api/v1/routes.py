from fastapi import APIRouter
from .endpoints import users, auth, test  # ✅ Add test

router = APIRouter()

# Include individual routers
router.include_router(users.router, prefix="/users", tags=["Users"])
router.include_router(auth.router, prefix="/auth", tags=["Auth"])
router.include_router(test.router, prefix="/test", tags=["Test"])  # ✅ Add test route
