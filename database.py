import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def get_connection():
    """
    Connect to PostgreSQL database.
    """

    database_url = os.getenv("DATABASE_URL")

    if not database_url:
        raise Exception("DATABASE_URL is not configured.")

    return psycopg2.connect(
        database_url,
        sslmode="require"
    )


def create_database():
    """
    Create required tables if they do not already exist.
    """

    conn = get_connection()
    cursor = conn.cursor()

    # Users table
    # -----------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username VARCHAR(100) UNIQUE NOT NULL,
            password TEXT NOT NULL
        )
    """)

    # Consultation memory table
    # -----------------------------
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS memory (
            id SERIAL PRIMARY KEY,
            patient_name VARCHAR(100),
            symptoms TEXT,
            illness VARCHAR(200),
            severity VARCHAR(50),
            visit_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    """)

    conn.commit()

    cursor.close()
    conn.close()