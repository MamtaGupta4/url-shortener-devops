import sqlite3


def create_database():
    conn = sqlite3.connect("urls.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS urls (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            long_url TEXT NOT NULL,
            short_code TEXT UNIQUE NOT NULL
        )
    """)

    conn.commit()
    conn.close()


def save_url(long_url, short_code):
    conn = sqlite3.connect("urls.db")
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO urls (long_url, short_code) VALUES (?, ?)",
        (long_url, short_code)
    )

    conn.commit()
    conn.close()


def get_long_url(short_code):
    conn = sqlite3.connect("urls.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT long_url FROM urls WHERE short_code=?",
        (short_code,)
    )

    result = cursor.fetchone()

    conn.close()

    return result