import html
from pathlib import Path

import joblib
import streamlit as st


st.set_page_config(
    page_title="HR Assistant",
    page_icon="🤖",
    layout="wide",
)

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "hr_chatbot.pkl"


@st.cache_resource
def load_chatbot(model_path: Path):
    return joblib.load(model_path)


if not MODEL_PATH.exists():
    st.error(
        "HR chatbot model not found. Please keep hr_chatbot.pkl in the same folder as app.py."
    )
    st.stop()

try:
    chatbot = load_chatbot(MODEL_PATH)
    model = chatbot["model"]
    responses = chatbot["responses"]
    threshold = chatbot["threshold"]
except Exception as error:
    st.error(f"Could not load the chatbot model: {error}")
    st.stop()


st.markdown(
    """
    <style>
    :root {
        --bg: #f3f7fb;
        --panel: rgba(255, 255, 255, 0.9);
        --primary: #0f4c81;
        --primary-soft: #dfeefb;
        --accent: #2a9d8f;
        --text: #1d2d3d;
        --muted: #5a6b7d;
        --bot: #edf6ff;
        --user: #eafaf3;
        --shadow: 0 8px 24px rgba(15, 76, 129, 0.12);
    }

    html, body, [data-testid="stAppViewContainer"] {
        background: linear-gradient(135deg, #eef5ff 0%, #f9fbff 50%, #f0f7f5 100%);
        color: var(--text);
    }

    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
    }

    .hero {
        background: linear-gradient(135deg, #123d66 0%, #1b5f9d 50%, #2a9d8f 100%);
        border-radius: 22px;
        padding: 1.5rem 1.75rem;
        margin-bottom: 1.25rem;
        box-shadow: var(--shadow);
    }

    .hero-title {
        color: white;
        font-size: 2.3rem;
        font-weight: 800;
        margin: 0;
        letter-spacing: -0.04em;
    }

    .hero-subtitle {
        color: rgba(255,255,255,0.9);
        font-size: 1.05rem;
        margin-top: 0.5rem;
    }

    .feature-row {
        display: flex;
        gap: 0.8rem;
        flex-wrap: wrap;
        margin-bottom: 1rem;
    }

    .feature-badge {
        background: rgba(255,255,255,0.12);
        border: 1px solid rgba(255,255,255,0.2);
        color: white;
        border-radius: 999px;
        padding: 0.45rem 0.8rem;
        font-size: 0.8rem;
        font-weight: 600;
    }

    .section-card {
        background: rgba(255,255,255,0.74);
        border: 1px solid rgba(18, 61, 102, 0.08);
        border-radius: 18px;
        padding: 1rem 1.1rem;
        box-shadow: var(--shadow);
        margin-bottom: 1rem;
    }

    .prompt-chip {
        display: inline-block;
        background: #edf5ff;
        border: 1px solid #cfe2ff;
        color: #1b4f8a;
        border-radius: 999px;
        padding: 0.5rem 0.8rem;
        margin: 0.25rem 0.4rem 0.4rem 0;
        font-size: 0.8rem;
        font-weight: 600;
        cursor: pointer;
    }

    .chat-user {
        background: linear-gradient(180deg, #eafaf3 0%, #e7f8ee 100%);
        border: 1px solid rgba(42, 157, 143, 0.12);
        color: var(--text);
        padding: 14px 16px;
        border-radius: 16px;
        margin: 10px 0;
        box-shadow: 0 4px 14px rgba(42, 157, 143, 0.08);
    }

    .chat-bot {
        background: linear-gradient(180deg, #eef6ff 0%, #edf4ff 100%);
        border: 1px solid rgba(15, 76, 129, 0.10);
        color: var(--text);
        padding: 14px 16px;
        border-radius: 16px;
        margin: 10px 0;
        box-shadow: 0 4px 14px rgba(15, 76, 129, 0.08);
    }

    .stChatInput {
        position: sticky;
        bottom: 0;
        background: transparent;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, #f7fbff 0%, #eef7fb 100%);
    }

    .sidebar-title {
        font-size: 1.4rem;
        font-weight: 800;
        color: var(--primary);
    }

    .sidebar-item {
        color: var(--text);
        margin: 0.25rem 0;
        font-size: 0.97rem;
    }
    </style>
    """,
    unsafe_allow_html=True,
)


