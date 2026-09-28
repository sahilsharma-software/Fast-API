from datetime import timedelta

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from sqlalchemy import select
from sqlalchemy.orm import Session

from auth import (
    create_access_token,
    decode_access_token,
    hash_password,
    verify_password,
)
from database import get_db
from models import User
from schemas import userCreate, userLogin, userResponse


router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)

security = HTTPBearer()


# ---------------------------
# Get currently authenticated user
# ---------------------------
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security),
    db: Session = Depends(get_db)
):
    # Extract actual JWT from:
    # Authorization: Bearer <JWT>
    token = credentials.credentials

    # Verify and decode JWT
    payload = decode_access_token(token)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    # Get user ID from JWT payload
    user_id = payload.get("sub")

    if user_id is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid token"
        )

    # Find user in database
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


# ---------------------------
# Admin authorization dependency
# ---------------------------
def require_role(*allowed_roles:str):
    def role_checkers(current_user:User = Depends(get_current_user)):
        if current_user.role not in allowed_roles:
            raise HTTPException(
                status_code=403,
                detail="insufficient permisions"
            )
        return current_user
    return role_checkers

# ---------------------------
# Admin-only protected route
# ---------------------------
@router.get("/admin", response_model=userResponse)
def admin_route(
    current_user: User = Depends(require_role("admin"))
):
    return current_user


# ---------------------------
# Register
# ---------------------------
@router.post(
    "/register",
    response_model=userResponse,
    status_code=201
)
def register_user(
    user: userCreate,
    db: Session = Depends(get_db)
):
    # Check if username already exists
    result = db.execute(
        select(User).where(User.username == user.username)
    )

    existing_user = result.scalar_one_or_none()

    if existing_user:
        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    # Hash password
    hashed_password = hash_password(user.password)

    # Create new user
    new_user = User(
        username=user.username,
        password_hash=hashed_password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user


# ---------------------------
# Login
# ---------------------------
@router.post("/login")
def login_user(
    user: userLogin,
    db: Session = Depends(get_db)
):
    # Find user
    result = db.execute(
        select(User).where(User.username == user.username)
    )

    existing_user = result.scalar_one_or_none()

    if existing_user is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    # Verify password
    if not verify_password(
        user.password,
        existing_user.password_hash
    ):
        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    # Create JWT
    # 60 seconds is temporary for testing expiry.
    token = create_access_token(
        data={"sub": str(existing_user.id)},
        expires_delta=timedelta(seconds=60)
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# ---------------------------
# Normal protected route
# ---------------------------
@router.get("/protected", response_model=userResponse)
def protected_route(
    current_user: User = Depends(get_current_user)
):
    return current_user