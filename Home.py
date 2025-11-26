import streamlit as st
import sys
from pathlib import Path

# Add parent directory to path if needed
sys.path.insert(0, str(Path(__file__).parent))

from app.data.db import connect_database
from app.data.users import verify_user, create_user

# Set up the main page layout and appearance.
# Note: Streamlit only accepts "centered" or "wide".
st.set_page_config(page_title="Login Page", layout="centered")

# Connect the app to the database so it can access the stored tables.
conn = connect_database()

# Make sure the session values exist before they are used.
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

if "username" not in st.session_state:
    st.session_state.username = ""

st.title(" Welcome to Multi-Domain Intelligence Platform")
st.image("https://tse4.mm.bing.net/th/id/OIP.QugjI0FFS56vzij1JV8pVgHaDe?w=349&h=150&c=7&r=0&o=7&dpr=1.5&pid=1.7&rm=3", width = 600)
# Correct way to set the page icon
st.set_page_config(
    page_title="Multi-Domain Intelligence Platform",
    page_icon="👌",   # I have used an emoji 
    layout="wide",
)
# Two simple tabs one for signing in, the other for registering a new account.
tab_login, tab_register = st.tabs(["Login", "Register"])

#  LOGIN TAB 
with tab_login:
    st.subheader("Sign In")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    # When the user presses the button, check their login details.
    if st.button("Sign In"):
        if verify_user(conn, username, password):
            st.session_state.logged_in = True
            st.session_state.username = username
            st.success("You have successfully signed in.")
            st.switch_page("pages/1_Dashboard.py")
        else:
            st.error("The username or password was not recognised.")

# REGISTER TAB
with tab_register:
    st.subheader("Create a New Account")

    new_user = st.text_input("Choose a username")
    new_pass = st.text_input("Choose a password", type="password")
    confirm_pass = st.text_input("Confirm password", type="password")

    # Ensure all information is valid before creating the new account.
    if st.button("Register"):
        if not new_user or not new_pass:
            st.warning("Please complete all fields before continuing.")
        elif new_pass != confirm_pass:
            st.error("The passwords do not match. Please try again.")
        else:
            if create_user(conn, new_user, new_pass):
                st.success("Your account has been created. You may now sign in.")
            else:
                st.error("That username is already in use.")

