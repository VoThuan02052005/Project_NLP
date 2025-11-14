import sqlite3

def backup_sqlite_db(src_db_path, backup_db_path):
    source_conn = sqlite3.connect(src_db_path)
    backup_conn = sqlite3.connect(backup_db_path)
    with backup_conn:
        source_conn.backup(backup_conn)
    backup_conn.close()
    source_conn.close()

if __name__ == "__main__":
    backup_sqlite_db("../../data/database/youtube_comments.db", "../../data/database/backup/backup_database.db")
