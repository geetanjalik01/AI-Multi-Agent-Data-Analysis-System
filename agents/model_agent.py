from crewai import Agent
from langchain_groq import ChatGroq
from dotenv import load_dotenv
import os

load_dotenv()

llm = ChatGroq(
    groq_api_key=os.getenv("GROQ_API_KEY"),
    model_name="llama-3.3-70b-versatile"
)

model_agent = Agent(
    role="Machine Learning Engineer",

    goal="""
    Train and evaluate machine learning models.
    """,

    backstory="""
    Expert in model selection,
    training, evaluation, and optimization.
    """,

    verbose=True,
    llm=llm
)