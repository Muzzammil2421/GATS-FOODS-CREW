import streamlit as st

# Set page configuration
st.set_page_config(page_title="GatFoods", layout="wide")

# Define navigation structure
pages = {
    "API Keys": [
        st.Page("Home.py", title="Enter API Keys"),
    ],
    "Crew Editor": [
        st.Page("crews_editor.py", title="Edit Agents and Task"),
    ],
    "Crew Runner": [
        st.Page("run_crews.py", title="Run Crew"),
    ],
}

# Define navigation
pg = st.navigation(pages)
pg.run()

