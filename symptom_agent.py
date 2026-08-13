import json
from config import llm
from memory import save_memory

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
    try:
        response = llm.invoke(prompt)

        result = response.content

        # Convert response to string if necessary
        if not isinstance(result, str):
            result = str(result)

        result = result.strip()

        # Remove markdown if Gemini adds it
        result = result.replace("```json", "")
        result = result.replace("```", "")
        result = result.strip()

        # Find JSON object
        start = result.find("{")
        end = result.rfind("}")

        if start == -1 or end == -1:
            raise ValueError("Gemini did not return valid JSON.")

        result = result[start:end + 1]

        # Convert JSON to dictionary
        data = json.loads(result)

    except Exception as e:
        print("Symptom Agent Error:", e)

        return {
            "illness": "Unknown",
            "severity": "Unknown",
            "cause": "Unable to analyze symptoms.",
            "doctor": "Unknown",
            "medicine": "Unknown",
            "precautions": [],
            "care_plan": []
        }

    try:
        save_memory(
            patient_name,
            symptoms,
            data
        )

    except Exception as e:
        print("Memory/Database Error:", e)

    return data