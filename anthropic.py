from crewai import Agent, Task, Crew, Process
from langchain_core.language_models import BaseChatModel
from litellm import completion
from typing import Any, List, Optional
from langchain_core.messages import BaseMessage
from langchain_core.outputs import ChatResult, ChatGeneration
from pydantic import Field
from common import *

class CustomChatModel(BaseChatModel):
    temperature: float = Field(default=0.7)
    model_name: str = Field(default="claude-3-sonnet-20240229")

    class Config:
        arbitrary_types_allowed = True

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def _call(self, messages: List[BaseMessage], stop: Optional[List[str]] = None) -> str:
        response = completion(
            model="anthropic/claude-3-sonnet-20240229",
            messages=[{"role": m.role, "content": m.content} for m in messages],
            temperature=self.temperature,
        )
        return response.choices[0].message

    @property
    def _llm_type(self) -> str:
        return "anthropic"

    def _generate(
        self,
        messages: List[BaseMessage],
        stop: Optional[List[str]] = None,
        run_manager: Optional[Any] = None,
        **kwargs: Any,
    ) -> ChatResult:
        response = completion(
            model="anthropic/claude-3-sonnet-20240229",
            messages=[{"role": m.role, "content": m.content} for m in messages],
            temperature=self.temperature,
            stop=stop,
            **kwargs
        )
        message = response.choices[0].message
        generation = ChatGeneration(message=message)
        return ChatResult(generations=[generation])


def run_anthropic_crew(definitions):
    # Create Claude instances
    claude_analyst = CustomChatModel(temperature=0.2)
    claude_content = CustomChatModel(temperature=0.7)

    # Data Analyst Agent
    data_analyst_agent = Agent(
        role=definitions["data_analyst_agent_role"],
        goal=definitions["data_analyst_agent_goal"],
        backstory=definitions["data_analyst_agent_backstory"],
        tools=[serper_search_tool, exa_search_tool],
        llm=claude_analyst,
        verbose=True,
        memory=True,
    )

    # Content Specialist Agent
    content_specialist_agent = Agent(
        role=definitions["content_specialist_agent_role"],
        goal=definitions["content_specialist_agent_goal"],
        backstory=definitions["content_specialist_agent_backstory"],
        llm=claude_content,
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

    # Create and run the crew
    crew = Crew(
        agents=[data_analyst_agent, content_specialist_agent],
        tasks=[market_research_task, content_creation_task],
        process=Process.sequential,
    )

    result = crew.kickoff()
    return result
