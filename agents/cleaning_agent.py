from crewai import Agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

cleaning_agent = Agent(
    role="Senior Data Cleaning Specialist",

    goal="""
    Clean uploaded datasets safely and accurately.
    """,

    backstory="""
    Expert in handling missing values,
    duplicates, outliers, and datatype corrections.
    """,

    verbose=True,
    memory=False,
    allow_delegation=False,
    llm=llm
)