import streamlit as st

from graph import hospital_graph
from database import create_database
from tools import emergency_tool
from memory import get_short_term_memory
from chat_agent import chat_agent
from auth import authenticate, register_user

# Basic page setup
# ------------------------------------------------------------
st.set_page_config(
    page_title="AI Smart Hospital Assistant",
    page_icon="🏥",
    layout="centered"
)

create_database()

# Simple custom styling 
# ------------------------------------------------------------
st.markdown("""
<style>
    .stApp {
        background-color: #f6f9fb;
    }

    .app-title {
        font-size: 2.4rem;
        font-weight: 800;
        color: #0b2540;
        margin-bottom: 0.6rem;
        text-align: center;
    }
    .app-subtitle {
        color: #5a6b7b;
        font-size: 1.05rem;
        margin-bottom: 1.8rem;
        text-align: center;
        max-width: 620px;
        margin-left: auto;
        margin-right: auto;
    }
    /* Streamlit's built-in tabs to look like Login / Create Account tabs */
    .stTabs [data-baseweb="tab-list"] {
        gap: 1.5rem;
        justify-content: center;
    }
    .stTabs [data-baseweb="tab"] {
        font-weight: 600;
        color: #5a6b7b;
    }
    .stTabs [aria-selected="true"] {
        color: #c0392b;
        border-bottom-color: #c0392b;
    }
    .step-label {
        color: #0f4c81;
        font-weight: 700;
        font-size: 0.85rem;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 0.3rem;
    }
    .section-card {
        background-color: #ffffff;
        border-radius: 16px;
        padding: 1.5rem 1.6rem;
        margin-bottom: 1.3rem;
        border: 1px solid #e3e9ef;
        box-shadow: 0 4px 14px rgba(15, 40, 70, 0.05);
    }
    .login-card {
        background-color: #ffffff;
        border-radius: 16px;
        padding: 1.5rem 1.6rem;
        margin: 0 auto 1.3rem auto;
        max-width: 460px;
        border: 1px solid #e3e9ef;
        box-shadow: 0 4px 14px rgba(15, 40, 70, 0.05);
    }
    .result-card {
        background-color: #ffffff;
        border-radius: 14px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1rem;
        border: 1px solid #e3e9ef;
        box-shadow: 0 2px 8px rgba(15, 40, 70, 0.05);
    }
    .result-label {
        font-size: 0.8rem;
        color: #8a97a3;
        text-transform: uppercase;
        letter-spacing: 0.06em;
    }
    .result-value {
        font-size: 1.3rem;
        font-weight: 700;
        color: #0b2540;
    }
    .emergency-box {
        background-color: #fdecea;
        border: 1px solid #f5c2c0;
        color: #9b2c2c;
        padding: 1.1rem 1.3rem;
        border-radius: 14px;
        font-weight: 600;
        white-space: pre-line;
    }
    .disclaimer-box {
        background-color: #fff8e8;
        border: 1px solid #f2e2b3;
        color: #7a5c00;
        padding: 0.8rem 1rem;
        border-radius: 10px;
        font-size: 0.85rem;
        margin-top: 0.8rem;
    }
    .stButton>button {
        background-color: #0f4c81;
        color: white;
        border-radius: 10px;
        padding: 0.6rem 1.6rem;
        border: none;
        font-weight: 700;
    }
    .stButton>button:hover {
        background-color: #0c3c68;
        color: white;
    }

    /* ---- Landing page sections ---- */
    .section-heading {
        text-align: center;
        font-size: 1.8rem;
        font-weight: 800;
        color: #0b2540;
        margin-top: 1.5rem;
    }
    .section-subheading {
        text-align: center;
        color: #5a6b7b;
        font-size: 0.95rem;
        margin-bottom: 1.2rem;
    }
    .how-card {
        background-color: #e8f0f8;
        border-radius: 14px;
        padding: 1.2rem 1.3rem;
        height: 100%;
    }
    .how-icon {
        font-size: 1.4rem;
        margin-bottom: 0.4rem;
    }
    .how-title {
        font-weight: 700;
        color: #0b2540;
        margin-bottom: 0.3rem;
    }
    .how-text {
        color: #5a6b7b;
        font-size: 0.85rem;
    }
    .who-card {
        background-color: #ffffff;
        border: 1px solid #e3e9ef;
        border-left: 4px solid #0f4c81;
        border-radius: 10px;
        padding: 1rem 1.2rem;
        margin-bottom: 0.8rem;
    }
    .who-title {
        font-weight: 700;
        color: #0b2540;
        margin-bottom: 0.3rem;
    }
    .who-text {
        color: #5a6b7b;
        font-size: 0.85rem;
    }
</style>
""", unsafe_allow_html=True)


