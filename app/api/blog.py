from fastapi import APIRouter, HTTPException, Request, Depends
from app.db.database import Database
from app.models.post import Post
from fastapi.templating import Jinja2Templates
from app.services.create_post import create_post as new_post
from sqlite3 import Error
from jose import JWTError, jwt
from app.auth.utils import verify_token, get_current_user

router = APIRouter()
conn = Database("db.sqlite").get_connection()
templates = Jinja2Templates(directory="templates")

@router.get('/posts')
def get_posts(request: Request):
    cursor = conn.cursor()
    posts = cursor.execute("SELECT POSTS.TITLE, POSTS.DESCRIPTION, POSTS.DATE, USERS.email FROM POSTS INNER JOIN USERS ON POSTS.author_id=USERS.id").fetchall()

    return templates.TemplateResponse('posts/posts.html', {"request": request, "posts": posts})

# Experimental /API endpoint
@router.get('/api/posts/')
def get_posts(request: Request):
    cursor = conn.cursor()
    posts = cursor.execute("SELECT * FROM POSTS").fetchall()

    return posts

@router.get('/api/user/posts/')
def get_posts(request: Request, current_user = Depends(verify_token)):
    author_id = current_user["user"][0]
    cursor = conn.cursor()
    posts = cursor.execute("SELECT * FROM POSTS WHERE author_id = ?", [author_id]).fetchall()

    return posts

@router.get('/create-post')
def get_create_post_page(request: Request, current_user = Depends(verify_token) ):
    return templates.TemplateResponse('posts/create-post.html', {"request": request})

@router.post('/create-post')
def create_post(post: Post, current_user = Depends(verify_token)):
    try:
        user_id = current_user["user"][0]

        new_post(post, user_id)
    except Error as err:
            print("Error!", err)
            raise HTTPException(status_code=409, detail="Error when creating post")

@router.get('/dashboard')
def get_posts_auth(request: Request, current_user = Depends(verify_token)):
    cursor = conn.cursor()
    posts = cursor.execute("SELECT * FROM POSTS").fetchall()

    return templates.TemplateResponse('dashboard/dashboard.html', {"request": request, "posts": posts})


