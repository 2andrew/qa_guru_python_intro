from fastapi import APIRouter, HTTPException

from app import models, crud

router = APIRouter()


@router.post("/", response_model=models.User)
def create_user(user: models.UserCreate):
    return crud.create_user(user)


@router.get("/{user_id}", response_model=models.User)
def get_user(user_id: int):
    user = crud.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user
