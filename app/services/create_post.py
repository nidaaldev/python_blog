from app.db.database import Database
from app.models.post import Post
import uuid
from datetime import date

conn = Database("db.sqlite").get_connection()

def create_post(post: Post, user_id: str):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO POSTS VALUES (?, ?, ?, ?, ?)", (str(uuid.uuid4()), post.title, post.description, date.today(), user_id))
    conn.commit()
    print("Post inserted!")
