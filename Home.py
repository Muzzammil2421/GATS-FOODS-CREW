import streamlit as st
import re

# Input fields for API keys
st.subheader("API Keys")

exa_api_key = st.text_input("Exa API Key:", type="password")
serper_api_key = st.text_input("Serper API Key:", type="password")
openai_key = st.text_input("OpenAI API Key:", type="password")
# gemini_key = st.text_input("Gemini API Key:", type="password")
# anthropic_key = st.text_input("Anthropic/Claude API Key:", type="password")

# Validation patterns
validation_patterns = {
    "Exa Key": {"value": exa_api_key, "pattern": r"^[0-9a-fA-F\-]{36}$"},
    "Serper Key": {"value": serper_api_key, "pattern": r"^[0-9a-fA-F]{40}$"},
    "OpenAI Key": {"value": openai_key, "pattern": r"^sk-proj-[a-zA-Z0-9_\-]{20,}$"},
    # "Gemini Key": {"value": gemini_key, "pattern": r"^[a-zA-Z0-9_\-]{10,}$"},
    # "Anthropic Key": {"value": anthropic_key, "pattern": r"^sk-ant-[a-zA-Z0-9_\-]{20,}$"},
}

# Function to validate keys
def validate_keys(patterns):
    invalid_keys = []
    for key_name, details in patterns.items():
        value = details["value"]
        if not value or not re.match(details["pattern"], value):
            invalid_keys.append(key_name)
    return invalid_keys

# Validation check
if st.button("Validate and Save"):
    invalid_keys = validate_keys(validation_patterns)

    if invalid_keys:
        st.error(f"Invalid or missing keys: {', '.join(invalid_keys)}")
    else:
        # Save API keys in session state
        st.session_state["Exa Key"] = exa_api_key
        st.session_state["Serper Key"] = serper_api_key
        st.session_state["OpenAI Key"] = openai_key
        # st.session_state["Gemini Key"] = gemini_key
        # st.session_state["Anthropic Key"] = anthropic_key

        st.success("API keys are valid and saved! Navigate to the next step using the sidebar.")
