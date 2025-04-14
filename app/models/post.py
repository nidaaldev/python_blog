from pydantic import BaseModel
from datetime import date

class Post(BaseModel):
        title: str
        description: str
