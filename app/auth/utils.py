from passlib.context import CryptContext
from app.db.database import Database
from datetime import datetime, timedelta
from jose import jwt, JWTError
from dotenv import load_dotenv
from fastapi import Depends, Security, HTTPException, Request
import os

load_dotenv()

cursor = Database("db.sqlite").get_connection().cursor()

SECRET_KEY = os.getenv('SECRET_KEY')
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def get_password_hash(password):
    return pwd_context.hash(password)

def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

def authenticate_user(email: str, password: str):
    user = cursor.execute("SELECT * FROM USERS WHERE EMAIL = ?", [email]).fetchall()

    if not user or not verify_password(password, user[0][2]):
        return False

    return user[0]

def create_access_token(data: dict, expires_delta: timedelta = None):
    to_encode = { "email": data["email"] }

    expire = datetime.utcnow() + timedelta(minutes=30)
    to_encode["exp"] = expire

    token = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

    print(to_encode)

    return token

def get_current_user(request: Request):

    token = request.cookies.get('access_token')

    if not token:
        raise HTTPException(status_code=401, detail="Token not found")

    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=ALGORITHM)
        email: str = payload.get("email")

        if email is None:
            raise HTTPException(status_code=401, detail="Invalid authentication credentials")
        user = cursor.execute("SELECT * FROM USERS WHERE EMAIL = ?", [email]).fetchone()

        if user is None:
            raise HTTPException(status_code=401, detail="User not found")
        return user
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid token")

def verify_token(current_user=Depends(get_current_user)):
    return { "valid": True, "user": current_user }
