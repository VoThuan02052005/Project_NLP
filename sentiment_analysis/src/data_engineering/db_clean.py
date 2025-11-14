import os
import sqlite3


def init_db1(db_path='../../data/database/youtube_comments_clean.db'):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.execute('''CREATE TABLE IF NOT EXISTS comments_clean (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        video_id TEXT,
        video_title TEXT,
        author TEXT,
        clean_text TEXT,
        likeCount INTEGER,
        publishedAt  TEXT
    );''')
    conn.close()
