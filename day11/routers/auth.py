from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from database import get_db
from models import User
from schemas import userCreate, userResponse, userLogin
from auth import (
    hash_password,
    verify_password,
    create_access_token,
    decode_access_token
)
from datetime import timedelta


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


security = HTTPBearer()

def get_current_user(credientials:HTTPAuthorizationCredentials=Depends(security),db:Session=Depends(get_db)):
    token = credientials.credentials
    payload = decode_access_token(token)
    if payload is None:
        raise HTTPException(
        status_code=401,
        detail="Invalid token"
    )
    user_id = payload.get("sub")
    if user_id is None:
        raise HTTPException(
        status_code=401,
        detail="Invalid token"
    )
    result = db.execute(
    select(User).where(User.id == int(user_id))
    )

    current_user = result.scalar_one_or_none()
    if current_user is None:
        raise HTTPException(
        status_code=401,
        detail="User not found"
    )
    return current_user


@router.post("/register", response_model=userResponse, status_code=201)
def register_user(
    user: userCreate,
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(User).where(User.username == user.username)
    )

    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    hashed_password = hash_password(user.password)

    new_user = User(
        username=user.username,
        password_hash=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


@router.post("/login")
def login_user(
    user: userLogin,
    db: Session = Depends(get_db)
):
    result = db.execute(
        select(User).where(User.username == user.username)
    )

    existing_user = result.scalar_one_or_none()

    if existing_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    if not verify_password(
        user.password,
        existing_user.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    token = create_access_token(
        data={"sub": str(existing_user.id)},
        expires_delta = timedelta(seconds=60)
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


@router.get("/protected", response_model=userResponse)
def protected_route(
    current_user:User = Depends(get_current_user)
):
    return current_user