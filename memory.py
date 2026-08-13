from database import get_connection

# Short-Term Memory
# ---------------------------------------
short_term_memory = []

# Save Memory
# ---------------------------------------
def save_memory(patient_name, symptoms, analysis):
    short_term_memory.append({
        "patient_name": patient_name,
        "symptoms": symptoms,
        "analysis": analysis
    })

    # Save consultation to PostgreSQL
    # -----------------------------------
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO memory
        (
            patient_name,
            symptoms,
            illness,
            severity
        )
        VALUES (%s, %s, %s, %s)
        """,
        (
            patient_name,
            ", ".join(symptoms),
            analysis.get("illness", "Unknown"),
            analysis.get("severity", "Unknown")
        )
    )

    conn.commit()

    cursor.close()
    conn.close()


# Get Short-Term Memory
# ---------------------------------------
def get_short_term_memory():
    if not short_term_memory:
        return None

    return short_term_memory[-1]


# Get Last Consultation
# ---------------------------------------
def get_last_memory():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT
            patient_name,
            symptoms,
            illness,
            severity,
            visit_time
        FROM memory
        ORDER BY id DESC
        LIMIT 1
        """
    )

    data = cursor.fetchone()

    cursor.close()
    conn.close()

    return data