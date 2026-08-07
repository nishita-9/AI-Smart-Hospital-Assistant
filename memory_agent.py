import sqlite3
from datetime import datetime

# Short-Term Memory
short_term_memory = []

def save_memory(patient_name, symptoms, analysis):

    # ---------- Short-Term Memory ----------
    short_term_memory.append({
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
        INSERT INTO memory(patient_name, symptoms, illness, severity, visit_time)
        VALUES(?,?,?,?,?)
        """,
        (
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

def get_last_memory():

    conn = sqlite3.connect("hospital.db")

    cursor = conn.cursor()

    cursor.execute("""
    SELECT patient_name, symptoms, illness, severity, visit_time
    FROM memory
    ORDER BY id DESC
    LIMIT 1
    """)

    data = cursor.fetchone()

    conn.close()

    return data