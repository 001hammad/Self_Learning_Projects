import streamlit as st
import google.generativeai as genai
import os
from dotenv import load_dotenv
import time

#  Environment Variables Load Karna
load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

#  API Key Check Karna
if not api_key:
    st.error("❌ Error: GEMINI_API_KEY not found in .env file!")
    st.stop()

#  Gemini API Configure Karna
genai.configure(api_key=api_key)

#  Streamlit Page Config (Sabse Pehle)
st.set_page_config(page_title="Gemini Chatbot", layout="wide")

#  Custom CSS Styling (Better UI)
st.markdown("""
    <style>
        /* Overall Page Styling */
        .main {
            background: linear-gradient(to right, #E3F0AF, #D4E157);
            padding: 20px;
        }

        /* Chat Container */
        .chat-container {
            background-color: white;
            padding: 20px;
            border-radius: 15px;
            box-shadow: 2px 2px 20px rgba(0, 0, 0, 0.1);
        }

        /* User & Bot Messages */
        .user-message {
            background-color: #E3F0AF;
            color: black;
            padding: 12px;
            border-radius: 15px;
            margin-bottom: 10px;
            border-left: 4px solid #A8C66C;
        }
        .bot-message {
            background-color: #F1F8E9;
            color: black;
            padding: 12px;
            border-radius: 15px;
            margin-bottom: 10px;
            border-left: 4px solid #81C784;
        }

        /* Text Input Styling */
        .stTextInput>div>div>input {
            background-color: white;
            color: black;
            border: 2px solid #A8C66C;
            border-radius: 10px;
            padding: 10px;
        }

        /* Button Styling */
        .stButton>button {
            background-color: #A8C66C;
            color: black;
            border-radius: 8px;
            padding: 10px;
            font-size: 16px;
            font-weight: bold;
            border: none;
            transition: 0.3s ease-in-out;
        }
        .stButton>button:hover {
            background-color: #81C784;
            transform: scale(1.05);
        }
    </style>
""", unsafe_allow_html=True)



#  UI Setup
st.title("🤖 Hammad’s AI | Smart Conversations Start Here")

#  Session State to Store Messages
if "messages" not in st.session_state:
    st.session_state.messages = []

#  Gemini Response Function
def get_response(prompt):
    try:
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content(prompt)
        time.sleep(2)
        return response.text
    except Exception as e:
        return f"❌ Error: {str(e)}"

# 🔥 Function to Handle Enter Key Press
def handle_input():
    user_input = st.session_state.user_message
    if user_input:
        # User Message Store Karna
        st.session_state.messages.append({"role": "user", "content": user_input})
        # ✅ Thinking Indicator Show Karna
    with st.empty():
        for i in range(3):
            st.write("🤖 Thinking" + "." +"." * i)  # "Thinking." → "Thinking.." → "Thinking..."
            time.sleep(0.5)  # Har dot ke beech delay

        # AI Response Fetch Karna
        response = get_response(user_input)

        # AI Response Store Karna
        st.session_state.messages.append({"role": "bot", "content": response})

        # Input Box Clear Karna
        st.session_state.user_message = ""

#  User Input Field (Jab Enter Press Karega, Message Send Ho Jayega)
st.text_input("💬 Write something:", key="user_message", on_change=handle_input)

if st.button("🔄 Clear Chat"):
    st.session_state.messages = []


for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"<div class='user-message'>🧑‍💻 {msg['content']}</div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div class='bot-message'>🤖 {msg['content']}</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