st.markdown(
    """
    <div class="hero">
        <div class="hero-title">🤖 HR Assistant</div>
        <div class="hero-subtitle">Your AI-powered Human Resources Support Desk</div>
        <div class="feature-row">
            <span class="feature-badge">Leave & Attendance</span>
            <span class="feature-badge">Payroll & Salary</span>
            <span class="feature-badge">Benefits</span>
            <span class="feature-badge">Recruitment</span>
            <span class="feature-badge">Policies</span>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

with st.container():
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(
            """
            <div class="section-card">
                <div style="font-size: 0.82rem; color: #5a6b7d; text-transform: uppercase; letter-spacing: 0.08em;">Support</div>
                <div style="font-size: 1.5rem; font-weight: 800; color: #123d66; margin-top: 0.3rem;">HR Questions</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col2:
        st.markdown(
            """
            <div class="section-card">
                <div style="font-size: 0.82rem; color: #5a6b7d; text-transform: uppercase; letter-spacing: 0.08em;">Coverage</div>
                <div style="font-size: 1.5rem; font-weight: 800; color: #123d66; margin-top: 0.3rem;">10+ Topics</div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    with col3:
        st.markdown(
            """
            <div class="section-card">
                <div style="font-size: 0.82rem; color: #5a6b7d; text-transform: uppercase; letter-spacing: 0.08em;">Status</div>
                <div style="font-size: 1.5rem; font-weight: 800; color: #123d66; margin-top: 0.3rem;">Live Assistant</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

sample_prompts = [
    "How do I apply for leave?",
    "What is the policy for work from home?",
    "How does salary payroll work?",
    "What are the employee benefits?",
]

st.markdown('<div class="section-card"><div style="font-size: 0.85rem; color: #5a6b7d; text-transform: uppercase; letter-spacing: 0.08em; margin-bottom: 0.5rem;">Quick prompts</div>', unsafe_allow_html=True)
for prompt in sample_prompts:
    st.markdown(
        f'<div class="prompt-chip" onclick="this.innerText=\'{prompt}\'">{prompt}</div>',
        unsafe_allow_html=True,
    )
st.markdown("</div>", unsafe_allow_html=True)

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.markdown('<div class="sidebar-title">HR Assistant</div>', unsafe_allow_html=True)
    st.markdown("<div class='sidebar-item'>I can help with:</div>", unsafe_allow_html=True)
    st.write("✅ Leave & Attendance")
    st.write("✅ Salary & Payroll")
    st.write("✅ Work From Home")
    st.write("✅ Employee Benefits")
    st.write("✅ Recruitment")
    st.write("✅ Interviews")
    st.write("✅ Onboarding")
    st.write("✅ Resignation")
    st.write("✅ HR Policies")
    st.divider()

    if st.button("Clear Chat"):
        st.session_state.messages = []
        st.rerun()

for message in st.session_state.messages:
    content = html.escape(str(message["content"]))
    if message["role"] == "user":
        st.markdown(
            f'<div class="chat-user"><b>You:</b> {content}</div>',
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            f'<div class="chat-bot"><b>HR Assistant:</b> {content}</div>',
            unsafe_allow_html=True,
        )

user_input = st.chat_input("Ask your HR question...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

    probabilities = model.predict_proba([user_input])[0]
    max_probability = probabilities.max()
    predicted_intent = model.classes_[probabilities.argmax()]

    if max_probability < threshold:
        bot_response = (
            "I'm sorry, I couldn't confidently understand your question. "
            "Please try asking about leave, attendance, salary, payroll, "
            "benefits, recruitment, onboarding, resignation, or HR policies."
        )
    else:
        bot_response = responses[predicted_intent]

    st.session_state.messages.append({"role": "assistant", "content": bot_response})
    st.rerun()

st.divider()
st.caption(
    "AI HR Assistant • Please verify important employment decisions with your HR department."
)
