from config import llm

chat_cache = {}

def chat_agent(memory, question):

    if question in chat_cache:
        return chat_cache[question]

    prompt = f"""
You are an AI Smart Hospital Assistant.

Possible Illness:
{memory["analysis"]["illness"]}

Severity:
{memory["analysis"]["severity"]}

The patient is asking a follow-up question.

Question:
{question}

Answer in simple language.

If the question is unrelated to healthcare,
politely say that you only answer health-related questions.
"""

    answer = llm.invoke(prompt).content
    chat_cache[question] = answer
    return answer