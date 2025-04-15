from app.db.database import Database
from app.models.post import Post
from fastapi import HTTPException

conn = Database("db.sqlite").get_connection()
cursor = conn.cursor()

def edit_post(post_id: str, edited_post: Post, user_id: str):
    post = cursor.execute("SELECT title, description, author_id FROM POSTS WHERE id = ?", [post_id]).fetchone()

    if user_id == post[2]:
        if post:
            cursor.execute("UPDATE POSTS SET title = ?, description = ? WHERE id = ?", [edited_post.title, edited_post.description, post_id])
            conn.commit()
        else:
            print(f"Post with id {id} not found")
    else:
        raise HTTPException(status_code=401, detail="Not Authenticated")
