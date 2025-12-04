import streamlit as st   #  Import Streamlit properly
import pandas as pd
import sys
from pathlib import Path

#  Add project root to path so 'app' can be imported
sys.path.insert(0, str(Path(__file__).parent.parent.resolve()))

#  Correct imports
from app.multi_domain_platform.database import connect_database
from app.multi_domain_platform.services.incidents import get_all_incidents
from app.multi_domain_platform.services.datasets import get_all_datasets
from app.multi_domain_platform.services.tickets import get_all_tickets

#  Ensures only signed-in users can reach this page.
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("You must be signed in to view this page.")
    if st.button("Return to Login"):
        st.switch_page("login.py")
    st.stop()

#  Dashboard title and welcome message
st.title("Dashboard")
st.success(f"Welcome, {st.session_state.username}!")
st.title("Here is an overview of the current cyber incidents, datasets, and IT tickets")

#  Connect to the database
conn = connect_database()

#  Display cyber incident records
st.header("Cyber Incidents")
st.dataframe(get_all_incidents(), use_container_width=True)

#  Display dataset information
st.header("Datasets")
st.dataframe(get_all_datasets(), use_container_width=True)

#  Display IT ticket information
st.header("IT Tickets")
st.dataframe(get_all_tickets(), use_container_width=True)

#  Divider for clarity
st.divider()

#  Allows the user to sign out
if st.button("Log Out"):
    st.session_state.logged_in = False
    st.session_state.username = ""
    st.switch_page("login.py")