import streamlit as st
import pandas as pd
import plotly.express as px
import json
import os


def generate_business_dashboard(df):

    # ==========================================
    # CREATE OUTPUT FOLDERS
    # ==========================================

    os.makedirs(
        "outputs/dashboard",
        exist_ok=True
    )

    # ==========================================
    # CLEAN COLUMN NAMES
    # ==========================================

    df.columns = [
        col.strip().lower().replace(" ", "_")
        for col in df.columns
    ]

    # ==========================================
    # CONVERT OBJECT COLUMNS TO NUMERIC
    # ==========================================

    for col in df.columns:

        if df[col].dtype == "object":

            try:

                df[col] = (
                    df[col]
                    .astype(str)
                    .str.replace(",", "")
                    .str.replace("$", "")
                    .str.replace("₹", "")
                )

                df[col] = pd.to_numeric(
                    df[col],
                    errors="ignore"
                )

            except:
                pass

    # ==========================================
    # DETECT NUMERIC COLUMNS
    # ==========================================

    numeric_cols = df.select_dtypes(
        include=["number"]
    ).columns.tolist()

    # ==========================================
    # AUTO DETECT KPI COLUMNS
    # ==========================================

    revenue_col = None
    profit_col = None
    orders_col = None

    for col in numeric_cols:

        if (
            "revenue" in col
            or "sales" in col
            or "amount" in col
        ):
            revenue_col = col

        if (
            "profit" in col
            or "income" in col
            or "earnings" in col
        ):
            profit_col = col

        if (
            "orders" in col
            or "quantity" in col
            or "units" in col
        ):
            orders_col = col

    # ==========================================
    # CALCULATE KPIs
    # ==========================================

    total_revenue = (
        float(df[revenue_col].sum())
        if revenue_col
        else 0
    )

    total_profit = (
        float(df[profit_col].sum())
        if profit_col
        else 0
    )

    total_orders = (
        float(df[orders_col].sum())
        if orders_col
        else len(df)
    )

    # ==========================================
    # STREAMLIT UI
    # ==========================================

    st.header(
        "Business Intelligence Dashboard"
    )

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Total Revenue",
            f"{total_revenue:,.2f}"
        )

    with col2:

        st.metric(
            "Total Profit",
            f"{total_profit:,.2f}"
        )

    with col3:

        st.metric(
            "Total Orders",
            f"{total_orders:,.0f}"
        )

    # ==========================================
    # DATASET PREVIEW
    # ==========================================

    st.subheader("Dataset Preview")

    st.dataframe(
        df.head().astype(str),
        width="stretch"
    )

    # ==========================================
    # HISTOGRAM
    # ==========================================

    if len(numeric_cols) > 0:

        st.subheader(
            "Distribution Analysis"
        )

        selected_col = st.selectbox(
            "Select Numeric Column",
            numeric_cols
        )

        fig = px.histogram(
            df,
            x=selected_col,
            title=f"{selected_col} Distribution"
        )

        st.plotly_chart(
            fig,
            width="stretch"
        )

        # Save chart
        fig.write_html(
            f"outputs/dashboard/{selected_col}_distribution.html"
        )

    # ==========================================
    # CORRELATION HEATMAP
    # ==========================================

    if len(numeric_cols) >= 2:

        st.subheader(
            "Correlation Heatmap"
        )

        corr = df[
            numeric_cols
        ].corr()

        heatmap = px.imshow(
            corr,
            text_auto=True,
            aspect="auto",
            title="Feature Correlation"
        )

        st.plotly_chart(
            heatmap,
            width="stretch"
        )

        # Save heatmap
        heatmap.write_html(
            "outputs/dashboard/correlation_heatmap.html"
        )

    # ==========================================
    # TOP REVENUE ANALYSIS
    # ==========================================

    if revenue_col:

        st.subheader(
            "Top Revenue Records"
        )

        top_revenue_df = (
            df.sort_values(
                by=revenue_col,
                ascending=False
            )
            .head(10)
        )

        st.dataframe(
            top_revenue_df.astype(str),
            width="stretch"
        )

        top_revenue_df.to_csv(
            "outputs/dashboard/top_revenue_records.csv",
            index=False
        )

    # ==========================================
    # KPI SUMMARY
    # ==========================================

    dashboard_summary = {

        "Total Rows": int(len(df)),

        "Total Columns": int(len(df.columns)),

        "Revenue Column": (
            revenue_col
            if revenue_col
            else "Not Found"
        ),

        "Profit Column": (
            profit_col
            if profit_col
            else "Not Found"
        ),

        "Orders Column": (
            orders_col
            if orders_col
            else "Not Found"
        ),

        "Total Revenue": total_revenue,

        "Total Profit": total_profit,

        "Total Orders": total_orders
    }

    # ==========================================
    # SAVE FILES
    # ==========================================

    # Save dashboard dataset
    df.to_csv(
        "outputs/dashboard/dashboard_data.csv",
        index=False
    )

    # Save summary JSON
    with open(
        "outputs/dashboard/dashboard_summary.json",
        "w"
    ) as file:

        json.dump(
            dashboard_summary,
            file,
            indent=4
        )

    # ==========================================
    # SUCCESS MESSAGE
    # ==========================================

    st.success(
        "Dashboard generated successfully!"
    )

    st.success(
        "Dashboard files saved in outputs/dashboard/"
    )