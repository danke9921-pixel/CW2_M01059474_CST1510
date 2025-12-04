# test_secrets.py

# Double check to confirm Streamlit secrets are loading properly

import streamlit as st

st.title("Secrets Test")
try:
    key = st.secrets["OPENAI_API_KEY"]
    st.success("API key loaded successfully.")
    st.write(f"Key starts with: {key[:10]} ...")
except Exception as e:
    st.error(f"Problem loading secrets: {e}")
    st.info("Check .streamlit/secrets.toml and ensure the key is correct.")