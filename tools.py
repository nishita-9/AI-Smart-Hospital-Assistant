from langchain_core.tools import tool


@tool
def doctor_tool(doctor: str) -> str:
    """
    Returns the recommended doctor specialization.
    """
    return doctor


@tool
def medicine_tool(medicine: str) -> str:
    """
    Returns the recommended medicine.
    """
    return medicine


@tool
def emergency_tool() -> str:
    """
    Returns emergency instructions.
    """

    return """
🚨 Emergency Detected!

• Visit the nearest hospital immediately.
• Call emergency medical services if required.
• Do not ignore severe symptoms.
• Follow professional medical advice.
"""