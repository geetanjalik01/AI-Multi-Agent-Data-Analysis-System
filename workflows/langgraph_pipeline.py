from typing import TypedDict
import uuid

from langgraph.graph import StateGraph, END

from tools.cleaning_tools import clean_dataset
from tools.eda_tools import generate_eda
from tools.visualization_tools import create_visualizations
from tools.model_tools import train_model
from tools.report_tools import generate_pdf

from database.db_logger import save_analysis_log
from tools.rag_store import store_report


# ---------------------------------------------------
# WORKFLOW STATE
# ---------------------------------------------------

class WorkflowState(TypedDict):

    uploaded_file: str

    cleaned_path: str

    cleaning_report: dict

    eda_report: dict

    visualization_paths: list

    model_results: dict

    pdf_path: str


# ---------------------------------------------------
# CLEANING NODE
# ---------------------------------------------------

def cleaning_node(state):

    cleaned_path, cleaning_report = clean_dataset(
        state["uploaded_file"]
    )

    return {
        **state,
        "cleaned_path": cleaned_path,
        "cleaning_report": cleaning_report
    }


# ---------------------------------------------------
# EDA NODE
# ---------------------------------------------------

def eda_node(state):

    eda_report = generate_eda(
        state["cleaned_path"]
    )

    return {
        **state,
        "eda_report": eda_report
    }


# ---------------------------------------------------
# VISUALIZATION NODE
# ---------------------------------------------------

def visualization_node(state):

    visualization_paths = create_visualizations(
        state["cleaned_path"]
    )

    return {
        **state,
        "visualization_paths": visualization_paths
    }


# ---------------------------------------------------
# MODEL NODE
# ---------------------------------------------------

def model_node(state):

    model_results = train_model(
        state["cleaned_path"]
    )

    return {
        **state,
        "model_results": model_results
    }


# ---------------------------------------------------
# REPORT NODE
# ---------------------------------------------------

def report_node(state):

    final_text = f"""
    ===================================================
                    CLEANING REPORT
    ===================================================

    {state['cleaning_report']}


    ===================================================
                        EDA REPORT
    ===================================================

    {state['eda_report']}


    ===================================================
                    MODEL RESULTS
    ===================================================

    {state['model_results']}
    """

    # ---------------------------------------------------
    # GENERATE PDF
    # ---------------------------------------------------

    pdf_path = generate_pdf(
        final_text,
        "outputs/final_report.pdf"
    )

    # ---------------------------------------------------
    # SAVE ANALYSIS LOG TO POSTGRESQL
    # ---------------------------------------------------

    save_analysis_log(
        filename=state["uploaded_file"],
        accuracy=state["model_results"].get(
            "accuracy",
            0
        ),
        report_path=pdf_path
    )

    # ---------------------------------------------------
    # STORE REPORT IN VECTOR DATABASE (RAG)
    # ---------------------------------------------------

    store_report(
        report_text=final_text,
        report_id=str(uuid.uuid4())
    )

    # ---------------------------------------------------
    # RETURN UPDATED STATE
    # ---------------------------------------------------

    return {
        **state,
        "pdf_path": pdf_path
    }


# ---------------------------------------------------
# CREATE LANGGRAPH WORKFLOW
# ---------------------------------------------------

graph = StateGraph(WorkflowState)

# Add Nodes
graph.add_node(
    "cleaning",
    cleaning_node
)

graph.add_node(
    "eda",
    eda_node
)

graph.add_node(
    "visualization",
    visualization_node
)

graph.add_node(
    "model",
    model_node
)

graph.add_node(
    "report",
    report_node
)

# ---------------------------------------------------
# DEFINE FLOW
# ---------------------------------------------------

graph.set_entry_point("cleaning")

graph.add_edge(
    "cleaning",
    "eda"
)

graph.add_edge(
    "eda",
    "visualization"
)

graph.add_edge(
    "visualization",
    "model"
)

graph.add_edge(
    "model",
    "report"
)

graph.add_edge(
    "report",
    END
)

# ---------------------------------------------------
# COMPILE GRAPH
# ---------------------------------------------------

app = graph.compile()


# ---------------------------------------------------
# MAIN RUN FUNCTION
# ---------------------------------------------------

def run_langgraph_pipeline(uploaded_file):

    initial_state = {
        "uploaded_file": uploaded_file
    }

    result = app.invoke(initial_state)

    return result