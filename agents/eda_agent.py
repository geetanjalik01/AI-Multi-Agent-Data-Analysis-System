from crewai import Agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

eda_agent = Agent(
    role="Exploratory Data Analyst",

    goal="""
    Perform statistical analysis
    and generate useful insights.
    """,

    backstory="""
    Expert in discovering hidden patterns,
    trends, and correlations.
    """,

    verbose=True,
    llm=llm
)