# Keep track of things between reruns using session_state
# ------------------------------------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

if "result" not in st.session_state:
    st.session_state.result = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "memory" not in st.session_state:
    st.session_state.memory = None

# Login / Register
# ------------------------------------------------------------
if not st.session_state.logged_in:
    st.markdown('<div class="app-title">🏥 AI Smart Hospital Assistant</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="app-subtitle">Describe your symptoms and get an AI-generated care plan</div>',
        unsafe_allow_html=True
    )

    # A real bordered container, centered using columns
    left_gap, center_col, right_gap = st.columns([1, 3, 1])
    with center_col:
        with st.container(border=True):
            login_tab, register_tab = st.tabs(["🔐 Login", "📝 Create Account"])

            # LOGIN
            # ------------------------------------------------------
            with login_tab:
                st.subheader("Welcome back")
                login_username = st.text_input("Username", key="login_username")
                login_password = st.text_input("Password", type="password", key="login_password")

                if st.button("Login", key="login_button"):
                    if authenticate(login_username, login_password):
                        st.session_state.logged_in = True
                        st.session_state.username = login_username
                        st.success("Login successful!")
                        st.rerun()
                    else:
                        st.error("Invalid username or password.")

            # CREATE ACCOUNT
            # ------------------------------------------------------
            with register_tab:
                st.subheader("Create your account")
                new_username = st.text_input("Username", key="new_username")
                new_password = st.text_input("Password", type="password", key="new_password")

                if st.button("Create Account", key="register_button"):
                    if not new_username or not new_password:
                        st.warning("Please enter username and password.")
                    else:
                        success, message = register_user(new_username, new_password)

                        if success:
                            st.success(message)
                            st.info(
                                "Your account has been created. "
                                "Please go to the Login tab."
                            )
                        else:
                            st.error(message)

    # ---- How To Use ----
    # ----------------------------------------------------------
    st.markdown('<div class="section-heading">How To Use</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="section-subheading">Get your care plan in just a few simple steps.</div>',
        unsafe_allow_html=True
    )
    how_col1, how_col2, how_col3 = st.columns(3)
    with how_col1:
        st.markdown(
            '<div class="how-card"><div class="how-icon">📝</div>'
            '<div class="how-title">Input Your Symptoms</div>'
            '<div class="how-text">Enter your single or multiple symptoms into the checker.</div></div>',
            unsafe_allow_html=True
        )
    with how_col2:
        st.markdown(
            '<div class="how-card"><div class="how-icon">💬</div>'
            '<div class="how-title">Get AI Analysis</div>'
            '<div class="how-text">Our AI agents analyze your symptoms and check for emergencies.</div></div>',
            unsafe_allow_html=True
        )
    with how_col3:
        st.markdown(
            '<div class="how-card"><div class="how-icon">📋</div>'
            '<div class="how-title">Receive Your Results</div>'
            '<div class="how-text">Instantly get a possible illness, severity, and care plan.</div></div>',
            unsafe_allow_html=True
        )

    # ---- What Our AI Assistant Does ----
    # ----------------------------------------------------------
    st.markdown('<div class="section-heading">What Our AI Assistant Does</div>', unsafe_allow_html=True)
    who_col1, who_col2 = st.columns(2)
    with who_col1:
        st.markdown(
            '<div class="who-card"><div class="who-title">🧠 AI Symptom Analysis</div>'
            '<div class="who-text">Analyzes the symptoms provided by the patient and identifies possible health conditions.</div></div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div class="who-card"><div class="who-title">🚨 Emergency Detection</div>'
            '<div class="who-text">Checks symptoms for possible emergency situations and highlights when immediate medical attention may be needed.</div></div>',
            unsafe_allow_html=True
        )
    with who_col2:
        st.markdown(
            '<div class="who-card"><div class="who-title">👨‍⚕️ Smart Care Planning</div>'
            '<div class="who-text">Provides a personalized care plan along with a suitable doctor or specialist recommendation.</div></div>',
            unsafe_allow_html=True
        )
        st.markdown(
            '<div class="who-card"><div class="who-title">💬 Follow-Up Conversation</div>'
            '<div class="who-text">Allows patients to ask follow-up questions and continue the conversation about their symptoms and results.</div></div>',
            unsafe_allow_html=True
        )

    st.stop()

# Header
# ------------------------------------------------------------
st.markdown('<div class="app-title">🏥 AI Smart Hospital Assistant</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="app-subtitle">Describe your symptoms and get an AI-generated care plan</div>',
    unsafe_allow_html=True
)

