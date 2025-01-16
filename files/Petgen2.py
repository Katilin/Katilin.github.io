import streamlit as st
import time

# Configure the page to look like a terminal
st.set_page_config(page_title="Pet Name Generator Terminal")

# Custom CSS for terminal look
st.markdown("""
    <style>
        .stTextInput input {
            background-color: black;
            color: #00ff00;
            font-family: monospace;
            border: none;
            padding: 10px;
        }
        .stMarkdown {
            color: #00ff00;
            font-family: monospace;
        }
        .stButton button {
            background-color: black;
            color: #00ff00;
            font-family: monospace;
            border: 1px solid #00ff00;
        }
        section.main {
            background-color: black;
            padding: 20px;
        }
        .stMarkdown p {
            color: #00ff00;
            font-family: monospace;
        }
        .status {
            color: #00ff00;
            font-family: monospace;
        }
    </style>
""", unsafe_allow_html=True)

# Initialize session state for managing conversation steps
if 'step' not in st.session_state:
    st.session_state.step = 0
    st.session_state.messages = ["Welcome to the pet name generator"]
    st.session_state.inputs = {}
    st.session_state.current_input = ""

# Questions list
questions = [
    "What is your favorite Movie Character?",
    "What is your favorite activity?",
    "What is your favorite food?",
    "Is your Pet male or female? (m/f):"
]

# Display all previous messages
for msg in st.session_state.messages:
    st.markdown(f"```{msg}```")

# Handle current step
if st.session_state.step < len(questions):
    # Show current question
    current_question = questions[st.session_state.step]
    
    # Create a placeholder for the input prompt
    prompt = st.empty()
    
    # Get user input
    user_input = st.text_input(
        "Input",
        key=f"input_{st.session_state.step}",
        label_visibility="collapsed"
    )

    # Process input when user hits enter
    if user_input:
        # Handle gender validation
        if st.session_state.step == 3:
            if user_input.lower() not in ['m', 'f']:
                st.session_state.messages.append(f"> {user_input}")
                st.session_state.messages.append("Invalid input. Please enter 'm' for male or 'f' for female.")
                st.experimental_rerun()
            
        # Store input and advance to next step
        st.session_state.inputs[st.session_state.step] = user_input
        st.session_state.messages.append(f"> {user_input}")
        
        if st.session_state.step < len(questions) - 1:
            st.session_state.step += 1
        else:
            # Generate pet name
            character = st.session_state.inputs[0]
            activity = st.session_state.inputs[1]
            food = st.session_state.inputs[2]
            gender = st.session_state.inputs[3].lower()
            
            title = "Mr." if gender == 'm' else "Miss"
            pet_name = f"{title} {character} {activity} {food}"
            
            st.session_state.messages.append(f"\nYour pet name could be: {pet_name}")
            st.session_state.messages.append("\nPress 'Reset' to start over...")
            st.session_state.step = len(questions)  # Mark as complete
        
        st.experimental_rerun()

# Show reset button when done
if st.session_state.step == len(questions):
    if st.button("Reset"):
        st.session_state.step = 0
        st.session_state.messages = ["Welcome to the pet name generator"]
        st.session_state.inputs = {}
        st.experimental_rerun()
