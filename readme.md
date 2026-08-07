# 🏥 AI Smart Hospital Assistant

## 📌 Project Overview
AI Smart Hospital Assistant is an intelligent healthcare assistant developed using **Python, Streamlit, LangChain, LangGraph, Google Gemini API, and SQLite**.

The application allows users to enter their symptoms, analyzes them using AI, predicts the possible illness and severity, recommends an appropriate doctor, suggests common medicines, provides precautions and a care plan, and supports follow-up healthcare questions through a conversational interface.

The project demonstrates **multi-agent AI architecture, LangGraph workflow execution, LangChain tools, short-term and long-term memory, conversational AI, and a user-friendly Streamlit interface.**


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


# 🛠 Technologies Used
- Python
- Streamlit
- LangChain
- LangGraph
- Google Gemini API
- SQLite
- Python Dotenv


# 🏗 System Architecture
```
                Patient

                   │

                   ▼

          Streamlit User Interface

                   │

                   ▼

             LangGraph Workflow

                   │

      ┌───────────────────────────┐

      ▼                           ▼

Decision Agent            Symptom Agent

                                   │

                                   ▼

                           Research Agent

                                   │

                                   ▼

                           Planning Agent

                                   │

                                   ▼

                            Memory Agent

                                   │

                                   ▼

                           Response Agent

                                   │

                                   ▼

                             Chat Agent

                                   │

                                   ▼

                              Final Output
```

# 🤖 Specialized AI Agents

## 1. Decision Agent
- Detect emergency symptoms.
- Decide whether immediate medical attention is required.
- Stop further execution in emergency cases.

## 2. Symptom Agent
Uses Google Gemini AI to:
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

## 5. Memory Agent
### Short-Term Memory
Stores current consultation during execution.

### Long-Term Memory
Stores consultation history inside SQLite database.
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
- Enter patient name
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
├── decision_agent.py
├── symptom_agent.py
├── research_agent.py
├── planning_agent.py
├── response_agent.py
├── memory_agent.py
├── chat_agent.py
├── tools.py
├── api_connector.py
├── requirements.txt
├── .env
└── README.md
```

# 🎯 Project Outcomes
- Designed multiple specialized AI agents.
- Implemented agent communication using LangGraph.
- Developed short-term conversational memory.
- Developed long-term knowledge retention using SQLite.
- Enabled context-aware healthcare conversations.
- Implemented LangChain tools.
- Integrated Streamlit frontend.
- Built an end-to-end AI healthcare assistant.


# 🔮 Future Enhancements
- Medical report upload
- Appointment booking
- Hospital management integration
- Authentication system
- Real-time healthcare APIs