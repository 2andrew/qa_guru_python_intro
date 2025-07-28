import json
from pathlib import Path
from typing import List, Optional

from app.models import User, UserCreate

BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR.parent / "data" / "users.json"


def load_users() -> List[User]:
    if not DATA_FILE.exists():
        return []
    with open(DATA_FILE, "r") as f:
        return [User(**u) for u in json.load(f)]


def save_users(users: List[User]) -> None:
    with open(DATA_FILE, "w") as f:
        json.dump([user.model_dump() for user in users], f, indent=2)


def get_user(user_id: int) -> Optional[User]:
    users = load_users()
    return next((u for u in users if u.id == user_id), None)


def create_user(user: UserCreate) -> User:
    users = load_users()
    user_id = max([u.id for u in users], default=0) + 1
    new_user = User(id=user_id, **user.model_dump())
    users.append(new_user)
    save_users(users)
    return new_user
