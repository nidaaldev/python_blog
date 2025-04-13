from app.db.database import Database
from app.models.post import Post

conn = Database("db.sqlite").get_connection()

def create_post(post: Post):
    cursor = conn.cursor()
    cursor.execute("INSERT INTO POSTS VALUES (?, ?, ?, ?)", (post.id, post.title, post.description, post.date))
    conn.commit()
    print("Post inserted!")
