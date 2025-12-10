# Author: Djani Colakovic
# Student ID: M01059474
# Module: CST1510 - PProgramming for Data Communication and Networks
# Description:
# This optional AI assistant provides analysis and commentary on IT ticket data,
# helping users understand operational patterns and workload.
import streamlit as st
from openai import OpenAI

# Define the system prompt to get the assistant
def system_prompt():
    return (
        "You are an IT Operations assistant.\n"
        "- Help with troubleshooting, servers, and networking\n"
        "- Explain concepts clearly\n"
        "- Give examples when useful\n"
        "- Keep answers short and practical"
    )

# Initialise the chat history if it doesn't exist
def init_chat():
    if "it_msgs" not in st.session_state:
        st.session_state.it_msgs = [{"role": "system", "content": system_prompt()}]

# This clears the chat history and restart which will take you back to system prompt
def render_chat():
    for msg in st.session_state.it_msgs:
        if msg["role"] != "system":
            with st.chat_message(msg["role"]):
                st.markdown(msg["content"])

def clear_chat():
    st.session_state.it_msgs = [{"role": "system", "content": system_prompt()}]
    st.rerun()

# Title and icon professional and polished
st.set_page_config(page_title="IT Operations Assistant", page_icon="💻")
st.title("IT Operations Assistant")

# This is a sidebar with a message count and includes a button to clear the chat
with st.sidebar:
    st.metric("Messages", len(st.session_state.get("it_msgs", [])) - 1)
    if st.button("Clear chat", use_container_width=True):
        clear_chat()

init_chat()
render_chat()

# Input for the user to ask about IT operations

prompt = st.chat_input("Ask about IT operations …")
if prompt:
    # This previews the user's message in the chatbot
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.it_msgs.append({"role": "user", "content": prompt})

    # Link to OpenAI with your stored API key
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    stream = client.chat.completions.create(
        model="gpt-4o",
        messages=st.session_state.it_msgs,
        stream=True
    )

    # Preview the assistant's streamed response in real time
    with st.chat_message("assistant"):
        box = st.empty()
        full = ""
        for chunk in stream:
            delta = chunk.choices[0].delta
            if delta.content:
                full += delta.content
                box.markdown(full + " ▌")
        box.markdown(full)

    # This saves the assistant's whole response back into the chatbot history
    st.session_state.it_msgs.append({"role": "assistant", "content": full})