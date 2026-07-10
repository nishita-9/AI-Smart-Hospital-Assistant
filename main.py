from decision_agent import decision_agent
from symptom_agent import symptom_agent
from planning_agent import planning_agent
from response_agent import response_agent

print("=" * 50)
print("AI SMART HOSPITAL ASSISTANT")
print("=" * 50)

user_input = input("Enter symptoms (comma separated): ")
symptoms = [s.strip() for s in user_input.split(",")]
decision = decision_agent(symptoms)

if decision["emergency"]:
    print("\n" + decision["message"])

else:
    analysis = symptom_agent(symptoms)
    plan = planning_agent(analysis)
    response_agent(analysis, plan)
