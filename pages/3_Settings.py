import streamlit as st 

# Prevents non-singed-in users from viewing this page
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("You do not have permission to view this page.")
    st.stop()

    st.title("Settings")

# This shows who is currently signed in
st.write("Signed in as:", st.session_state.username)