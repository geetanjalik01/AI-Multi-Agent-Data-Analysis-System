from crewai import Agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

visualization_agent = Agent(
    role="Data Visualization Expert",

    goal="""
    Create meaningful visualizations
    for datasets.
    """,

    backstory="""
    Specialized in generating graphs,
    heatmaps, and statistical plots.
    """,

    verbose=True,
    llm=llm
)