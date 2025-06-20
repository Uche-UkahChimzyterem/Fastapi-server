from fastapi import FastAPI
from api.v1.routes import router as v1_router

app = FastAPI()

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
