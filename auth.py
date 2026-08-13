from database import get_connection

# Register New User
# ---------------------------------------
def register_user(username, password):
    username = username.strip()

    if not username or not password:
        return False, "Username and password are required."

    conn = get_connection()
    cursor = conn.cursor()

    try:
        # Check whether username already exists
        cursor.execute(
            """
            SELECT id
            FROM users
            WHERE username = %s
            """,
            (username,)
        )

        existing_user = cursor.fetchone()

        if existing_user:
            return False, "Username already exists."

        # Save new user
        cursor.execute(
            """
            INSERT INTO users (username, password)
            VALUES (%s, %s)
            """,
            (username, password)
        )

        conn.commit()
        return True, "Account created successfully."

    except Exception as e:
        conn.rollback()
        return False, "Registration failed."

    finally:
        cursor.close()
        conn.close()


# Login
# ---------------------------------------
def authenticate(username, password):
    username = username.strip()

    conn = get_connection()
    cursor = conn.cursor()

    try:
        cursor.execute(
            """
            SELECT password
            FROM users
            WHERE username = %s
            """,
            (username,)
        )

        user = cursor.fetchone()

        if user and user[0] == password:
            return True

        return False

    finally:
        cursor.close()
        conn.close()