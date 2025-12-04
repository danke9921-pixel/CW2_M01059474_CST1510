import streamlit as st
from openai import OpenAI
import sys
from pathlib import Path

# I Added a project root to path so 'app' can be imported
sys.path.insert(0, str(Path(__file__).parent.parent.resolve()))

# I Corrected imports
from app.multi_domain_platform.database import connect_database
from app.multi_domain_platform.services.incidents import get_all_incidents

# Construct prompt for AI
def build_prompt(incident):
    return (
        f"Analyse this cybersecurity incident:\n\n"
        f"Incident ID: {incident['incident_id']}\n"
        f"Timestamp: {incident['timestamp']}\n"
        f"Category: {incident['category']}\n"
        f"Severity: {incident['severity']}\n"
        f"Status: {incident['status']}\n"
        f"Description: {incident['description']}\n\n"
        "Provide:\n"
        "1. Root cause analysis\n"
        "2. Immediate actions\n"
        "3. Prevention steps\n"
        "4. Risk assessment"
    )

# Page setup
st.set_page_config(page_title="AI Incident Analyzer", page_icon="🔍")
st.title("AI Incident Analyzer")

# Connect to database and fetch incidents
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
conn = connect_database()
incidents = get_all_incidents()

# If no incidents, warn the user
if incidents.empty:
    st.warning("No incidents found.")
else:
    options = [
        f"{row['incident_id']}: {row['category']} - {row['severity']}"
        for _, row in incidents.iterrows()
    ]
    idx = st.selectbox("Select incident:", range(len(incidents)), format_func=lambda i: options[i])
    incident = incidents.iloc[idx]

    # Preview incident details
    st.subheader("Incident Details")
    st.write(f"**Incident ID:** {incident['incident_id']}")
    st.write(f"**Timestamp:** {incident['timestamp']}")
    st.write(f"**Category:** {incident['category']}")
    st.write(f"**Severity:** {incident['severity']}")
    st.write(f"**Status:** {incident['status']}")
    st.write(f"**Description:** {incident['description']}")

    # Analyse with AI
    if st.button("Analyse with AI"):
        prompt = build_prompt(incident)
        with st.spinner("Thinking …"):
            stream = client.chat.completions.create(
                model="gpt-4o",
                messages=[
                    {"role": "system", "content": "You are a cybersecurity expert."},
                    {"role": "user", "content": prompt}
                ],
                stream=True
            )

        # Show AI's answer
        st.subheader("AI Analysis")
        box = st.empty()
        full = ""
        for chunk in stream:
            delta = chunk.choices[0].delta
            if delta.content:
                full += delta.content
                box.markdown(full + " ▌")
        box.markdown(full)

# Close database connection
try:
    conn.close()
except Exception:
    pass