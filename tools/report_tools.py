import os
import json

from fpdf import FPDF


# ==========================================
# GENERATE FINAL REPORT
# ==========================================

def generate_final_report(
    cleaning_report,
    eda_results,
    model_results
):

    # ======================================
    # CREATE REPORT DIRECTORY
    # ======================================

    os.makedirs(
        "outputs/reports",
        exist_ok=True
    )

    # ======================================
    # PDF PATH
    # ======================================

    pdf_path = (
        "outputs/reports/final_report.pdf"
    )

    # ======================================
    # CREATE PDF
    # ======================================

    pdf = FPDF()

    pdf.add_page()

    pdf.set_font(
        "Arial",
        "B",
        16
    )

    # ======================================
    # TITLE
    # ======================================

    pdf.cell(
        200,
        10,
        txt="AI Multi-Agent Data Analysis Report",
        ln=True,
        align="C"
    )

    pdf.ln(10)

    # ======================================
    # CLEANING REPORT
    # ======================================

    pdf.set_font(
        "Arial",
        "B",
        14
    )

    pdf.cell(
        200,
        10,
        txt="1. Data Cleaning Report",
        ln=True
    )

    pdf.set_font(
        "Arial",
        "",
        12
    )

    for key, value in cleaning_report.items():

        pdf.multi_cell(
            0,
            8,
            f"{key}: {value}"
        )

    pdf.ln(5)

    # ======================================
    # EDA REPORT
    # ======================================

    pdf.set_font(
        "Arial",
        "B",
        14
    )

    pdf.cell(
        200,
        10,
        txt="2. Exploratory Data Analysis",
        ln=True
    )

    pdf.set_font(
        "Arial",
        "",
        12
    )

    for key, value in eda_results.items():

        pdf.multi_cell(
            0,
            8,
            f"{key}: {value}"
        )

    pdf.ln(5)

    # ======================================
    # MODEL REPORT
    # ======================================

    pdf.set_font(
        "Arial",
        "B",
        14
    )

    pdf.cell(
        200,
        10,
        txt="3. Machine Learning Results",
        ln=True
    )

    pdf.set_font(
        "Arial",
        "",
        12
    )

    for key, value in model_results.items():

        pdf.multi_cell(
            0,
            8,
            f"{key}: {value}"
        )

    pdf.ln(5)

    # ======================================
    # SAVE PDF
    # ======================================

    pdf.output(pdf_path)

    # ======================================
    # SAVE JSON REPORTS
    # ======================================

    with open(
        "outputs/reports/cleaning_report.json",
        "w"
    ) as file:

        json.dump(
            cleaning_report,
            file,
            indent=4
        )

    with open(
        "outputs/reports/eda_report.json",
        "w"
    ) as file:

        json.dump(
            eda_results,
            file,
            indent=4
        )

    with open(
        "outputs/reports/model_report.json",
        "w"
    ) as file:

        json.dump(
            model_results,
            file,
            indent=4
        )

    return pdf_path