import sqlite3

def create_database():

    conn = sqlite3.connect("hospital.db")

    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS memory(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        patient_name TEXT,
        symptoms TEXT,
        illness TEXT,
        severity TEXT,
        visit_time TEXT           
    )
    """)

    conn.commit()
    conn.close()