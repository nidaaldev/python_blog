from app.db.database import Database
from app.models.post import Post
from fastapi import HTTPException

conn = Database("db.sqlite").get_connection()
cursor = conn.cursor()

def delete_post(post_id: str, user_id: str):
    post = cursor.execute("SELECT author_id FROM POSTS WHERE id = ?", [post_id]).fetchone()

    if user_id == post[0]:
        if post:
            cursor.execute("DELETE FROM POSTS WHERE ID = ?", [post_id])
            conn.commit()
        else:
            print(f"Post with id {id} not found")
    else:
        raise HTTPException(status_code=401, detail="Not Authenticated")
