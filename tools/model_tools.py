# tools/model_tools.py

import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score,
    mean_squared_error,
    r2_score
)

from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.feature_selection import SelectKBest, chi2


# =========================================================
# DETECT PROBLEM TYPE
# =========================================================

def detect_problem_type(y):

    # If target is object/category
    if y.dtype == "object":
        return "classification"

    unique_values = y.nunique()

    # Small unique numeric values = classification
    if unique_values < 20:
        return "classification"

    return "regression"


# =========================================================
# MEMORY OPTIMIZATION
# =========================================================

def reduce_memory_usage(df):

    for col in df.columns:

        col_type = df[col].dtype

        if col_type != object:

            c_min = df[col].min()
            c_max = df[col].max()

            if str(col_type)[:3] == "int":

                if c_min > np.iinfo(np.int8).min and c_max < np.iinfo(np.int8).max:
                    df[col] = df[col].astype(np.int8)

                elif c_min > np.iinfo(np.int16).min and c_max < np.iinfo(np.int16).max:
                    df[col] = df[col].astype(np.int16)

                elif c_min > np.iinfo(np.int32).min and c_max < np.iinfo(np.int32).max:
                    df[col] = df[col].astype(np.int32)

            else:

                df[col] = df[col].astype(np.float32)

    return df


# =========================================================
# TRAIN MODELS
# =========================================================

def train_models(file_path, target_column):

    # =====================================================
    # LOAD DATA
    # =====================================================

    df = pd.read_csv(file_path)

    # Remove missing target rows
    df = df.dropna(subset=[target_column])

    # =====================================================
    # SPLIT FEATURES & TARGET
    # =====================================================

    X = df.drop(columns=[target_column])
    y = df[target_column]

    # =====================================================
    # REMOVE HIGH CARDINALITY COLUMNS
    # =====================================================

    high_cardinality_cols = []

    for col in X.columns:

        if X[col].dtype == "object":

            unique_count = X[col].nunique()

            # Drop columns with too many unique values
            if unique_count > 50:

                high_cardinality_cols.append(col)

    X = X.drop(columns=high_cardinality_cols)

    print("\nDropped High Cardinality Columns:")
    print(high_cardinality_cols)

    # =====================================================
    # ENCODE SMALL CATEGORICAL COLUMNS
    # =====================================================

    categorical_cols = X.select_dtypes(include=["object"]).columns

    for col in categorical_cols:

        unique_count = X[col].nunique()

        # Encode only small categorical columns
        if unique_count <= 20:

            X[col] = X[col].astype("category").cat.codes

        else:

            X = X.drop(columns=[col])

    # =====================================================
    # HANDLE MISSING VALUES
    # =====================================================

    for col in X.columns:

        if X[col].dtype == "object":

            X[col] = X[col].fillna("Unknown")

        else:

            X[col] = X[col].fillna(X[col].median())

    # =====================================================
    # MEMORY OPTIMIZATION
    # =====================================================

    X = reduce_memory_usage(X)

    # =====================================================
    # FEATURE SELECTION
    # =====================================================

    if X.shape[1] > 100:

        print(f"\nOriginal Features: {X.shape[1]}")

        # For classification only
        if detect_problem_type(y) == "classification":

            selector = SelectKBest(score_func=chi2, k=100)

            X = selector.fit_transform(abs(X), y)

        else:

            # For regression simply keep first 100 cols
            X = X.iloc[:, :100]

        print("Reduced Features to 100")

    # =====================================================
    # SCALE FEATURES
    # =====================================================

    scaler = StandardScaler(with_mean=False)

    X = scaler.fit_transform(X.astype(np.float32))

    # =====================================================
    # DETECT PROBLEM TYPE
    # =====================================================

    problem_type = detect_problem_type(y)

    print("\nProblem Type:", problem_type)

    # =====================================================
    # TRAIN TEST SPLIT
    # =====================================================

    X_train, X_test, y_train, y_test = train_test_split(
        X,
        y,
        test_size=0.2,
        random_state=42
    )

    # =====================================================
    # MODELS
    # =====================================================

    if problem_type == "classification":

        models = {
            "Decision Tree": DecisionTreeClassifier(
                max_depth=10,
                random_state=42
            ),

            "Random Forest": RandomForestClassifier(
                n_estimators=50,
                max_depth=10,
                random_state=42,
                n_jobs=-1
            )
        }

    else:

        models = {
            "Decision Tree Regressor": DecisionTreeRegressor(
                max_depth=10,
                random_state=42
            ),

            "Random Forest Regressor": RandomForestRegressor(
                n_estimators=50,
                max_depth=10,
                random_state=42,
                n_jobs=-1
            )
        }

    # =====================================================
    # TRAINING
    # =====================================================

    results = {}

    for name, model in models.items():

        print(f"\nTraining {name}...")

        try:

            model.fit(X_train, y_train)

            predictions = model.predict(X_test)

            # =============================================
            # CLASSIFICATION METRICS
            # =============================================

            if problem_type == "classification":

                accuracy = accuracy_score(y_test, predictions)

                results[name] = {
                    "Accuracy": round(accuracy * 100, 2)
                }

            # =============================================
            # REGRESSION METRICS
            # =============================================

            else:

                mse = mean_squared_error(y_test, predictions)

                r2 = r2_score(y_test, predictions)

                results[name] = {
                    "MSE": round(mse, 2),
                    "R2 Score": round(r2, 2)
                }

        except Exception as e:

            results[name] = {
                "Error": str(e)
            }

    # =====================================================
    # RETURN RESULTS
    # =====================================================

    return {
        "problem_type": problem_type,
        "results": results,
        "dropped_columns": high_cardinality_cols
    }