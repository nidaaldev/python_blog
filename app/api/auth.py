from fastapi import APIRouter, Request, HTTPException, Depends
from fastapi.responses import JSONResponse, Response
from fastapi.templating import Jinja2Templates
from app.models.user import User
from app.services.register_user import register_user as register
from sqlite3 import Error
from app.auth.utils import authenticate_user as auth_user, create_access_token, verify_token

router = APIRouter()
templates = Jinja2Templates(directory="templates")

@router.get('/register')
def register_page(request: Request):
    return templates.TemplateResponse("auth/register.html", { "request": request })

@router.post('/register')
def register_user(user: User):
    try:
        register(user)
        return { "registered": True }
    except Error as err:
        raise Error("Error: ", err)


@router.get('/login')
def login_page(request: Request):
    return templates.TemplateResponse("auth/login.html", { "request": request })

@router.post('/login')
def authenticate_user(user: User, response: Response):
    try:
        if auth_user(user.email, user.password):
            response.set_cookie(
                key="access_token",
                value=f"{create_access_token({ "email": user.email })}",
                httponly=True,
                samesite="strict"
            )
            return {"message": "Login successful"}
        else:
            raise HTTPException(status_code=401, detail="Incorrect email or password")
    except Error as err:
        raise Exception("Error:", err)

@router.post('/verifytoken')
def verify(current_user = Depends(verify_token)):
    return { "user": current_user }

@router.post("/logout")
def logout(response: Response):
    response = JSONResponse(content={"message": "Logout successful"})
    response.delete_cookie(key="access_token")
    return response

@router.get('/users/me')
def user_info(current_user = Depends(verify_token)):
    return current_user
