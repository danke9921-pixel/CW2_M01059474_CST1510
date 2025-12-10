# Author: Djani Colakovic
# Student ID: M01059474
# Module: CST1510 - Programming for Data Communication and Networks
# Description:
# This dashboard presents dataset summaries, metadata, and category breakdowns.
# It helps users understand the structure and composition of each dataset in
# the system.


import streamlit as st
import pandas as pd
import altair as alt

# Make sure the user is properly signed in before they are allowed to view this dashboard 
if "logged_in" not in st.session_state or not st.session_state.logged_in:
    st.error("You must be signed in to view this page.")
    st.stop()

# Clear title so the user knows exactly which dashboard they are viewing
st.title("📊 Data Science Dashboard")
st.subheader("""This dashboard gives a clear, friendly view of Data Science project performance across various cities.""")
st.subheader("""It helps users explore a performance, tasks, and issues across different cities, with easy to read charts and timelines""")
# Load the Data Science project dataset stored inside the DATA folder
# Make sure this filename matches the one you created earlier
df = pd.read_csv("DATA/data_science.csv", parse_dates=["date"])

# Allow the user to view the full dataset if they wish to inspect it
with st.expander("Show project data"):
    st.dataframe(df)

# Simple summary so the user can quickly understand the overall picture
st.subheader("Project Summary")

total_projects = len(df)
average_score = round(df["performance_score"].mean(), 1)
total_tasks = df["tasks_completed"].sum()

st.write(f"• Number of projects recorded: **{total_projects}**")
st.write(f"• Average performance score: **{average_score}**")
st.write(f"• Total tasks completed across all cities: **{total_tasks}**")

# Let the user filter the dataset by city to make it easier to navigate
st.subheader("Filter Projects by City")

cities = sorted(df["city"].unique())
chosen_city = st.selectbox("Select a city:", ["All"] + cities)

# Use if/elif for filtering logic to match the Cyber Security dashboard style
if chosen_city == "All":
    filtered_df = df
elif chosen_city in cities:
    filtered_df = df[df["city"] == chosen_city]
else:
    st.warning("City not recognised, showing all data instead.")
    filtered_df = df

# Bar chart showing how many tasks have been completed in each city
st.subheader("Tasks Completed by City")
st.write("""This bar chart shows the total number of tasks completed in each city.""")

tasks_chart = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x="city:N",
        y="tasks_completed:Q",
        color="city:N",
        tooltip=["city", "tasks_completed"]
    )
)

st.altair_chart(tasks_chart, use_container_width=True)

# Line chart showing how project performance has changed over time 
st.subheader("Performance Timeline")
st.write("""Performance trend of recent activities.""")

performance_chart = (
    alt.Chart(filtered_df)
    .mark_line(point=True)
    .encode(
        x="date:T",
        y="performance_score:Q",
        tooltip=["date", "project", "performance_score"]
    )
)

st.altair_chart(performance_chart, use_container_width=True)

# Pie chart showing the number of active issues for each city
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
# End of Data Science Dashboard code 
