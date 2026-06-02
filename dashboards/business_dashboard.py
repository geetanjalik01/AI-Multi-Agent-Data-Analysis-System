import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


def business_dashboard(df):

    st.title("AI Business Intelligence Dashboard")

    # ==========================================
    # CLEAN COLUMN NAMES
    # ==========================================

    df.columns = [
        col.lower().strip().replace(" ", "_")
        for col in df.columns
    ]

    # ==========================================
    # KPI SECTION
    # ==========================================

    st.subheader("Business KPIs")

    total_sales = (
        df["sales"].sum()
        if "sales" in df.columns
        else 0
    )

    total_profit = (
        df["profit"].sum()
        if "profit" in df.columns
        else 0
    )

    total_orders = len(df)

    avg_profit = (
        df["profit"].mean()
        if "profit" in df.columns
        else 0
    )

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Sales",
        f"{total_sales:,.2f}"
    )

    col2.metric(
        "Total Profit",
        f"{total_profit:,.2f}"
    )

    col3.metric(
        "Total Orders",
        total_orders
    )

    col4.metric(
        "Average Profit",
        f"{avg_profit:,.2f}"
    )

    st.divider()

    # ==========================================
    # SALES TREND
    # ==========================================

    if "sales" in df.columns:

        st.subheader("Sales Trend")

        sales_fig = px.line(
            df,
            y="sales",
            title="Sales Trend Analysis"
        )

        st.plotly_chart(
            sales_fig,
            use_container_width=True
        )

    # ==========================================
    # PROFIT BY CATEGORY
    # ==========================================

    if (
        "category" in df.columns
        and "profit" in df.columns
    ):

        st.subheader("Profit by Category")

        category_profit = (
            df.groupby("category")["profit"]
            .sum()
            .reset_index()
        )

        category_fig = px.bar(
            category_profit,
            x="category",
            y="profit",
            title="Category-wise Profit"
        )

        st.plotly_chart(
            category_fig,
            use_container_width=True
        )

    # ==========================================
    # REGION SALES DISTRIBUTION
    # ==========================================

    if (
        "region" in df.columns
        and "sales" in df.columns
    ):

        st.subheader("Regional Sales Distribution")

        region_sales = (
            df.groupby("region")["sales"]
            .sum()
            .reset_index()
        )

        region_fig = px.pie(
            region_sales,
            names="region",
            values="sales",
            title="Region-wise Sales"
        )

        st.plotly_chart(
            region_fig,
            use_container_width=True
        )

    # ==========================================
    # TOP PRODUCTS
    # ==========================================

    if (
        "product_name" in df.columns
        and "sales" in df.columns
    ):

        st.subheader("Top 10 Products")

        top_products = (
            df.groupby("product_name")["sales"]
            .sum()
            .sort_values(ascending=False)
            .head(10)
            .reset_index()
        )

        product_fig = px.bar(
            top_products,
            x="product_name",
            y="sales",
            title="Top Selling Products"
        )

        st.plotly_chart(
            product_fig,
            use_container_width=True
        )

    # ==========================================
    # HEATMAP
    # ==========================================

    numeric_df = df.select_dtypes(
        include=["int64", "float64"]
    )

    if not numeric_df.empty:

        st.subheader("Correlation Heatmap")

        corr = numeric_df.corr()

        heatmap_fig = px.imshow(
            corr,
            text_auto=True,
            aspect="auto",
            title="Feature Correlation Heatmap"
        )

        st.plotly_chart(
            heatmap_fig,
            use_container_width=True
        )

    # ==========================================
    # OUTLIER DETECTION
    # ==========================================

    if "profit" in df.columns:

        st.subheader("Profit Outlier Detection")

        box_fig = px.box(
            df,
            y="profit",
            title="Profit Outliers"
        )

        st.plotly_chart(
            box_fig,
            use_container_width=True
        )

    # ==========================================
    # DATA PREVIEW
    # ==========================================

    st.subheader("Dataset Preview")

    st.dataframe(
    df.head().astype(str),
    use_container_width=True
)

    # ==========================================
    # AI BUSINESS INSIGHTS
    # ==========================================

    st.subheader("AI Business Insights")

    insights = []

    if "profit" in df.columns:

        max_profit = df["profit"].max()

        min_profit = df["profit"].min()

        insights.append(
            f"Highest profit observed: {max_profit:.2f}"
        )

        insights.append(
            f"Lowest profit observed: {min_profit:.2f}"
        )

    if (
        "category" in df.columns
        and "profit" in df.columns
    ):

        best_category = (
            df.groupby("category")["profit"]
            .sum()
            .idxmax()
        )

        insights.append(
            f"Most profitable category: {best_category}"
        )

    if (
        "region" in df.columns
        and "sales" in df.columns
    ):

        best_region = (
            df.groupby("region")["sales"]
            .sum()
            .idxmax()
        )

        insights.append(
            f"Best performing region: {best_region}"
        )

    for insight in insights:

        st.success(insight)