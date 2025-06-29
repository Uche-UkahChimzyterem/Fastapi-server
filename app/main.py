# app/api/v1/main.py
from fastapi import FastAPI
from app.api.v1.routes import router as v1_router
from app.api.v1.deps import Base, engine

# Create all database tables on startup
Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="User Management API",
    version="1.0.0"
)

# Include all versioned routes
app.include_router(v1_router, prefix="/api/v1")



# from fastapi import FastAPI
# from pydantic import BaseModel

# app = FastAPI()

# # GET endpoint
# @app.get("/")
# def read_root():
#     return {"message": "Hello, FastAPI!"}

# # Create a data model using Pydantic
# class User(BaseModel):
#     name: str
#     email: str
#     age: int

# # POST endpoint
# @app.post("/create-user/")
# def create_user(user: User):
#     return {
#         "message": f"User {user.name} created successfully!",
#         "user": user
#     }
