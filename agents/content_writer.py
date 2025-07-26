import os
from crewai import Agent, LLM
from crewai_tools import FileWriterTool


# LLM configurations - Agent specific config
model = os.getenv("WRITER_AGENT_LLM")
temperature = float(os.getenv("WRITER_AGENT_TEMPERATURE"))

llm = LLM(
    model=model,
    temperature=temperature,
    max_tokens= 800
)

content_writer_agent = Agent(
    role="Content Writer",
    goal="Create  well-structured report",
    backstory = (
                "You are a professional content writer with expertise in creating "
                "clear, engaging, and well-structured documents. You can transform complex "
                "information into accessible and compelling content."
            ),
    llm=llm,
    tools=[FileWriterTool()],
    verbose=True,
)