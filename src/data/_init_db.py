import sqlite3

def _init_():
    conn = sqlite3.connect('./attendance.db')
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE attendance(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            status TEXT NOT NULL,
            datetime TEXT NOT NULL
        );
    """)

    cur.commit() #DBファイルの更新
    cur.close()

if __name__ == "__main__":
    _init_()