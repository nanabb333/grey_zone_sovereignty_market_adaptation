from pathlib import Path
import os

import pandas as pd


EVENT_RESULTS_FILE = Path("results/event_abnormal_return_summary.csv")
FIGURE_DIR = Path("figures")
MPL_CONFIG_DIR = Path(".matplotlib_cache")

# Keep Matplotlib cache files inside the project instead of the user's home folder.
os.environ.setdefault("MPLCONFIGDIR", str(MPL_CONFIG_DIR))

import matplotlib.pyplot as plt


def save_average_car_figure(event_results):
    # Calculate average CAR values by event mechanism.
    averages = event_results.groupby("mechanism")[
        ["twse_car_3", "tsmc_car_3"]
    ].mean()

    # Create a simple bar chart for comparison.
    ax = averages.plot(kind="bar", figsize=(8, 5))
    ax.set_title("Average 3-Day CAR by Event Type")
    ax.set_xlabel("Event Type")
    ax.set_ylabel("Cumulative Abnormal Return (%)")
    ax.axhline(0, color="black", linewidth=0.8)
    ax.legend(["TWSE", "TSMC"])
    plt.tight_layout()
    plt.savefig(FIGURE_DIR / "average_car_by_event_type.png", dpi=300)
    plt.close()


def save_event_scatter_figure(event_results):
    # Plot individual cases to show variation within each event type.
    colors = {
        "Risk": "#b23a48",
        "Strategic_Importance": "#247ba0",
    }

    fig, ax = plt.subplots(figsize=(9, 5))

    for mechanism, group in event_results.groupby("mechanism"):
        ax.scatter(
            group["twse_car_3"],
            group["tsmc_car_3"],
            label=mechanism,
            color=colors.get(mechanism, "gray"),
            s=70,
            alpha=0.85,
        )

    ax.axhline(0, color="black", linewidth=0.8)
    ax.axvline(0, color="black", linewidth=0.8)
    ax.set_title("Event-Level 3-Day CAR: TWSE and TSMC")
    ax.set_xlabel("TWSE 3-Day CAR (%)")
    ax.set_ylabel("TSMC 3-Day CAR (%)")
    ax.legend()
    plt.tight_layout()
    plt.savefig(FIGURE_DIR / "event_level_car_scatter.png", dpi=300)
    plt.close()


def main():
    # Create the figure directory if it does not already exist.
    FIGURE_DIR.mkdir(parents=True, exist_ok=True)
    MPL_CONFIG_DIR.mkdir(parents=True, exist_ok=True)

    # Load event-level results from the abnormal-return script.
    event_results = pd.read_csv(EVENT_RESULTS_FILE)

    # Generate the main portfolio figures.
    save_average_car_figure(event_results)
    save_event_scatter_figure(event_results)

    print(f"Saved figures to {FIGURE_DIR}")


if __name__ == "__main__":
    main()
