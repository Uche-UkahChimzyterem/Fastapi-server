# app/api/v1/endpoints/users.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List, Optional

from ..deps import get_db
from . import schemas, crud, models

router = APIRouter(prefix="/users", tags=["users"])

@router.post("/", 
            response_model=schemas.User, 
            status_code=status.HTTP_201_CREATED,
            summary="Create a new user",
            description="Creates a new user with the provided details. Email must be unique.")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    """
    Create a new user with the following information:
    - **name**: User's full name
    - **email**: User's email (must be unique)
    - **age**: User's age
    """
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )
    return crud.create_user(db=db, user=user)

@router.get("/", 
           response_model=List[schemas.User],
           summary="List all users",
           description="Returns a paginated list of all users in the system.")
def read_users(
    skip: int = 0, 
    limit: int = 100, 
    db: Session = Depends(get_db),
    name: Optional[str] = None,
    email: Optional[str] = None,
    min_age: Optional[int] = None,
    max_age: Optional[int] = None
):
    """
    Get list of users with optional filtering:
    - **skip**: Number of records to skip (for pagination)
    - **limit**: Maximum number of records to return
    - **name**: Filter by name (contains)
    - **email**: Filter by email (contains)
    - **min_age**: Minimum age filter
    - **max_age**: Maximum age filter
    """
    query = db.query(models.User)
    
    if name:
        query = query.filter(models.User.name.contains(name))
    if email:
        query = query.filter(models.User.email.contains(email))
    if min_age is not None:
        query = query.filter(models.User.age >= min_age)
    if max_age is not None:
        query = query.filter(models.User.age <= max_age)
    
    return query.offset(skip).limit(limit).all()

@router.get("/{user_id}", 
           response_model=schemas.User,
           summary="Get user details",
           description="Returns complete details for a specific user.")
def read_user(user_id: int, db: Session = Depends(get_db)):
    """
    Get details for a specific user by ID:
    - **user_id**: The ID of the user to retrieve
    """
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return db_user

@router.patch("/{user_id}", 
             response_model=schemas.User,
             summary="Update user details",
             description="Partially updates a user's information.")
def update_user(
    user_id: int, 
    user_update: schemas.UserUpdate, 
    db: Session = Depends(get_db)
):
    """
    Update partial user information:
    - **user_id**: The ID of the user to update
    - **name**: (Optional) Updated name
    - **email**: (Optional) Updated email
    - **age**: (Optional) Updated age
    """
    db_user = crud.update_user(db, user_id=user_id, user_update=user_update)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return db_user

@router.put("/{user_id}", 
           response_model=schemas.User,
           summary="Replace user data",
           description="Completely replaces all user data with the provided information.")
def replace_user(
    user_id: int, 
    user_data: schemas.UserCreate, 
    db: Session = Depends(get_db)
):
    """
    Replace all user data:
    - **user_id**: The ID of the user to replace
    - **name**: New name
    - **email**: New email
    - **age**: New age
    """
    # First check if user exists
    db_user = crud.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    
    # Delete the existing user
    crud.delete_user(db, user_id=user_id)
    
    # Create a new user with the same ID
    new_user_data = user_data.dict()
    db_user = models.User(id=user_id, **new_user_data)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.delete("/{user_id}", 
              status_code=status.HTTP_204_NO_CONTENT,
              summary="Delete a user",
              description="Permanently removes a user from the system.")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    """
    Delete a user by ID:
    - **user_id**: The ID of the user to delete
    """
    db_user = crud.delete_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return None