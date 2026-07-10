import json
from config import llm
from memory import save_memory

def symptom_agent(symptoms):

    prompt = f"""
You are a medical assistant.

Analyze these symptoms:
{", ".join(symptoms)}

Return ONLY a JSON object like this:

{{
    "illness": "Common Cold",
    "severity": "Low"
}}
"""

    response = llm.invoke(prompt)
    result = response.content

    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    try:
        data = json.loads(result)

        save_memory(symptoms, data)

        return data

    except:
        return {
            "illness": "Unknown",
            "severity": "Unknown"
        }