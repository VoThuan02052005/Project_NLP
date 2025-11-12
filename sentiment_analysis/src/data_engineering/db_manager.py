import sqlite3
import pandas as pd
import os

def init_db(db_path='data/database/youtube_comments.db'):
    os.makedirs(os.path.dirname(db_path), exist_ok=True)
    conn = sqlite3.connect(db_path)
    conn.execute('''CREATE TABLE IF NOT EXISTS comments (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        video_id TEXT,
        video_title TEXT,
        author TEXT,
        text TEXT,
        likeCount INTEGER,
        publishedAt  TEXT
    );''')
    conn.close()

def insert_comments(df: pd.DataFrame, db_path='data/database/youtube_comments.db'):
    conn = sqlite3.connect(db_path)
    df.to_sql('comments', conn, if_exists='append', index=False)
    conn.close()
