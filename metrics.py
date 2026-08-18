import time
from database import get_connection

def save_metric(metric_name, metric_value):

    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO metrics (metric_name, metric_value)
        VALUES (%s, %s)
        """,
        (metric_name, metric_value)
    )

    conn.commit()

    cursor.close()
    conn.close()