import streamlit as st
import random

# Define the question bank
questions = [
    {"question": "What is the capital of France?", "options": ["London", "Paris", "Berlin", "Madrid"], "answer": "Paris"},
    {"question": "What is 5 + 7?", "options": ["10", "12", "15", "9"], "answer": "12"},
    {"question": "Who developed the theory of relativity?", "options": ["Isaac Newton", "Albert Einstein", "Galileo Galilei", "Nikola Tesla"], "answer": "Albert Einstein"},
    {"question": "What is the chemical symbol for water?", "options": ["O2", "H2O", "CO2", "H2"], "answer": "H2O"},
    {"question": "What is the square root of 64?", "options": ["6", "8", "10", "12"], "answer": "8"},
    {"question": "Who painted the Mona Lisa?", "options": ["Vincent van Gogh", "Pablo Picasso", "Leonardo da Vinci", "Michelangelo"], "answer": "Leonardo da Vinci"},
    {"question": "Which planet is known as the Red Planet?", "options": ["Venus", "Saturn", "Mars", "Jupiter"], "answer": "Mars"},
]

# Select 5 random questions
if "selected_questions" not in st.session_state:
    st.session_state.selected_questions = random.sample(questions, 5)
if "current_question" not in st.session_state:
    st.session_state.current_question = 0
if "score" not in st.session_state:
    st.session_state.score = 0
if "user_answer" not in st.session_state:
    st.session_state.user_answer = None
if "submitted" not in st.session_state:
    st.session_state.submitted = False

st.title("🧠 Quiz Game 🎯")

# Get the current question
if st.session_state.current_question < len(st.session_state.selected_questions):
    q = st.session_state.selected_questions[st.session_state.current_question]
    
    # Display the question
    st.subheader(f"Question {st.session_state.current_question + 1}: {q['question']}")

    # User selects an answer (without causing rerun)
    st.session_state.user_answer = st.radio("Choose an answer:", q["options"], index=None, key=f"q{st.session_state.current_question}")

    # Submit button logic
    if st.button("Submit"):
        if st.session_state.user_answer is None:
            st.warning("Please select an answer before submitting.")
        else:
            st.session_state.submitted = True

    # Show result only after submission
    if st.session_state.submitted:
        if st.session_state.user_answer == q["answer"]:
            st.success("✅ Correct! 🎉")
            st.session_state.score += 1
        else:
            st.error(f"❌ Incorrect! The correct answer is {q['answer']}.")

        # Next Question Button
        if st.button("Next Question"):
            st.session_state.current_question += 1
            st.session_state.submitted = False  # Reset submission state
            st.session_state.user_answer = None
            st.rerun()  # ✅ Fixed rerun method

else:
    st.subheader(f"🎯 Final Score: {st.session_state.score}/5")
    
    # Play Again Button
    if st.button("Play Again"):
        st.session_state.selected_questions = random.sample(questions, 5)
        st.session_state.current_question = 0
        st.session_state.score = 0
        st.session_state.user_answer = None
        st.session_state.submitted = False
        st.rerun()  # ✅ Fixed rerun method
