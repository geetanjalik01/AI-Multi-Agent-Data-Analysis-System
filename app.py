import streamlit as st
import pandas as pd
import os
import json
import warnings

from sklearn.exceptions import ConvergenceWarning

warnings.filterwarnings("ignore", category=UserWarning)
warnings.filterwarnings("ignore", category=ConvergenceWarning)

# IMPORT TOOLS

from tools.cleaning_tools import clean_dataset
from tools.eda_tools import perform_eda
from tools.visualization_tools import generate_visualizations
from tools.model_tools import train_models
from tools.dashboard_tools import generate_business_dashboard
from tools.report_tools import generate_final_report

# CREATE DIRECTORIES

folders = [
    "uploads",
    "outputs",
    "outputs/reports",
    "outputs/plots",
    "outputs/models",
    "outputs/cleaned_data",
    "outputs/dashboard"
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

# STREAMLIT CONFIG

st.set_page_config(
    page_title="AI Multi-Agent Data Analysis Platform",
    layout="wide"
)

st.title("AI Multi-Agent Data Analysis Platform")

# FILE UPLOAD

uploaded_file = st.file_uploader(
    "Upload CSV File",
    type=["csv"]
)

# MAIN PIPELINE

if uploaded_file is not None:

    # SAVE UPLOADED FILE

    upload_path = os.path.join(
        "uploads",
        uploaded_file.name
    )

    with open(upload_path, "wb") as file:
        file.write(uploaded_file.getbuffer())

    st.success("Dataset Uploaded Successfully")
    
    # STEP 1 - DATA CLEANING

    st.header("Step 1 - Data Cleaning")

    with st.spinner("Cleaning Dataset..."):

        cleaned_path, cleaning_report = clean_dataset(
            upload_path
        )

    cleaned_df = pd.read_csv(cleaned_path)

    st.success("Data Cleaning Completed")

    # CLEANING REPORT

    st.subheader("Cleaning Report")

    st.json(cleaning_report)

    # CLEANED DATA PREVIEW

    st.subheader("Cleaned Dataset Preview")

    st.dataframe(
        cleaned_df.head().astype(str),
        width="stretch"
    )

    # DATASET INFORMATION

    st.subheader("Dataset Information")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            "Rows",
            cleaned_df.shape[0]
        )

    with col2:
        st.metric(
            "Columns",
            cleaned_df.shape[1]
        )

    with col3:
        st.metric(
            "Missing Values",
            int(cleaned_df.isnull().sum().sum())
        )

    with col4:
        st.metric(
            "Duplicate Rows",
            int(cleaned_df.duplicated().sum())
        )

    # STEP 2 - EDA

    st.header("Step 2 - Exploratory Data Analysis")

    with st.spinner("Performing EDA..."):

        eda_results = perform_eda(cleaned_path)

    st.success("EDA Completed")

    st.subheader("EDA Results")

    st.json(eda_results)

    # STEP 3 - VISUALIZATION

    st.header("Step 3 - Visualization")

    with st.spinner("Generating Visualizations..."):

        generate_visualizations(cleaned_path)

    st.success("Visualizations Generated")

    # STEP 4 - MACHINE LEARNING

    st.header("Step 4 - Machine Learning")

    target_column = st.selectbox(
        "Select Target Column",
        cleaned_df.columns
    )

    if st.button("Train Models"):

        with st.spinner("Training Models..."):

            try:

                model_results = train_models(
                    cleaned_path,
                    target_column
                )

                st.success("Model Training Completed")

                # PROBLEM TYPE

                st.subheader("Problem Type")

                st.write(
                    model_results["problem_type"]
                )

                # DROPPED COLUMNS

                st.subheader(
                    "Dropped High Cardinality Columns"
                )

                dropped_cols = model_results[
                    "dropped_columns"
                ]

                if len(dropped_cols) > 0:

                    dropped_df = pd.DataFrame({
                        "Dropped Columns": dropped_cols
                    })

                    st.dataframe(
                        dropped_df,
                        width="stretch"
                    )

                else:

                    st.success(
                        "No High Cardinality Columns Found"
                    )

                # MODEL RESULTS

                st.subheader("Model Results")

                results = model_results["results"]

                all_metrics = []

                for model_name, metrics in results.items():

                    st.markdown(f"### {model_name}")

                    if "Error" in metrics:

                        st.error(metrics["Error"])

                    else:

                        metric_df = pd.DataFrame({
                            "Metric": list(metrics.keys()),
                            "Value": list(metrics.values())
                        })

                        st.dataframe(
                            metric_df,
                            width="stretch"
                        )

                        metric_data = {
                            "Model": model_name
                        }

                        for metric_name, value in metrics.items():
                            metric_data[metric_name] = value

                        all_metrics.append(metric_data)

                # MODEL COMPARISON

                if len(all_metrics) > 0:

                    st.subheader("Model Comparison")

                    comparison_df = pd.DataFrame(
                        all_metrics
                    )

                    st.dataframe(
                        comparison_df,
                        width="stretch"
                    )

                # BEST MODEL

                st.subheader("Best Model")

                if model_results["problem_type"] == "classification":

                    best_model = max(
                        results.items(),
                        key=lambda x: x[1].get(
                            "Accuracy",
                            0
                        )
                    )

                    st.success(
                        f"{best_model[0]} "
                        f"(Accuracy: "
                        f"{best_model[1].get('Accuracy')}%)"
                    )

                else:

                    best_model = max(
                        results.items(),
                        key=lambda x: x[1].get(
                            "R2 Score",
                            -999
                        )
                    )

                    st.success(
                        f"{best_model[0]} "
                        f"(R2 Score: "
                        f"{best_model[1].get('R2 Score')})"
                    )

                # STEP 5 - REPORT GENERATION

                st.header(
                    "Step 5 - Report Generation"
                )

                with st.spinner(
                    "Generating Final Report..."
                ):

                    report_path = generate_final_report(
                        cleaning_report,
                        eda_results,
                        model_results
                    )

                st.success(
                    "Final Report Generated"
                )

                st.code(report_path)

                # STEP 6 - BUSINESS DASHBOARD

                st.header(
                    "Step 6 - Business Dashboard"
                )

                with st.spinner(
                    "Creating Dashboard..."
                ):

                    generate_business_dashboard(
                        cleaned_df
                    )

                st.success("Dashboard Created")

                # DOWNLOAD SECTION

                st.header("Generated Files")

                st.write(
                    "All generated files are "
                    "saved inside outputs/ folder"
                )

                # DOWNLOAD CLEANED DATA
                
                with open(cleaned_path, "rb") as file:

                    st.download_button(
                        label="Download Cleaned Dataset",
                        data=file,
                        file_name="cleaned_data.csv",
                        mime="text/csv"
                    )

            except Exception as e:

                st.error(
                    f"Error During Training: {str(e)}"
                )

else:

    st.info(
        "Upload CSV dataset to start analysis"
    )