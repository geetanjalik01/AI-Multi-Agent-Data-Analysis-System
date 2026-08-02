#  AI Multi-Agent Data Analysis System

An AI-powered end-to-end data analysis platform that automates data cleaning, exploratory data analysis (EDA), visualization, machine learning, report generation, and semantic report search.

Built using **Python**, **Streamlit**, **Scikit-learn**, **LangGraph**, **CrewAI**, **PostgreSQL**, and **ChromaDB**.

---

## Overview

Analyzing datasets usually involves multiple manual steps such as cleaning data, performing exploratory analysis, generating visualizations, training machine learning models, and preparing reports.

This project automates the complete workflow. Users simply upload a CSV dataset, and the system generates meaningful insights, visualizations, machine learning predictions, and a business report automatically.

---

## Features

-  Upload CSV datasets through a Streamlit interface
-  Automatic data cleaning
  - Remove duplicate records
  - Handle missing values
  - Standardize column names
-  Exploratory Data Analysis (EDA)
  - Dataset summary
  - Descriptive statistics
  - Correlation analysis
-  Automatic visualizations
  - Histograms
  - Correlation Heatmaps
-  Machine Learning
  - Automatic Classification/Regression detection
  - Decision Tree
  - Random Forest
  - Performance evaluation
-  Automatic PDF report generation
-  Store analysis history using PostgreSQL
-  Semantic report search using ChromaDB + Sentence Transformers
-  Modular AI Agent architecture using CrewAI
-  Workflow organization using LangGraph

---

#  Workflow

1. User uploads a CSV dataset.
2. Dataset is cleaned automatically.
3. Exploratory Data Analysis is performed.
4. Visualizations are generated.
5. ML module detects Classification or Regression automatically.
6. Decision Tree and Random Forest models are trained.
7. Best model performance is displayed.
8. PDF business report is generated.
9. Analysis history is stored in PostgreSQL.
10. Report embeddings are stored in ChromaDB for semantic retrieval.

---

#  AI Components

## CrewAI

Specialized AI agents were defined for:

- Supervisor Agent
- Cleaning Agent
- EDA Agent
- Visualization Agent
- Machine Learning Agent
- Report Generation Agent

These agents use **Llama 3.3 70B** through the **Groq API** for reasoning and modular workflow design.

> **Note:** In the current implementation, the data processing pipeline is executed through Python modules, while CrewAI defines the modular multi-agent architecture.

---

## LangGraph

LangGraph is used to organize the workflow by passing a shared workflow state between different modules.

---

## RAG Pipeline

Generated reports are:

- Converted into embeddings using Sentence Transformers
- Stored in ChromaDB
- Retrieved using semantic similarity search

---

#  Tech Stack

### Languages

- Python

### Data Analysis

- Pandas
- NumPy

### Machine Learning

- Scikit-learn
- Decision Tree
- Random Forest

### Visualization

- Matplotlib
- Seaborn

### Frontend

- Streamlit

### AI Frameworks

- CrewAI
- LangGraph

### LLM

- Llama 3.3 70B (Groq API)

### Database

- PostgreSQL
- SQLAlchemy

### Vector Database

- ChromaDB

### Embeddings

- Sentence Transformers

---

#  Project Structure

```
app.py
agents/
tools/
database/
rag/
reports/
outputs/
uploads/
```

---

# Future Improvements

- Interactive Plotly dashboards
- Hyperparameter tuning
- Additional ML algorithms (XGBoost, LightGBM)
- Multi-file support (Excel, JSON)
- Cloud deployment (AWS/Azure)
- Full CrewAI execution pipeline

---

B.Tech Information Technology | NIT Raipur

Interested in Data Analytics, Machine Learning, AI, and Multi-Agent Systems.
