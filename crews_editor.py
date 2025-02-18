import streamlit as st
from common import *

# Ensure API keys are set
if not all(
    key in st.session_state
    for key in ["Exa Key", "Serper Key", "OpenAI Key", "Gemini Key", "Anthropic Key"]
):
    st.error("Please go back to the first page and enter API keys.")
    st.stop()


# Initialize session state with defaults from `common.py`
if "agent_definitions" not in st.session_state:
    st.session_state.agent_definitions = {
        "data_analyst_agent_role": data_analyst_agent_role,
        "data_analyst_agent_goal": data_analyst_agent_goal,
        "data_analyst_agent_backstory": data_analyst_agent_backstory,
        "content_specialist_agent_role": content_specialist_agent_role,
        "content_specialist_agent_goal": content_specialist_agent_goal,
        "content_specialist_agent_backstory": content_specialist_agent_backstory,
        "market_research_task_description": market_research_task_description,
        "market_research_task_expected_output": market_research_task_expected_output,
        "content_creation_task_description": content_creation_task_description,
        "content_creation_task_expected_output": content_creation_task_expected_output,
    }

# Editable agent and task definitions
st.subheader("Data Analyst Agent")
st.session_state.agent_definitions["data_analyst_agent_role"] = st.text_area(
    "Role", st.session_state.agent_definitions["data_analyst_agent_role"], height=150
)
st.session_state.agent_definitions["data_analyst_agent_goal"] = st.text_area(
    "Goal", st.session_state.agent_definitions["data_analyst_agent_goal"], height=100
)
st.session_state.agent_definitions["data_analyst_agent_backstory"] = st.text_area(
    "Backstory", st.session_state.agent_definitions["data_analyst_agent_backstory"], height=100
)

st.subheader("Content Specialist Agent")
st.session_state.agent_definitions["content_specialist_agent_role"] = st.text_area(
    "Role", st.session_state.agent_definitions["content_specialist_agent_role"], height=150
)
st.session_state.agent_definitions["content_specialist_agent_goal"] = st.text_area(
    "Goal", st.session_state.agent_definitions["content_specialist_agent_goal"], height=100
)
st.session_state.agent_definitions["content_specialist_agent_backstory"] = st.text_area(
    "Backstory", st.session_state.agent_definitions["content_specialist_agent_backstory"], height=100
)

st.subheader("Tasks")
st.session_state.agent_definitions["market_research_task_description"] = st.text_area(
    "Market Research Task Description",
    st.session_state.agent_definitions["market_research_task_description"],
    height=150,
)
st.session_state.agent_definitions["market_research_task_expected_output"] = st.text_area(
    "Market Research Task Expected Output",
    st.session_state.agent_definitions["market_research_task_expected_output"],
    height=100,
)
st.session_state.agent_definitions["content_creation_task_description"] = st.text_area(
    "Content Creation Task Description",
    st.session_state.agent_definitions["content_creation_task_description"],
    height=150,
)
st.session_state.agent_definitions["content_creation_task_expected_output"] = st.text_area(
    "Content Creation Task Expected Output",
    st.session_state.agent_definitions["content_creation_task_expected_output"],
    height=100,
)
if st.button("Save Crew"):
    st.success("Crew saved! Navigate to the next step using the sidebar.")
