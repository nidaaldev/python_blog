from app.db.database import Database
from app.models.user import User
from fastapi import HTTPException
from app.auth.utils import get_password_hash
import uuid

conn = Database("db.sqlite").get_connection()

def register_user(user: User):
    cursor = conn.cursor()

    email = user.email

    results = cursor.execute("SELECT * FROM USERS WHERE EMAIL = (?)", [email]).fetchall()

    if len(results) > 0:
        raise HTTPException(status_code=400, detail="Email already registered")

    hashed_password = get_password_hash(user.password)

    cursor.execute("INSERT INTO USERS VALUES (?, ?, ?)", (str(uuid.uuid4()), email, hashed_password))
    conn.commit()
