from graph import hospital_graph
from response_agent import response_agent
from tools import emergency_tool
from database import create_database
from memory_agent import get_short_term_memory
from chat_agent import chat_agent

create_database()

print("=" * 50)
print("AI SMART HOSPITAL ASSISTANT")
print("=" * 50)


# Patient Details
# -----------------------------
patient_name = input("Enter Patient Name: ")
user_input = input("Enter symptoms (comma separated): ")
symptoms = [s.strip() for s in user_input.split(",")]


# LangGraph State
# -----------------------------
state = {
    "patient_name": patient_name,
    "symptoms": symptoms
}


# Execute LangGraph Workflow
# -----------------------------
result = hospital_graph.invoke(state)
decision = result["decision"]


# Emergency Check
# -----------------------------
if decision["emergency"]:
    print(emergency_tool.invoke({}))


# Normal Workflow
# -----------------------------
else:
    analysis = result["analysis"]
    research = result["research"]
    planning = result["planning"]
    response_agent(analysis, planning, research)


    # Follow-up Conversation
    # -----------------------------
    print("\n" + "=" * 50)
    print("You can now ask health-related follow-up questions.")
    print("Type 'exit' to end the consultation.")
    print("=" * 50)

    while True:

        question = input("\nYou: ")

        if question.lower() == "exit":
            print("\nThank you for using AI Smart Hospital Assistant.")
            break

        memory = get_short_term_memory()
        answer = chat_agent(memory, question)
        print("\nAssistant:", answer)