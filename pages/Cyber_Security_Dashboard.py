# Author: Djani Colakovic
# Student ID: M01059474
# Module: CST1510 - Programming for Data Communication and Networks
# Description:
# This Streamlit dashboard displays cybersecurity incident data, including
# severity levels, incident types, and overall trends. It provides users with
# clear visual insights into security-related activity.

import streamlit as st
import pandas as pd
import altair as alt

# Make sure the user is properly signed in before they are allowed to view this dashboard 
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("You must be signed in to view this page.")
    st.stop()

# Have a clear title for the dashboard so users know which section they're in
st.title("📊Cyber Security Dashboard")
st.subheader("""This dashboard presents a secure and interactive view of recorder cyber security incidents.""")
st.subheader(""" It allows key statistics, allows filtering by type, and provides clear visualtion of severity & timelines""")

# Load the Cyber Security data from the CSV file stored inside the DATA Folder 
# Verify whether that filename below matches the one saved from earlier 
df = pd.read_csv("DATA/cybersecurity_incidents.csv", parse_dates=["date"])

# Permit the user to open and view the full dataset if they want to check it out. 
with st.expander("Show incident table"):
    st.dataframe(df)

# Brief summary to offer the user an overview of the Cyber Incidents 
st.subheader("Summary of Recorded Cyber Incidents")

total_incidents = len(df)
most_common_type = df["type"].mode()[0]
high_severity = len(df[df["severity"] == "High"])

st.write(f"• Total number of incidents: **{total_incidents}**")
st.write(f"• Most frequent type of incident: **{most_common_type}**")
st.write(f"• Number of high-severity incidents: **{high_severity}**")

# Let the user filter incidents by type to make it easier to navigate through the dataset 
st.subheader("Filter Incidents by Type")

incident_types = sorted(df["type"].unique())
selected_type = st.selectbox("Select an incident type:", ["All"] + incident_types)

if selected_type == "All":
    filtered_df = df
else:
    filtered_df = df[df["type"] == selected_type]

# Bar chart that previews how many incidents occurred for each type
# This helps highlight which threats happen most frequently. 
st.subheader("Incidents by Type")
st.write("""This bar chart shows the distribution of incidents by their type and the count of records.""")

type_chart = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x="type:N",
        y="count():Q",
        color="type:N",
        tooltip=["type", "count()"]
    )
)

st.altair_chart(type_chart, use_container_width=True)

# This is a decomposed breakdown of incident severity so users are able to see how serious the issues are as a whole 
st.subheader("Severity Breakdown")
st.write("""This pie chart illustrates the proportion of incidents by their severity level.""")

severity_chart = (
    alt.Chart(df)
    .mark_arc()
    .encode(
        theta="count():Q",
        color="severity:N",
        tooltip=["severity", "count()"]
    )
)

st.altair_chart(severity_chart, use_container_width=True)

# Make sure the user is authenticated before loading any of the dashboard content. 
st.subheader("Incident Timeline")
st.write("""This line chart displays the timeline of incidents over time, allowing for trend analysis.""")

timeline_chart = (
    alt.Chart(filtered_df)
    .mark_line(point=True)
    .encode(
        x="date:T",
        y="count():Q",
        tooltip=["date", "type", "severity", "location"]
    )
)

st.altair_chart(timeline_chart, use_container_width=True)
