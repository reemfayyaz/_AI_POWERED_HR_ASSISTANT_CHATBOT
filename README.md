# AI-Powered HR Assistant Chatbot

An AI-powered Human Resources assistant built with Streamlit. The chatbot answers common HR questions about leave, attendance, salary, payroll, benefits, recruitment, interviews, onboarding, resignation, and HR policies.

## Features

- Interactive Streamlit chat interface
- Intent classification using a trained machine-learning model
- Predefined responses for common HR questions
- Confidence threshold for questions the chatbot does not understand
- Clear chat history button
- Saved trained model loaded from `hr_chatbot.pkl`

## Project Files

| File | Description |
| --- | --- |
| `app.py` | Streamlit application | 
| `hr_chatbot.pkl` | Trained chatbot model, responses, and confidence threshold |
| `🤖_AI_Powered_HR_Assistant_Chatbot.ipynb` | Notebook used to develop the chatbot |
| `requirements.txt` | Python dependencies |

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/reemfayyaz/_AI_POWERED_HR_ASSISTANT_CHATBOT.git
   cd _AI_POWERED_HR_ASSISTANT_CHATBOT
   ```

2. Create and activate a virtual environment (recommended):

   **Windows:**

   ```bash
   python -m venv .venv
   .venv\Scripts\activate
   ```

   **macOS/Linux:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Run the Application

Make sure `hr_chatbot.pkl` is in the same directory as `app.py`, then run:

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal, usually `http://localhost:8501`.

## Usage

Enter an HR-related question in the chat box. The assistant can help with topics including:

- Leave and attendance
- Salary and payroll
- Work from home
- Employee benefits
- Recruitment and interviews
- Onboarding
- Resignation
- HR policies

If the chatbot is not confident about the question, it will ask you to rephrase it or ask about a supported HR topic.

## Disclaimer

This project is intended for educational and demonstration purposes. Chatbot responses should not replace advice from your organization's HR department or qualified professionals. Verify important employment decisions with your HR team.
