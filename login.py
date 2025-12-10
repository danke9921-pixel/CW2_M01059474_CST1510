# Author : Djani Colakovic
# Student ID: M01059474
# Module: CST1510 - Programming for Data Communication and Networks
# Description:
# This file handles the user login and registration interface. 
# It collects user credentials, sends them to the authentication manager for verfication
# and directs the user to the appropriate dashboard once authenticated.
import streamlit as st
import sys
from pathlib import Path
import sqlite3
import bcrypt

# Add project root to path so 'app' can be imported
sys.path.insert(0, str(Path(__file__).parent.resolve()))

# Import authentication functions
from app.multi_domain_platform.services.auth_manager import (
    password_requirements,
    register_user
)

#  Direct absolute path to your database
DB_PATH = r"DATA/intelligence_platforms.db"


def login_user(username: str, password: str) -> bool:
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute(
        "SELECT password FROM users WHERE username = ?",
        (username.strip(),)
    )
    row = cursor.fetchone()
    conn.close()

    if not row:
        return False

    stored_pw = row[0]

    # Normalise stored hash
    if isinstance(stored_pw, memoryview):
        stored_pw = stored_pw.tobytes()
    if isinstance(stored_pw, str):
        stored_pw = stored_pw.encode("utf-8")

    return bcrypt.checkpw(password.strip().encode("utf-8"), stored_pw)


def launch_streamlit():
    st.set_page_config(page_title="Login Page", layout="centered")

    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
    if "username" not in st.session_state:
        st.session_state.username = ""

    st.title("Welcome to Multi-Domain Intelligence Platform")
    st.image(
        "https://tse4.mm.bing.net/th/id/OIP.QugjI0FFS56vzij1JV8pVgHaDe?w=349&h=150&c=7&r=0&o=7&dpr=1.5&pid=1.7&rm=3",
        width=600
    )

    tab_login, tab_register = st.tabs(["Login", "Register"])

    # LOGIN TAB
    with tab_login:
        st.subheader("Sign In")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        if st.button("Sign In"):
            if login_user(username.strip(), password.strip()):
                st.session_state.logged_in = True
                st.session_state.username = username.strip()
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

        role = st.radio(
            "Select a Role",
            ["User", "Admin", "Guest"],
            index=1
        )

        if st.button("Register"):
            if not new_user or not new_pass:
                st.warning("Please complete all fields before continuing.")
            elif new_pass != confirm_pass:
                st.error("The passwords do not match. Please try again.")
            elif not password_requirements(new_pass):
                st.error("Password does not meet security requirements.")
                st.caption(
                    "Password must be at least 8 characters, include uppercase, "
                    "lowercase, a number, and a special character."
                )
            else:
                if register_user(new_user.strip(), new_pass.strip(), "user"):
                    st.success("Your account has been created. You may now sign in.")
                else:
                    st.error("That username is already in use.")


if __name__ == "__main__":
    launch_streamlit()