# Sidebar
# ------------------------------------------------------------
with st.sidebar:
    st.header("🏥 AI Hospital Assistant")
    st.caption(
        f"Logged in as: {st.session_state.username}"
    )
    st.divider()

    if st.button("🔄 Start New Consultation"):
        st.session_state.result = None
        st.session_state.chat_history = []
        st.rerun()

    if st.button("🚪 Logout"):
        st.session_state.logged_in = False
        st.session_state.username = ""
        st.session_state.result = None
        st.session_state.chat_history = []
        st.rerun()


# Step 1: Patient form (name + symptoms)
# ------------------------------------------------------------
st.markdown('<div class="step-label">Step 1 · General Information</div>', unsafe_allow_html=True)

with st.form("patient_form"):
    patient_name = st.text_input("Patient Name")
    symptoms_input = st.text_area("Symptoms (comma separated)", placeholder="e.g. fever, headache, sore throat")
    submitted = st.form_submit_button("🔍 Analyze Symptoms")


# When the form is submitted, run the AI agents
# ------------------------------------------------------------
if submitted:
    if not patient_name.strip() or not symptoms_input.strip():
        st.warning("Please enter both patient name and symptoms.")
    else:
        symptoms = [s.strip() for s in symptoms_input.split(",") if s.strip()]

        with st.spinner("Consulting AI agents..."):
            state = {
                 "username": st.session_state.username,
                 "patient_name": patient_name,
                 "symptoms": symptoms
            }
            result = hospital_graph.invoke(state)

        st.session_state.result = result
        st.session_state.chat_history = []
        st.session_state.memory = {
             "patient_name": patient_name,
             "symptoms": symptoms,
             "analysis": result.get("analysis", {})
        }

# Step 2: Show the results 
# ------------------------------------------------------------
result = st.session_state.result

if result:
    decision = result["decision"]

    # ---------- Emergency case ----------
    if decision["emergency"]:
        message = emergency_tool.invoke({})
        st.markdown(f'<div class="emergency-box">🚨 {message}</div>', unsafe_allow_html=True)

    # ---------- Normal case ----------
    else:
        analysis = result["analysis"]
        research = result["research"]
        planning = result["planning"]

        st.markdown('<div class="step-label">Step 2 · Your Results</div>', unsafe_allow_html=True)
        st.subheader("Results")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                f'<div class="result-card"><div class="result-label">🩺 Possible Illness</div>'
                f'<div class="result-value">{analysis.get("illness", "Unknown")}</div></div>',
                unsafe_allow_html=True
            )
        with col2:
            st.markdown(
                f'<div class="result-card"><div class="result-label">⚠️ Severity</div>'
                f'<div class="result-value">{analysis.get("severity", "Unknown")}</div></div>',
                unsafe_allow_html=True
            )

        col3, col4 = st.columns(2)
        with col3:
            st.markdown(
                f'<div class="result-card"><div class="result-label">👨‍⚕️ Recommended Doctor</div>'
                f'<div class="result-value">{planning.get("doctor", "Unknown")}</div></div>',
                unsafe_allow_html=True
            )
        with col4:
            st.markdown(
                f'<div class="result-card"><div class="result-label">💊 Suggested Medicine</div>'
                f'<div class="result-value">{planning.get("medicine", "Unknown")}</div></div>',
                unsafe_allow_html=True
            )

        st.markdown('<div class="section-card">', unsafe_allow_html=True)
        st.markdown("#### 📝 Recommended Care Plan")
        for step in planning.get("plan", []):
            if step.strip():
                st.markdown(f"- {step}")

        st.markdown("#### ⚠️ Precautions")
        for note in research.get("precautions", []):
            if note.strip():
                st.markdown(f"- {note}")
        st.markdown('</div>', unsafe_allow_html=True)

        st.markdown(
            '<div class="disclaimer-box">ℹ️ This is an AI-generated suggestion, not a medical diagnosis.'
            'Please consult a real doctor.</div>',
            unsafe_allow_html=True
        )

        # Step 3: Follow-up chat with the AI assistant
        # --------------------------------------------------------
        st.divider()
        st.markdown('<div class="step-label">Step 3 · Follow-up</div>', unsafe_allow_html=True)
        st.markdown("#### 💬 Ask a follow-up question")

        # Show the previous messages in this chat
        for role, text in st.session_state.chat_history:
            with st.chat_message(role):
                st.write(text)

        question = st.chat_input("Type a health-related question...")

        if question:
            # Show the user's message right away
            with st.chat_message("user"):
                st.write(question)
            st.session_state.chat_history.append(("user", question))

            # Ask the chat agent, using the last saved patient memory
            with st.spinner("Thinking..."):
                memory = st.session_state.memory
                answer = chat_agent(memory, question)

            with st.chat_message("assistant"):
                st.write(answer)
            st.session_state.chat_history.append(("assistant", answer))