from typing import Union
from fastapi import FastAPI
from app.db.database import Database
from app.api.blog import router as blog_router
from app.api.auth import router as auth_router
from jinja2 import Environment, PackageLoader, select_autoescape

app = FastAPI()
env = Environment(
    loader=PackageLoader("app"),
    autoescape=select_autoescape
)

db = Database("db.sqlite")
app.include_router(blog_router)
app.include_router(auth_router)
