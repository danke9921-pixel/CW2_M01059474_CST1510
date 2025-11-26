import streamlit as st
from app.data.db import connect_database
from app.data.incidents import get_all_incidents
from app.data.datasets import get_all_datasets
from app.data.tickets import get_all_tickets

# Ensures only signed-in users can reach this page.
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("You must be signed in to view this page.")
    if st.button("Return to Login"):
        st.switch_page("Home.py")
    st.stop()

st.title(" Dashboard")
st.success(f"Welcome, {st.session_state.username}!")

# Connect to the database so the tables can be loaded.
conn = connect_database()

# Display cyber incident records.
st.header("Cyber Incidents")
st.dataframe(get_all_incidents(conn), use_container_width=True)

# Display dataset information.
st.header("Datasets")
st.dataframe(get_all_datasets(conn), use_container_width=True)

# Display IT ticket information.
st.header("IT Tickets")
st.dataframe(get_all_tickets(conn), use_container_width=True)

st.divider()

# Allows the user to sign out.
if st.button("Log Out"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.switch_page("Home.py")
