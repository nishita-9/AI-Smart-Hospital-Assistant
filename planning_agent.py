from config import llm
from tools import doctor_tool, medicine_tool

def planning_agent(analysis):

    prompt = f"""
You are a healthcare assistant.

Patient Details:

Possible Illness: {analysis['illness']}
Severity: {analysis['severity']}

Give exactly 4 simple care recommendations.

Return only the recommendations as bullet points.
"""

    response = llm.invoke(prompt)
    plan = response.content.split("\n")
    
    doctor = doctor_tool(analysis["illness"])
    medicine = medicine_tool(analysis["illness"])

    return {
        "plan": plan,
        "doctor": doctor,
        "medicine": medicine
    }