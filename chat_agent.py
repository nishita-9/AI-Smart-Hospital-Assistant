from config import llm

chat_cache = {}

def chat_agent(memory, question):

    if not memory:
        return "I could not find the current consultation details. Please analyze the symptoms again."

    analysis = memory.get("analysis", {})
    illness = analysis.get("illness", "Unknown")
    severity = analysis.get("severity", "Unknown")

    cache_key = (
        illness.lower().strip(),
        severity.lower().strip(),
        question.lower().strip()
    )

    # Check cache
    # ---------------------------------------
    if cache_key in chat_cache:
        return chat_cache[cache_key]

    prompt = f"""
You are an AI Smart Hospital Assistant.

Possible Illness:
{illness}

Severity:
{severity}

The patient is asking a follow-up question.

Question:
{question}

Answer in simple language.

If the question is unrelated to healthcare,
politely say that you only answer health-related questions.

Do not claim to provide a confirmed medical diagnosis.
"""


    # Call Gemini only if answer is not cached
    # ---------------------------------------
    try:
        answer = llm.invoke(prompt).content.strip()

        chat_cache[cache_key] = answer
        return answer

    except Exception as e:
        print("Chat Agent Error:", e)

        return "Sorry, I could not process your question right now."