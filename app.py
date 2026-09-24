# ============================================
# CREATE STREAMLIT APP
# ============================================

app_code = r'''
import streamlit as st
import joblib
import os

# ============================================
# PAGE CONFIGURATION
# ============================================

st.set_page_config(
    page_title="HR Assistant",
    page_icon="🤖",
    layout="centered"
)

# ============================================ \
# LOAD MODEL
# ============================================ \

MODEL_PATH = "hr_chatbot.pkl"

if not os.path.exists(MODEL_PATH):

    st.error(
        "HR chatbot model not found. "
        "Please keep hr_chatbot.pkl in the same folder as app.py."
    )

    st.stop()

chatbot = joblib.load(MODEL_PATH)

model = chatbot["model"]
responses = chatbot["responses"]
threshold = chatbot["threshold"]


# ============================================ \
# CUSTOM CSS
# ============================================ \

st.markdown("""
<style>

.main-title {
    font-size: 38px;
    font-weight: 700;
    text-align: center;
}

.subtitle {
    text-align: center;
    font-size: 17px;
    margin-bottom: 25px;
}

.chat-user {
    background-color: #f0f2f6;
    padding: 12px;
    border-radius: 12px;
    margin: 8px 0;
}

.chat-bot {
    background-color: #e8f4ff;
    padding: 12px;
    border-radius: 12px;
    margin: 8px 0;
}

</style>
""", unsafe_allow_html=True)


# ============================================ \
# HEADER
# ============================================ \

st.markdown(
    '<div class="main-title">🤖 HR Assistant</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Your AI-powered Human Resources Assistant'
    '</div>',
    unsafe_allow_html=True
)


# ============================================ \
# SESSION STATE
# ============================================ \

if "messages" not in st.session_state:

    st.session_state.messages = []


# ============================================ \
# SIDEBAR
# ============================================ \

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


# ============================================ \
# DISPLAY CHAT HISTORY
# ============================================ \

for message in st.session_state.messages:

    if message["role"] == "user":

        st.markdown(
            f"""
            <div class="chat-user">
            <b>You:</b> {message["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )

    else:

        st.markdown(
            f"""
            <div class="chat-bot">
            <b>HR Assistant:</b> {message["content"]}
            </div>
            """,
            unsafe_allow_html=True
        )


# ============================================ \
# USER INPUT
# ============================================ \

user_input = st.chat_input(
    "Ask your HR question..."
)


# ============================================ \
# CHATBOT LOGIC
# ============================================ \

if user_input:

    # Store user message
    st.session_state.messages.append({
        "role": "user",
        "content": user_input
    })

    # Predict probability
    probabilities = model.predict_proba([user_input])[0]

    max_probability = probabilities.max()

    predicted_intent = model.classes_[
        probabilities.argmax()
    ]

    # Generate response
    if max_probability < threshold:

        bot_response = (
            "I'm sorry, I couldn't confidently understand your question. "
            "Please try asking about leave, attendance, salary, payroll, "
            "benefits, recruitment, onboarding, resignation, or HR policies."
        )

    else:

        bot_response = responses[predicted_intent]

    # Store bot response
    st.session_state.messages.append({
        "role": "assistant",
        "content": bot_response
    })

    st.rerun()


# ============================================ \
# FOOTER
# ============================================ \

st.divider()

st.caption(
    "AI HR Assistant • Please verify important employment decisions "
    "with your HR department."
)
'''

# Use textwrap.dedent to remove the common leading whitespace
# from the multiline string, which is causing the IndentationError.
import textwrap
app_code = textwrap.dedent(app_code)

with open("/content/app.py", "w", encoding="utf-8") as f:
    f.write(app_code)

print("app.py created successfully!")