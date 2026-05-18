"""JWT helpers, admin verification dependency and login endpoint."""
import os
from datetime import datetime, timedelta, timezone
import bcrypt
import jwt
from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials

from models import LoginRequest, LoginResponse

ADMIN_EMAIL = os.environ.get('ADMIN_EMAIL', 'admin@essbeeheaters.com')
ADMIN_PASSWORD_HASH = os.environ.get('ADMIN_PASSWORD_HASH', '').encode()
JWT_SECRET = os.environ.get('JWT_SECRET', 'change-me')
JWT_ALGORITHM = os.environ.get('JWT_ALGORITHM', 'HS256')
JWT_EXPIRE_HOURS = int(os.environ.get('JWT_EXPIRE_HOURS', '24'))

security = HTTPBearer()


def create_access_token(email: str) -> str:
    payload = {
        'sub': email,
        'exp': datetime.now(timezone.utc) + timedelta(hours=JWT_EXPIRE_HOURS),
        'iat': datetime.now(timezone.utc),
    }
    return jwt.encode(payload, JWT_SECRET, algorithm=JWT_ALGORITHM)


async def verify_admin(credentials: HTTPAuthorizationCredentials = Depends(security)) -> str:
    try:
        payload = jwt.decode(credentials.credentials, JWT_SECRET, algorithms=[JWT_ALGORITHM])
        email = payload.get('sub')
        if email != ADMIN_EMAIL:
            raise HTTPException(status_code=401, detail='Invalid token')
        return email
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail='Token expired')
    except jwt.InvalidTokenError:
        raise HTTPException(status_code=401, detail='Invalid token')


router = APIRouter()


@router.post("/admin/login", response_model=LoginResponse)
async def admin_login(req: LoginRequest):
    if req.email.lower() != ADMIN_EMAIL.lower():
        raise HTTPException(status_code=401, detail='Invalid email or password')
    try:
        valid = bcrypt.checkpw(req.password.encode(), ADMIN_PASSWORD_HASH)
    except Exception:
        valid = False
    if not valid:
        raise HTTPException(status_code=401, detail='Invalid email or password')
    token = create_access_token(req.email.lower())
    return LoginResponse(access_token=token, email=req.email.lower(), expires_in=JWT_EXPIRE_HOURS * 3600)


@router.get("/admin/me")
async def admin_me(email: str = Depends(verify_admin)):
    return {"email": email}
