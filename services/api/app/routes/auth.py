from fastapi.security import OAuth2PasswordRequestForm

from app.auth.jwt import create_access_token
from app.schemas.token import Token
from app.services.user_service import authenticate_user
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from jose import JWTError, jwt

from app.db.dependencies import get_db
from app.schemas.user import UserCreate, UserResponse
from app.services.user_service import (
    create_user,
    get_by_email,
    get_by_username,
)
from app.auth.jwt import (
    create_access_token,
    create_refresh_token,
)

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"],
)


@router.get("/")
async def auth_home():
    return {"message": "Authentication module is working 🚀"}


@router.post(
    "/register",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def register(
    user: UserCreate,
    db: Session = Depends(get_db),
):
    if get_by_email(db, user.email):
        raise HTTPException(
            status_code=400,
            detail="Email already registered",
        )

    if get_by_username(db, user.username):
        raise HTTPException(
            status_code=400,
            detail="Username already exists",
        )

    return create_user(
        db=db,
        username=user.username,
        email=user.email,
        password=user.password,
    )


@router.post("/login", response_model=Token)
def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    db: Session = Depends(get_db),
):
    user = authenticate_user(
        db=db,
        username=form_data.username,
        password=form_data.password,
    )

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid username or password",
        )

    access_token = create_access_token(
        data={"sub": user.username}
    )

    refresh_token = create_refresh_token(
        data={"sub": user.username}
    )

    return {
        "access_token": access_token,
        "refresh_token": refresh_token,
        "token_type": "bearer",
    }

@router.post("/refresh", response_model=Token)
def refresh(token: str):

    try:

        payload = jwt.decode(
            token,
            settings.SECRET_KEY,
            algorithms=[settings.ALGORITHM],
        )

        username = payload.get("sub")

    except JWTError:

        raise HTTPException(
            status_code=401,
            detail="Invalid refresh token",
        )

    access = create_access_token(
        {"sub": username}
    )

    refresh = create_refresh_token(
        {"sub": username}
    )

    return {
        "access_token": access,
        "refresh_token": refresh,
        "token_type": "bearer",
    }