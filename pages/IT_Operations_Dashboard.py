# Author: Djani Colakovic
# Student ID: M01059474
# Module: CST1510 - Programming for Data Communication and Networks
# Description:
# This dashboard visualises IT ticket information, including ticket status,
# priority levels, and resolution times. It provides an overview of operational
# workload and performance.

import streamlit as st
import pandas as pd
import altair as alt

# Make sure the user is properly signed in before they are allowed to view this dashboard 
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("You must be signed in to view this page.")
    st.stop()

# Have a clear title for the dashboard so users know which section they're in
st.title("📊IT Operations Dashboard")
st.subheader("""This dashboard provides a secure and interactive overview of IT operations across multiple cities.""")
st.subheader("""Only authenticated users can access this data.""")
st.subheader("""It emphasises tasks completed, active issues, supported by clear charts and timelines.""")
# Load the IT Operations data from the CSV file stored inside the DATA Folder 
# Verify whether that filename below matches the one saved from earlier 
df = pd.read_csv("DATA/IT_operations.csv", parse_dates=["date"])

# Permit the user to open and view the full dataset if they want to check it out. 
with st.expander("Show operations table"):
    st.dataframe(df)

# Brief summary to offer the user an overview of the IT Operations 
st.subheader("Summary of Recorded IT Operations")

total_projects = len(df)
most_common_city = df["city"].mode()[0]
avg_performance = round(df["performance_score"].mean(), 2)

st.write(f"• Total number of projects: **{total_projects}**")
st.write(f"• City with most recorded projects: **{most_common_city}**")
st.write(f"• Average performance score: **{avg_performance}**")

# Let the user filter operations by city to make it easier to navigate through the dataset 
st.subheader("Filter Operations by City")

cities = sorted(df["city"].unique())
selected_city = st.selectbox("Select a city:", ["All"] + cities)

if selected_city == "All":
    filtered_df = df
else:
    filtered_df = df[df["city"] == selected_city]

# Bar chart that previews how many tasks were completed for each project 
# This helps highlight which projects have achieved the most progress 
st.subheader("Tasks Completed per Project")
st.write("""This bar chart shows the number of tasks completed for each project across different cities.""")

tasks_chart = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x="project:N",
        y="tasks_completed:Q",
        color="city:N",
        tooltip=["city", "project", "tasks_completed"]
    )
)

st.altair_chart(tasks_chart, use_container_width=True)

# This is a decomposed breakdown of active issues so users are able to see where problems are concentrated 
st.subheader("Active Issues Breakdown")
st.write("""This pie chart illustrates the distribution of active issues across different cities.""")

issues_chart = (
    alt.Chart(df)
    .mark_arc()
    .encode(
        theta="active_issues:Q",
        color="city:N",
        tooltip=["city", "active_issues"]
    )
)

st.altair_chart(issues_chart, use_container_width=True)

# Make sure the user is authenticated before loading any of the dashboard content. 
st.subheader("Project Timeline")
st.write("""This timeline chart tracks the performance scores of projects over time across different cities.""")

timeline_chart = (
    alt.Chart(filtered_df)
    .mark_line(point=True)
    .encode(
        x="date:T",
        y="performance_score:Q",
        color="city:N",
        tooltip=["date", "city", "project", "performance_score"]
    )
)

st.altair_chart(timeline_chart, use_container_width=True)