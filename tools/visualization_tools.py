import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Create plot directory safely
PLOT_DIR = "outputs/plots"

os.makedirs(PLOT_DIR, exist_ok=True)


def generate_visualizations(file_path):

    df = pd.read_csv(file_path)

    plot_paths = {}

    numeric_columns = df.select_dtypes(include="number").columns

    # Histogram plots
    for column in numeric_columns[:2]:

        plt.figure(figsize=(6, 4))

        sns.histplot(df[column], kde=True)

        plt.title(f"Histogram of {column}")

        plot_path = f"{PLOT_DIR}/{column}_histogram.png"

        plt.savefig(plot_path)

        plt.close()

        plot_paths[f"{column}_histogram"] = plot_path

    # Heatmap
    plt.figure(figsize=(10, 6))

    correlation_matrix = df.corr(numeric_only=True)

    sns.heatmap(correlation_matrix, annot=True)

    heatmap_path = f"{PLOT_DIR}/correlation_heatmap.png"

    plt.savefig(heatmap_path)

    plt.close()

    plot_paths["correlation_heatmap"] = heatmap_path

    return plot_paths