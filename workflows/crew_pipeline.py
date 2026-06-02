from crewai import Task, Crew

from agents.cleaning_agent import cleaning_agent
from agents.eda_agent import eda_agent
from agents.visualization_agent import visualization_agent
from agents.model_agent import model_agent
from agents.report_agent import report_agent

cleaning_task = Task(
    description="Clean uploaded dataset",
    agent=cleaning_agent,
    expected_output="Clean dataset and cleaning report"
)

eda_task = Task(
    description="Perform exploratory data analysis",
    agent=eda_agent,
    expected_output="EDA insights"
)

visual_task = Task(
    description="Generate visualizations",
    agent=visualization_agent,
    expected_output="Charts and plots"
)

model_task = Task(
    description="Train ML models",
    agent=model_agent,
    expected_output="Best model and metrics"
)

report_task = Task(
    description="Generate final business report",
    agent=report_agent,
    expected_output="PDF report"
)

crew = Crew(
    agents=[
        cleaning_agent,
        eda_agent,
        visualization_agent,
        model_agent,
        report_agent
    ],
    tasks=[
        cleaning_task,
        eda_task,
        visual_task,
        model_task,
        report_task
    ],
    verbose=True
)