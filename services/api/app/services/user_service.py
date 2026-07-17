from sqlalchemy.orm import Session

from app.models.user import User
from app.auth.hashing import hash_password
from app.repositories.user_repositories import UserRepository


def get_by_email(db: Session, email: str):
    repo = UserRepository(db)
    return repo.get_by_email(email)


def get_by_username(db: Session, username: str):
    repo = UserRepository(db)
    return repo.get_by_username(username)


def create_user(
    db: Session,
    username: str,
    email: str,
    password: str,
):
    user = User(
        username=username,
        email=email,
        hashed_password=hash_password(password),
    )

    repo = UserRepository(db)
    repo.create(user)
    return user


def authenticate_user(
    db: Session,
    username: str,
    password: str,
):
    print("USERNAME:", username)

    user = get_by_username(db, username)

    print("USER FOUND:", user)

    if not user:
        print("User not found")
        return None

    from app.auth.hashing import verify_password

    print("HASH:", user.hashed_password)

    ok = verify_password(password, user.hashed_password)

    print("PASSWORD OK:", ok)

    if not ok:
        return None

    return user