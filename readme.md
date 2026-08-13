# 🏥 AI Smart Hospital Assistant

## 📌 Project Overview
AI Smart Hospital Assistant is an intelligent healthcare assistant developed using **Python, Streamlit, LangChain, LangGraph, Google Gemini API, and PostgreSQL**.

The application allows users to enter their symptoms and receive an AI-generated analysis of their possible illness and severity. It also provides healthcare precautions, a care plan, doctor and medicine recommendations, and allows users to ask follow-up healthcare questions through a conversational interface.

The project demonstrates **multi-agent AI architecture, LangGraph workflow orchestration, LangChain tools, short-term and long-term memory, conversational AI, authentication and a user-friendly Streamlit interface.**


# 🎯 Objectives
- Analyze patient symptoms using AI.
- Predict possible illness and severity.
- Detect emergency situations.
- Recommend an appropriate doctor.
- Suggest commonly used medicines.
- Generate precautions and a care plan.
- Answer follow-up healthcare questions.
- Store patient consultation history.
- Demonstrate multi-agent coordination using LangGraph.
- Provide a simple and interactive Streamlit interface.
- Prepare the application for cloud deployment.


# 🚀 Features
-  Streamlit-based graphical user interface
-  AI-powered symptom analysis
-  Emergency symptom detection
-  Doctor recommendation
-  Medicine recommendation
-  Care plan generation
-  Health precautions
-  Follow-up healthcare chatbot
-  Short-Term Memory
-  Long-Term Memory using SQLite
-  LangGraph workflow execution
-  LangChain custom tools
-  Consultation history storage
-  Cloud deployment support

# 🛠 Technologies Used
- Python
- Streamlit
- LangChain
- LangGraph
- Google Gemini API
- PostgreSQL


# 🏗 System Architecture
```
                         USER
                           │
                           ▼
                ┌─────────────────────┐
                │   Authentication    │
                │ Login / Registration│
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │   Streamlit UI      │
                │     Dashboard       │
                └──────────┬──────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │     LangGraph       │
                │Workflow Orchestrator│
                └──────────┬──────────┘
                           │
          ┌────────────────┼────────────────┐
          │                │                │
          ▼                ▼                ▼
   Decision Agent    Symptom Agent    Research Agent
          │                │                │
          │                └───────┬────────┘
          │                        │
          │                        ▼
          │                Planning Agent
          │                        │
          │                ┌───────┴────────┐
          │                │                │
          │                ▼                ▼
          │          Doctor Tool      Medicine Tool
          │
          ▼
   Emergency Handling
                           │
                           ▼
                   Response Agent
                           │
                           ▼
                    Final Results
                           │
                           ▼
                    Chat Agent
                           │
                           ▼
                 Follow-up Questions
                           │
                           ▼
                 Short-Term Memory
                           │
                           ▼
                 PostgreSQL Database
```

# 🤖 Specialized AI Agents

## 1. Decision Agent
- Detect emergency symptoms.
- Decide whether immediate medical attention is required.
- Stop further execution in emergency cases.

## 2. Symptom Agent
Uses Google Gemini API through LangChain to:
- Analyze symptoms
- Predict illness
- Determine severity
- Identify cause
- Recommend doctor
- Suggest medicine
- Generate precautions
- Generate care plan

## 3. Research Agent
- Retrieve healthcare precautions.
- Pass healthcare information to other agents.
- Share information during workflow execution.

## 4. Planning Agent
- Organize recommendations.
- Prepare doctor recommendation.
- Prepare medicine recommendation.
- Prepare care plan.

## 5. Memory 
### Short-Term Memory
Stores current consultation during execution.

### Long-Term Memory
Stores consultation history inside PostgreSQL database.
- Patient Name
- Symptoms
- Illness
- Severity
- Visit Time

## 6. Response Agent
- Display complete diagnosis.
- Display precautions.
- Display care plan.
- Display doctor recommendation.
- Display medicine recommendation.

## 7. Chat Agent
- Answer follow-up healthcare questions.
- Use previous consultation as context.
- Maintain conversational interaction.


# 🖥 Streamlit User Interface
The project provides a simple and interactive web interface using Streamlit.

Users can:
- Create an account
- Log in
- Enter patient details
- Enter symptoms
- View diagnosis
- View doctor recommendation
- View medicine recommendation
- View precautions
- View care plan
- Ask follow-up healthcare questions

Run the application using:
```bash
streamlit run app.py


# 📂 Project Structure
```
AI Smart Hospital Assistant
│
├── app.py                  # Streamlit User Interface
├── main.py                 # Main application
├── graph.py                # LangGraph workflow
├── config.py               # Gemini configuration
├── database.py             # SQLite database creation
├── hospital.db             # Long-term memory database
│
├── auth.py   
├── memory.py
│
├── decision_agent.py
├── symptom_agent.py
├── research_agent.py
├── planning_agent.py
├── response_agent.py
├── chat_agent.py
│
├── tools.py
├── api_connector.py
│
├── .env
└── README.md
```

# 🎯 Project Outcomes
- Designed multiple specialized AI agents.
- Implemented LangGraph-based workflow orchestration.
- Implemented LangChain tools.
- Developed short-term conversational memory.
- Developed long-term memory using PostgreSQL.
- Implemented follow-up conversational interaction.
- Integrated Streamlit frontend.
- Built an end-to-end AI healthcare assistant.


# 🔮 Future Enhancements
- Medical report upload
- Appointment booking
- Hospital management integration
- Real-time healthcare APIs
- Notification system.
- Advanced monitoring and analytics.