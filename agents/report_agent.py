from crewai import Agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

report_agent = Agent(
    role="Executive Report Writer",

    goal="""
    Generate professional business reports
    from analytical outputs.
    """,

    verbose=True,
    llm=llm
)