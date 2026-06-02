import pandas as pd
import json
import os

# Create reports directory safely
REPORT_DIR = "outputs/reports"

os.makedirs(REPORT_DIR, exist_ok=True)


def perform_eda(file_path):

    df = pd.read_csv(file_path)

    report = {
        "shape": df.shape,
        "columns": list(df.columns),
        "summary_statistics": df.describe(include="all").to_dict(),
        "correlation": df.corr(numeric_only=True).to_dict()
    }

    output_path = f"{REPORT_DIR}/eda_report.json"

    with open(output_path, "w") as f:
        json.dump(report, f, indent=4)

    return report