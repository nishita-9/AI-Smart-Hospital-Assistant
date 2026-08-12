EMERGENCY_SYMPTOMS = [
    "chest pain",
    "difficulty breathing",
    "heavy bleeding",
    "unconscious"
]

def decision_agent(symptoms):
    symptoms = [symptom.lower().strip() for symptom in symptoms]

    for symptom in symptoms:
        if symptom in EMERGENCY_SYMPTOMS:
            return {
                "emergency": True,
                "message": "🚨 Emergency Detected! Seek immediate medical attention."
            }

    return {
        "emergency": False,
        "message": "Proceeding with symptom analysis..."
    }