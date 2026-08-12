import sqlite3
from datetime import datetime

# Short-Term Memory
short_term_memory = []

def save_memory(username, patient_name, symptoms, analysis):

    # ---------- Short-Term Memory ----------
    short_term_memory.append({
        "username": username,
        "patient_name": patient_name,
        "symptoms": symptoms,
        "analysis": analysis
    })
    visit_time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

    # ---------- Long-Term Memory ----------
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO memory(username, patient_name, symptoms, illness, severity, visit_time)
        VALUES(?,?,?,?,?,?)
        """,
        (
            username,
            patient_name,
            ",".join(symptoms),
            analysis["illness"],
            analysis["severity"],
            visit_time
        )
    )

    conn.commit()
    conn.close()

def get_short_term_memory():

    if short_term_memory:
        return short_term_memory[-1]

    return None

def get_user_records(username):
    conn = sqlite3.connect("hospital.db")
    cursor = conn.cursor()
    cursor.execute("""
    SELECT patient_name, symptoms, illness, severity, visit_time
    FROM memory
    WHERE username = ?               
    ORDER BY id DESC
    """,
    (username,)
    )

    records = cursor.fetchall()
    conn.close()
    return records