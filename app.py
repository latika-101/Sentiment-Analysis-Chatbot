import streamlit as st
from chatbot import get_response

# Set Streamlit page config
st.set_page_config(page_title="Latika's Sentiment Analysis Advanced Chatbot", page_icon="🤖", layout="centered")

# Custom CSS for styling
st.markdown("""
    <style>
    body {
        background-color: #f0f2f6;
    }
    .title {
        text-align: center;
        color: #4B0082;
        font-size: 36px;
        font-weight: bold;
    }
    .bot-container {
        background-color: #ffffff;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 0px 4px 8px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }
    .input-container {
        background-color: #f9f9f9;
        padding: 15px;
        border-radius: 10px;
        box-shadow: 0px 2px 4px rgba(0,0,0,0.1);
    }
    .bot-text {
        color: #333;
        font-size: 18px;
    }
    .user-input {
        padding: 10px;
        font-size: 16px;
        margin-bottom: 10px;
        width: 100%;
    }
    .bot-response {
        font-size: 18px;
        color: #008000;
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Streamlit app title with custom styling
st.markdown('<h1 class="title">Latika\'s Sentiment Analysis Advanced Chatbot 🤖</h1>', unsafe_allow_html=True)
st.write("Interact with the chatbot below. The chatbot supports contextual conversations and provides various responses.")


# Input text from the user
user_input = st.text_input("You: ", "", key="user_input")
st.markdown('</div>', unsafe_allow_html=True)

# Get chatbot response and display
if user_input:
    response = get_response(user_input)
    st.markdown(f'<p class="bot-response"><strong>Bot:</strong> {response}</p>', unsafe_allow_html=True)

# End chatbot container
st.markdown('</div>', unsafe_allow_html=True)
