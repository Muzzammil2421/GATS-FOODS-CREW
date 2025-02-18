import os
from crewai import Agent, Task, Crew, Process, LLM
from common import *


def run_gemini_crew(definitions):
    data_analyst_llm = LLM(
        api_key=os.getenv("GOOGLE_API_KEY"),
        model="gemini/gemini-1.5-pro",
        verbose=True,
        temperature=0.2,
    )

    content_specialist_llm = LLM(
        api_key=os.getenv("GOOGLE_API_KEY"),
        model="gemini/gemini-1.5-pro",
        verbose=True,
        temperature=0.7,
    )
    # Data Analyst Agent
    data_analyst_agent = Agent(
        role=definitions["data_analyst_agent_role"],
        goal=definitions["data_analyst_agent_goal"],
        backstory=definitions["data_analyst_agent_backstory"],
        tools=[serper_search_tool, exa_search_tool],  # Replace 'search_tool' with actual tool definitions
        llm=data_analyst_llm,
        verbose=True,
        memory=True,
    )

    # Content Specialist Agent
    content_specialist_agent = Agent(
        role=definitions["content_specialist_agent_role"],
        goal=definitions["content_specialist_agent_goal"],
        backstory=definitions["content_specialist_agent_backstory"],
        llm=content_specialist_llm,
        verbose=True,
        memory=True,
    )

    market_research_task = Task(
        description=definitions["market_research_task_description"],
        expected_output=definitions["market_research_task_expected_output"],
        agent=data_analyst_agent,
    )

    content_creation_task = Task(
        description=definitions["content_creation_task_description"],
        expected_output=definitions["content_creation_task_expected_output"],
        agent=content_specialist_agent,
    )

    # Assemble the Crew
    crew = Crew(
        agents=[data_analyst_agent, content_specialist_agent],
        tasks=[market_research_task, content_creation_task],
        process=Process.sequential,
    )

    result = crew.kickoff()
    return result

