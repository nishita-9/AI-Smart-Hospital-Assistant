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
    .app-title {
        font-size: 2.2rem;
        font-weight: 700;
        color: #0f4c81;
        margin-bottom: 0px;
    }
    .app-subtitle {
        color: #5a6b7b;
        font-size: 1rem;
        margin-bottom: 1.5rem;
    }
    .result-card {
        background-color: #ffffff;
        border-radius: 12px;
        padding: 1.2rem 1.5rem;
        margin-bottom: 1rem;
        border: 1px solid #e3e9ef;
        box-shadow: 0 2px 6px rgba(0,0,0,0.04);
    }
    .result-label {
        font-size: 0.85rem;
        color: #8a97a3;
        text-transform: uppercase;
        letter-spacing: 0.05em;
    }
    .result-value {
        font-size: 1.25rem;
        font-weight: 600;
        color: #182a3d;
    }
    .emergency-box {
        background-color: #fdecea;
        border: 1px solid #f5c2c0;
        color: #9b2c2c;
        padding: 1rem 1.2rem;
        border-radius: 12px;
        font-weight: 600;
        white-space: pre-line;
    }
    .stButton>button {
        background-color: #0f4c81;
        color: white;
        border-radius: 8px;
        padding: 0.5rem 1.5rem;
        border: none;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #0c3c68;
        color: white;
    }
</style>
""", unsafe_allow_html=True)


# Keep track of things between reruns using session_state
# (Streamlit reruns the whole script every time you click something,
# so we store our results here instead of losing them)
# ------------------------------------------------------------
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""
    
if "result" not in st.session_state:
    st.session_state.result = None

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Login / Register
# ------------------------------------------------------------
if not st.session_state.logged_in:
    st.title("🏥 AI Smart Hospital Assistant")
    st.write("Login to access your hospital assistant.")
    login_tab, register_tab = st.tabs(["🔐 Login", "📝 Create Account"])

    # LOGIN
    # --------------------------------------------------------
    with login_tab:
        st.subheader("Login")
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
    # --------------------------------------------------------
    with register_tab:
        st.subheader("Create New Account")
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
    st.stop()

# Header
# ------------------------------------------------------------
st.markdown('<div class="app-title">🏥 AI Smart Hospital Assistant</div>', unsafe_allow_html=True)
st.markdown('<div class="app-subtitle">Describe your symptoms and get an AI-generated care plan.</div>', unsafe_allow_html=True)


# Sidebar: just a "start over" button
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


# Step 2: Show the results (if we have any)
# ------------------------------------------------------------
result = st.session_state.result

if result:
    decision = result["decision"]

    # ---------- Emergency case ----------
    if decision["emergency"]:
        message = emergency_tool.invoke({})
        st.markdown(f'<div class="emergency-box">{message}</div>', unsafe_allow_html=True)

    # ---------- Normal case ----------
    else:
        analysis = result["analysis"]
        research = result["research"]
        planning = result["planning"]

        st.subheader("Results")

        col1, col2 = st.columns(2)
        with col1:
            st.markdown(
                f'<div class="result-card"><div class="result-label">Possible Illness</div>'
                f'<div class="result-value">{analysis.get("illness", "Unknown")}</div></div>',
                unsafe_allow_html=True
            )
        with col2:
            st.markdown(
                f'<div class="result-card"><div class="result-label">Severity</div>'
                f'<div class="result-value">{analysis.get("severity", "Unknown")}</div></div>',
                unsafe_allow_html=True
            )

        col3, col4 = st.columns(2)
        with col3:
            st.markdown(
                f'<div class="result-card"><div class="result-label">Recommended Doctor</div>'
                f'<div class="result-value">{planning.get("doctor", "Unknown")}</div></div>',
                unsafe_allow_html=True
            )
        with col4:
            st.markdown(
                f'<div class="result-card"><div class="result-label">Suggested Medicine</div>'
                f'<div class="result-value">{planning.get("medicine", "Unknown")}</div></div>',
                unsafe_allow_html=True
            )

        st.markdown("#### 📝 Recommended Care Plan")
        for step in planning.get("plan", []):
            if step.strip():
                st.markdown(f"- {step}")

        st.markdown("#### ⚠️ Precautions")
        for note in research.get("precautions", []):
            if note.strip():
                st.markdown(f"- {note}")

        st.caption("This is an AI-generated suggestion, not a medical diagnosis. Please consult a real doctor.")

        
        # Step 3: Follow-up chat with the AI assistant
        # --------------------------------------------------------
        st.divider()
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
                memory = get_short_term_memory()
                answer = chat_agent(memory, question)

            with st.chat_message("assistant"):
                st.write(answer)
            st.session_state.chat_history.append(("assistant", answer))