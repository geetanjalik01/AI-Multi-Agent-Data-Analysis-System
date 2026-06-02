from crewai import Agent

dashboard_agent = Agent(
    role="Business Intelligence Dashboard Specialist",

    goal=(
        "Generate intelligent business dashboards "
        "from uploaded company datasets and extract "
        "useful profit, sales, and performance insights."
    ),

    backstory=(
        "You are an expert Business Intelligence Engineer "
        "specialized in transforming raw business data "
        "into interactive dashboards and executive insights "
        "using Streamlit and Plotly."
    ),

    verbose=True,

    allow_delegation=False
)