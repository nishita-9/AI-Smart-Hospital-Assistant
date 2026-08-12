import sqlite3

def register_user(username, password):
    username = username.strip()

    if not username or not password:
        return False, "Username and password are required."

    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            INSERT INTO users(username, password)
            VALUES(?, ?)
            """,
            (username, password)
        )

        conn.commit()
        return True, "Account created successfully."

    except sqlite3.IntegrityError:
        return False, "Username already exists."

    finally:
        conn.close()


def authenticate(username, password):
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT username
        FROM users
        WHERE username = ? AND password = ?
        """,
        (username, password)
    )

    user = cursor.fetchone()
    conn.close()

    if user:
        return True

    return False