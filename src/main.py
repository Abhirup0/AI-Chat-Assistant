import os
import streamlit as st
from src.config import Config
from src.gemini_handler import GeminiHandler

# Load and validate configuration
Config.validate_config()

# Initialize Gemini handler
gemini_handler = GeminiHandler()

# Page configuration
st.set_page_config(
    page_title="AI Chat Assistant",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Add custom CSS
css_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static", "styles.css")
with open(css_path) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Create three columns for layout
left_col, main_col, right_col = st.columns([1, 2, 1])

with main_col:
    # Streamlit UI setup
    st.title("🤖 AI Chat Assistant")
    st.markdown("""
        Welcome to the AI Chat Assistant! This chatbot uses Google's Gemini model to provide:
        - 💡 Intelligent responses
        - 🔍 Information lookup
        - 🛠️ Problem-solving assistance
        - 💬 Natural conversation
    """)

    # Initialize chat history
    if "messages" not in st.session_state:
        st.session_state.messages = []

    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Chat input
    if prompt := st.chat_input("What would you like to know?"):
        # Validate input
        if not gemini_handler.validate_input(prompt):
            st.error(f"Please enter a valid input (maximum {Config.MAX_INPUT_LENGTH} characters)")
        else:
            # Add user message to chat history
            st.session_state.messages.append({"role": "user", "content": prompt})
            with st.chat_message("user"):
                st.markdown(prompt)

            # Generate AI response
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    try:
                        response = gemini_handler.generate_response(
                            prompt, 
                            st.session_state.messages[:-1]  # Exclude the current message
                        )
                        st.markdown(response)
                        st.session_state.messages.append({"role": "assistant", "content": response})
                        
                        # Limit chat history length
                        if len(st.session_state.messages) > Config.MAX_HISTORY_LENGTH * 2:  # *2 because each exchange has 2 messages
                            st.session_state.messages = st.session_state.messages[-Config.MAX_HISTORY_LENGTH * 2:]
                    except Exception as e:
                        st.error(f"An error occurred: {str(e)}")

# Sidebar
with st.sidebar:
    st.markdown("### Chat Controls")
    if st.button("🗑️ Clear Chat", use_container_width=True):
        st.session_state.messages = []
        st.rerun()
    
    st.markdown("---")
    st.markdown("### About")
    st.markdown("""
        This AI Chat Assistant is powered by Google's Gemini model, 
        providing intelligent responses and assistance across a wide 
        range of topics.
        📝 Version: 1.0.0
    """) 