from pathlib import Path

import matplotlib.pyplot as plt


FIGURES_DIR = Path("figures")


def generate_event_figure(event, event_window_data):
    FIGURES_DIR.mkdir(parents=True, exist_ok=True)

    output_file = FIGURES_DIR / f"{event['event_id']}_abnormal_returns.png"

    figure, axis = plt.subplots(figsize=(10, 6))
    axis.plot(
        event_window_data["date"],
        event_window_data["abnormal_return"],
        marker="o",
    )
    axis.axhline(0, color="black", linewidth=1)
    axis.set_title(f"{event['event_name']} Abnormal Returns")
    axis.set_xlabel("Date")
    axis.set_ylabel("Abnormal Return")
    figure.autofmt_xdate()
    figure.tight_layout()

    figure.savefig(output_file)
    plt.close(figure)

    return output_file
