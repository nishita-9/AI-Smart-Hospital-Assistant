from config import llm

def doctor_tool(illness):
    prompt = f"""
A patient has {illness}.

Suggest the most suitable doctor.

Return only the doctor's specialization.

Example:
General Physician
Cardiologist
Neurologist
"""

    response = llm.invoke(prompt)
    return response.content.strip()


def medicine_tool(illness):
    prompt = f"""
A patient has {illness}.

Suggest only 2 general care recommendations.

Do not prescribe strong medicines.
Keep the answer short.
"""

    response = llm.invoke(prompt)
    return response.content.strip()


def emergency_tool():
    prompt = """
A patient has an emergency.

Return only the emergency helpline number and one short instruction.
"""

    response = llm.invoke(prompt)
    return response.content.strip()