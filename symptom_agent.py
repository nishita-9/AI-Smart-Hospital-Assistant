import json
from config import llm
from memory_agent import save_memory

def symptom_agent(patient_name, symptoms):

    prompt = f"""
You are an AI Smart Hospital Assistant.

Analyze the following symptoms:
{", ".join(symptoms)}

Return ONLY a valid JSON object in the following format.
Do NOT include markdown or explanations.

{{
    "illness": "Common Cold",
    "severity": "Low",

    "cause": "Short explanation of what causes this illness",

    "doctor": "General Physician",

    "medicine": "Paracetamol",

    "precautions": [
        "Precaution 1",
        "Precaution 2",
        "Precaution 3"
    ],

    "care_plan": [
        "Care Step 1",
        "Care Step 2",
        "Care Step 3"
    ]
}}
"""

    response = llm.invoke(prompt)

    result = response.content.strip()

    result = result.replace("```json", "")
    result = result.replace("```", "")
    result = result.strip()

    try:

        data = json.loads(result)

        save_memory(patient_name, symptoms, data)

        return data

    except Exception as e:

        print("JSON Error:", e)

        return {
            "illness": "Unknown",
            "severity": "Unknown",
            "cause": "Unknown",
            "doctor": "Unknown",
            "medicine": "Unknown",
            "precautions": [],
            "care_plan": []
        }