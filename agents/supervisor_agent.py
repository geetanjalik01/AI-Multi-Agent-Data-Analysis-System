from crewai import Agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

supervisor_agent = Agent(
    role="AI Workflow Supervisor",

    goal="""
    Coordinate all agents
    and manage workflow execution.
    """,

    verbose=True,
    allow_delegation=True,
    llm=llm
)