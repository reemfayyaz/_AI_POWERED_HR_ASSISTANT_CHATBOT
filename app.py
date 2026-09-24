import html
import os
from pathlib import Path

import joblib
import streamlit as st


st.set_page_config(
    page_title="HR Assistant",
    page_icon="🤖",
    layout="centered",
)

MODEL_PATH = Path(__file__).resolve().parent / "hr_chatbot.pkl"


@st.cache_resource
def load_chatbot(model_path: Path):
    return joblib.load(model_path)


if not MODEL_PATH.exists():
    st.error(
        "HR chatbot model not found. Please keep hr_chatbot.pkl "
        "in the same folder as app.py."
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
    .main-title { font-size: 38px; font-weight: 700; text-align: center; }
    .subtitle { text-align: center; font-size: 17px; margin-bottom: 25px; }
    .chat-user { background-color: #f0f2f6; padding: 12px; border-radius: 12px; margin: 8px 0; }
    .chat-bot { background-color: #e8f4ff; padding: 12px; border-radius: 12px; margin: 8px 0; }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="main-title">🤖 HR Assistant</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Your AI-powered Human Resources Assistant</div>',
    unsafe_allow_html=True,
)

if "messages" not in st.session_state:
    st.session_state.messages = []

with st.sidebar:
    st.header("HR Assistant")
    st.write("I can help you with:")
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

    st.session_state.messages.append(
        {"role": "assistant", "content": bot_response}
    )
    st.rerun()

st.divider()
st.caption(
    "AI HR Assistant • Please verify important employment decisions "
    "with your HR department."
)
