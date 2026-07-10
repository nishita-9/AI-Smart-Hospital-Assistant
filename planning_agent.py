from config import llm

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
    return plan