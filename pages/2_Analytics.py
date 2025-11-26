import streamlit as st
import pandas as pd
import altair as alt

# Make sure the user is signed in before viewing this page.
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("Please sign in to access this page.")
    st.stop()

st.title("Analytics")

# Load cyber incidents data (same file used in your dashboard)
df = pd.read_csv("DATA/cybersecurity_incidents.csv")

# Total incident count
st.subheader("Total Number of Incidents")
st.write(len(df))

# FIXED: Replaced incorrect 'st.bar_charts' with a proper Altair bar chart
st.subheader("Severity Distribution")

severity_counts = df["severity"].value_counts().reset_index()
severity_counts.columns = ["severity", "count"]

severity_chart = (
    alt.Chart(severity_counts)
    .mark_bar()
    .encode(
        x="severity:N",
        y="count:Q",
        color="severity:N",
        tooltip=["severity", "count"]
    )
)

st.altair_chart(severity_chart, use_container_width=True)
