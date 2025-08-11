from pydantic import BaseModel
from datetime import datetime


class User(BaseModel):
    id: int
    email: str
    first_name: str
    last_name: str
    avatar: str


class UsersListResponse(BaseModel):
    page: int
    per_page: int
    total: int
    total_pages: int
    data: list[User]


class SingleUserResponse(BaseModel):
    data: User


class CreateUserRequest(BaseModel):
    name: str
    job: str


class CreateUserResponse(BaseModel):
    name: str
    job: str
    id: str
    createdAt: datetime


class RegisterRequest(BaseModel):
    email: str
    password: str | None = None


class RegisterSuccessfulResponse(BaseModel):
    id: int
    token: str


class RegisterUnsuccessfulResponse(BaseModel):
    error: str
