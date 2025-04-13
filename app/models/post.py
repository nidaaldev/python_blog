from pydantic import BaseModel
from datetime import date

class Post(BaseModel):
        id: int
        title: str
        description: str
        date: date # iso 8601
