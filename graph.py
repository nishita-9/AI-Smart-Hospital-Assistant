from typing import TypedDict

from langgraph.graph import StateGraph, START, END

from decision_agent import decision_agent
from symptom_agent import symptom_agent
from research_agent import research_agent
from planning_agent import planning_agent


# Graph State
# -----------------------------
class HospitalState(TypedDict):
    patient_name: str
    symptoms: list
    decision: dict
    analysis: dict
    research: str
    planning: dict


# Decision Node
# -----------------------------
def decision_node(state: HospitalState):

    decision = decision_agent(state["symptoms"])
    state["decision"] = decision
    return state


# Symptom Node
# -----------------------------
def symptom_node(state: HospitalState):

    if state["decision"]["emergency"]:
        return state

    analysis = symptom_agent(
        state["patient_name"],
        state["symptoms"]
    )

    state["analysis"] = analysis
    return state


# Research Node
# -----------------------------
def research_node(state: HospitalState):

    if state["decision"]["emergency"]:
        return state

    research = research_agent(
        state["analysis"]
    )

    state["research"] = research
    return state


# Planning Node
# -----------------------------
def planning_node(state: HospitalState):

    if state["decision"]["emergency"]:
        return state

    planning = planning_agent(
        state["analysis"],
        state["research"]
    )

    state["planning"] = planning
    return state


# Build Graph
# -----------------------------
builder = StateGraph(HospitalState)

builder.add_node("decision", decision_node)
builder.add_node("symptom", symptom_node)
builder.add_node("research", research_node)
builder.add_node("planning", planning_node)

builder.add_edge(START, "decision")
builder.add_edge("decision", "symptom")
builder.add_edge("symptom", "research")
builder.add_edge("research", "planning")
builder.add_edge("planning", END)

hospital_graph = builder.compile()