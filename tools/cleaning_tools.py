import pandas as pd
import os
import json


def clean_dataset(file_path):

    # =====================================
    # CREATE OUTPUT FOLDER
    # =====================================

    os.makedirs(
        "outputs/cleaned_data",
        exist_ok=True
    )

    os.makedirs(
        "outputs/reports",
        exist_ok=True
    )

    # =====================================
    # LOAD DATASET
    # =====================================

    df = pd.read_csv(file_path)

    original_shape = df.shape

    # =====================================
    # STANDARDIZE COLUMN NAMES
    # =====================================

    df.columns = [
        col.strip().lower().replace(" ", "_")
        for col in df.columns
    ]

    # =====================================
    # REMOVE DUPLICATES
    # =====================================

    duplicates_removed = (
        df.duplicated().sum()
    )

    df = df.drop_duplicates()

    # =====================================
    # HANDLE MISSING VALUES
    # =====================================

    missing_before = (
        df.isnull().sum().sum()
    )

    # Fill numeric columns
    numeric_cols = (
        df.select_dtypes(
            include=["number"]
        ).columns
    )

    for col in numeric_cols:

        df[col] = df[col].fillna(
            df[col].median()
        )

    # Fill categorical columns
    categorical_cols = (
        df.select_dtypes(
            exclude=["number"]
        ).columns
    )

    for col in categorical_cols:

        df[col] = df[col].fillna(
            df[col].mode()[0]
        )

    missing_after = (
        df.isnull().sum().sum()
    )

    # =====================================
    # SAVE CLEANED DATASET
    # =====================================

    cleaned_path = (
        "outputs/cleaned_data/cleaned_dataset.csv"
    )

    df.to_csv(
        cleaned_path,
        index=False
    )

    # =====================================
    # CLEANING REPORT
    # =====================================

    cleaning_report = {

        "Original Shape": str(original_shape),

        "Cleaned Shape": str(df.shape),

        "Duplicates Removed": int(
            duplicates_removed
        ),

        "Missing Values Before": int(
            missing_before
        ),

        "Missing Values After": int(
            missing_after
        ),

        "Columns": list(df.columns)

    }

    # =====================================
    # SAVE REPORT
    # =====================================

    with open(
        "outputs/reports/cleaning_report.json",
        "w"
    ) as file:

        json.dump(
            cleaning_report,
            file,
            indent=4
        )

    

    return cleaned_path, cleaning_report