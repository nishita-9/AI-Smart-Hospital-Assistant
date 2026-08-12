import sqlite3

def create_database():
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()

    # Users Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL
    )
    """)

    # Consultation Memory Table
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS memory(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT,
        patient_name TEXT,
        symptoms TEXT,
        illness TEXT,
        severity TEXT,
        visit_time TEXT
    )
    """)

    conn.commit()
    conn.close()