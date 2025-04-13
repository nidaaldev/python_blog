from fastapi import APIRouter, HTTPException, Request, Depends
from app.db.database import Database
from app.models.post import Post
from fastapi.templating import Jinja2Templates
from app.services.create_post import create_post as new_post
from sqlite3 import Error
from jose import JWTError, jwt
from app.auth.utils import verify_token

router = APIRouter()
conn = Database("db.sqlite").get_connection()
templates = Jinja2Templates(directory="templates")

@router.get('/posts')
def get_posts(request: Request):
    cursor = conn.cursor()
    posts = cursor.execute("SELECT * FROM POSTS").fetchall()

    return templates.TemplateResponse('posts/posts.html', {"request": request, "posts": posts})

@router.get('/create-post')
def get_create_post_page(request: Request):
    return templates.TemplateResponse('posts/create-post.html', {"request": request})

@router.post('/create-post')
def create_post(post: Post):
    try:
        new_post(post)
    except Error as err:
        if err.sqlite_errorcode == 1555:
            raise HTTPException(status_code=409, detail="ID Already Exists")
        else:
            raise HTTPException(status_code=409, detail="Error when creating post")

@router.get('/posts-auth')
def get_posts_auth(request: Request, current_user = Depends(verify_token)):
    cursor = conn.cursor()
    posts = cursor.execute("SELECT * FROM POSTS").fetchall()
    print("auth")

    return templates.TemplateResponse('posts/posts-auth.html', {"request": request, "posts": posts})


