# AI Smart Hospital Assistant

## Project Overview
AI Smart Hospital Assistant is a simple multi-agent system. It helps users by analyzing symptoms, generating a care plan, suggesting the appropriate doctor, and providing basic hospital information.

This project demonstrates AI agent coordination, tool usage, API integration, and memory implementation.

## Features
- Symptom Analysis using Gemini AI
- Decision Agent for emergency detection
- Care Planning Agent
- Doctor Recommendation Tool
- General Care Recommendation Tool
- Hospital API Connector
- Memory to store previous analyses
- Simple command-line interface

## Tech Stack
- Python
- LangChain
- Google Gemini API
- Requests
- JSON

## Project Structure
Hospital_AI_Assistant/

│── main.py
│── config.py
│── decision_agent.py
│── symptom_agent.py
│── planning_agent.py
│── response_agent.py
│── tools.py
│── api_connector.py
│── memory.py
│── memory.json
│── requirements.txt
│── .env
│── README.md

## Workflow
User
   │
Decision Agent
   │
Symptom Agent
   │
Planning Agent
   │
Tools & API Connector
   │
Response Agent