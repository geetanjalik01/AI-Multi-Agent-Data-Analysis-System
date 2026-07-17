# InsightFlow AI
### Multi-Agent Business Intelligence & Data Analysis System
Transform raw datasets into actionable business insights using autonomous AI agents.

An AI-powered Multi-Agent Data Analysis Platform built using Streamlit, CrewAI, LangGraph, Machine Learning, Business Intelligence, RAG, and PostgreSQL.

The platform automatically performs data cleaning, exploratory data analysis (EDA), visualization, machine learning model training, business dashboard generation, report generation, and knowledge retrieval through an intelligent multi-agent workflow.

---

## Features

### Automated Data Cleaning

* Missing value handling
* Duplicate removal
* Data type correction
* Outlier detection
* Cleaning report generation

### Exploratory Data Analysis (EDA)

* Dataset profiling
* Statistical summary
* Correlation analysis
* Missing value analysis
* Feature distribution analysis

### Automated Visualizations

* Histograms
* Boxplots
* Correlation Heatmaps
* Scatter Plots
* Distribution Charts

### Machine Learning Module

* Classification Models
* Regression Models
* Automatic Target Selection
* Best Model Selection
* Model Performance Evaluation
* Model Serialization (.pkl)

### Business Intelligence Dashboard

* KPI Cards
* Revenue Analysis
* Profit Analysis
* Sales Trends
* Category Performance
* Top Customers
* Top Products
* Regional Analysis

### AI Report Generation

* Cleaning Report
* EDA Report
* Model Report
* Dashboard Report
* Executive Summary Report

### Retrieval-Augmented Generation (RAG)

* Dataset Knowledge Base
* Semantic Search
* Business Question Answering
* Vector Embedding Storage

### Database Integration

* PostgreSQL Support
* Analysis History Tracking
* Workflow Logging
* Report Storage

---

# System Architecture

Dataset Upload

↓

Cleaning Agent

↓

EDA Agent

↓

Visualization Agent

↓

Machine Learning Agent

↓

Dashboard Agent

↓

Report Agent

↓

RAG Knowledge Agent

↓

Executive Summary

---

# Tech Stack

### Frontend

* Streamlit

### AI Frameworks

* CrewAI
* LangGraph

### Machine Learning

* Scikit-Learn
* Pandas
* NumPy

### Visualization

* Plotly
* Matplotlib
* Seaborn

### Database

* PostgreSQL
* SQLAlchemy

### RAG

* Sentence Transformers
* ChromaDB

### Reporting

* ReportLab
* JSON Reports

---

# Project Structure

AI_Multi_Agent_Data_Analysis_System/

├── app.py

├── requirements.txt

├── README.md

├── .env

│

├── tools/

│ ├── cleaning_tools.py

│ ├── eda_tools.py

│ ├── visualization_tools.py

│ ├── model_tools.py

│ ├── dashboard_tools.py

│ ├── report_tools.py

│ ├── database_tools.py

│ └── rag_store.py

│

├── workflows/

│ ├── crew_pipeline.py

│ └── langgraph_pipeline.py

│

├── state/

│ └── workflow_state.py

│

├── utils/

│ ├── config_loader.py

│ ├── db_manager.py

│ └── sandbox_executor.py

│

├── database/

│ ├── database.py

│ ├── db_models.py

│ ├── db_logger.py

│ ├── create_tables.py

│ └── schema.sql

│

├── uploads/

│

├── outputs/

│ ├── cleaned_data/

│ ├── reports/

│ ├── plots/

│ ├── dashboard/

│ ├── models/

│ └── logs/

│

└── docs/

---

# Installation

## Clone Repository

git clone https://github.com/geetanjalik01/AI-Multi-Agent-Data-Analysis-System.git

cd AI-Multi-Agent-Data-Analysis-System

---

## Create Virtual Environment

Windows

python -m venv agent_env

agent_env\Scripts\activate

Linux / Mac

python3 -m venv agent_env

source agent_env/bin/activate

---

## Install Dependencies

pip install -r requirements.txt

---

## Configure Environment Variables

Create a .env file

OPENAI_API_KEY=your_api_key

DATABASE_URL=postgresql://username:password@localhost/database

---

# Run Application

streamlit run app.py

Open:

http://localhost:8501

---

# Workflow

1. Upload Dataset

2. Data Cleaning Agent

   * Removes duplicates
   * Handles missing values

3. EDA Agent

   * Statistical analysis
   * Correlation analysis

4. Visualization Agent

   * Generates charts
   * Saves plots

5. Machine Learning Agent

   * Trains multiple models
   * Selects best model

6. Dashboard Agent

   * Generates business KPIs
   * Creates dashboard insights

7. Report Agent

   * Creates executive reports

8. RAG Agent

   * Stores knowledge embeddings
   * Enables question answering

---

# Generated Outputs

outputs/

├── cleaned_data/

├── reports/

│ ├── cleaning_report.json

│ ├── eda_report.json

│ ├── model_report.json

│ ├── dashboard_report.json

│ └── executive_report.pdf

│

├── models/

│ ├── best_model.pkl

│ └── model_metrics.json

│

├── plots/

│ ├── histogram.png

│ ├── boxplot.png

│ └── heatmap.png

│

└── dashboard/

├── dashboard_summary.json

└── dashboard_data.csv

---

# Future Enhancements

* Multi-dataset analysis
* Real-time dashboard monitoring
* LLM-powered data storytelling
* Predictive business forecasting
* Automated Power BI report export
* Cloud deployment on AWS/Azure

---
