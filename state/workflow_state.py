from pydantic import BaseModel
from typing import Dict, Any

class WorkflowState(BaseModel):
    raw_data_path: str = ""
    cleaned_data_path: str = ""
    eda_results: Dict[str, Any] = {}
    visualization_paths: Dict[str, str] = {}
    model_results: Dict[str, Any] = {}
    report_path: str = ""