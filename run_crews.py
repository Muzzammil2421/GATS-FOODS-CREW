import streamlit as st
from concurrent.futures import ThreadPoolExecutor
from open_ai import run_open_ai_crew
from gemini import run_gemini_crew
from anthropic import run_anthropic_crew


# Ensure API keys are set
if not all(
    key in st.session_state
    for key in ["Exa Key", "Serper Key", "OpenAI Key"]
):
    st.error("Please go back to the first page and enter API keys.")
    st.stop()


if not st.session_state.agent_definitions:
    st.error("Please go back to the second page and edit/save crew.")
    st.stop()

# Run crews function
def execute_crews_in_parallel():
    # with ThreadPoolExecutor() as executor:
    #     futures = {
    #         "openai": executor.submit(run_open_ai_crew, st.session_state.agent_definitions),
    #         # "gemini": executor.submit(run_gemini_crew, st.session_state.agent_definitions),
    #         # "anthropic": executor.submit(run_anthropic_crew, st.session_state.agent_definitions),
    #     }
    #     results = {key: future.result() for key, future in futures.items()}
    open_ai = run_open_ai_crew(st.session_state.agent_definitions)
    # print(open_ai.__str__())
    # results = {'openai': open_ai}
    return open_ai.__str__()


# Run Crew Button
if st.button("Run Crew"):
    st.write("Running the crew...")

    # Environment variables (optional for API key integration)
    import os

    os.environ["EXA_API_KEY"] = st.session_state["Exa Key"]
    os.environ["SERPER_API_KEY"] = st.session_state["Serper Key"]
    os.environ["OPENAI_API_KEY"] = st.session_state["OpenAI Key"]
    # os.environ["GOOGLE_API_KEY"] = st.session_state["Gemini Key"]
    # os.environ["ANTHROPIC_API_KEY"] = st.session_state["Anthropic Key"]

    try:
        with st.spinner("Executing crews in parallel, please wait..."):
            results = execute_crews_in_parallel()

            # Display results in columns
            st.write("### OpenAI Response")
            st.text(results)
            # col1 = st.columns(1)
            #
            # with col1:
            #     st.write("### OpenAI Response")
            #     st.text(results)

            # with col2:
            #     st.write("### Gemini Response")
            #     st.text(results["gemini"])

            # with col3:
            #     st.write("### Anthropic/Claude Response")
            #     st.text(results["anthropic"])

            st.success("Crews executed successfully!")
    except Exception as e:
        st.error(f"An error occurred while executing crews: {e}")
