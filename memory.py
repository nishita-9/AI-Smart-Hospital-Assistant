memory = []

def save_memory(symptoms, analysis):

    memory.append({
        "symptoms": symptoms,
        "analysis": analysis
    })

def get_memory():
    return memory