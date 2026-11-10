"""Shared data and chart helpers for the UX test reports (used from the .qmd files)."""
import json
import os
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

NAVY = "#0b3d91"
GREY = "#52606d"
SEVERITY_ORDER = ["Critical", "High", "Medium", "Low"]
SEVERITY_COLORS = {"Critical": "#c0392b", "High": "#e67e22", "Medium": "#f1c40f", "Low": "#95a5a6"}

plt.rcParams.update({
    "font.family": "Segoe UI",
    "font.size": 9,
    "axes.edgecolor": "#c9d3e0",
    "axes.spines.top": False,
    "axes.spines.right": False,
    "svg.fonttype": "none",  # keep chart text as text: much smaller HTML
})


def score_color(score: float) -> str:
    if score <= 2:
        return "#c0392b"
    if score < 4:
        return "#f39c12"
    return "#27ae60"


def load_bugs() -> pd.DataFrame:
    df = pd.read_csv(Path(__file__).resolve().parent.parent / "bugs.csv")
    df["Severity"] = pd.Categorical(df["Severity"], SEVERITY_ORDER, ordered=True)
    return df


def target_format() -> str:
    """Output format of the current render (e.g. 'html', 'typst', 'confluence-html')."""
    info = os.environ.get("QUARTO_EXECUTE_INFO")
    if not info:
        return ""
    data = json.loads(Path(info).read_text(encoding="utf-8"))
    return data.get("format", {}).get("identifier", {}).get("target-format", "")


def md_table(df: pd.DataFrame, widths) -> str:
    """Pipe table whose separator dashes set relative column widths (used by PDF/Typst)."""
    head = "| " + " | ".join(df.columns) + " |"
    sep = "|" + "|".join("-" * w for w in widths) + "|"
    rows = ["| " + " | ".join(str(v) for v in row) + " |" for row in df.itertuples(index=False)]
    return "\n".join([head, sep, *rows])


def kpi_tiles(tiles):
    """tiles: list of (value, label, colour). Draws a row of score cards."""
    fig, axes = plt.subplots(1, len(tiles), figsize=(7.2, 1.25))
    for ax, (value, label, colour) in zip(axes, tiles):
        ax.set_axis_off()
        ax.add_patch(plt.Rectangle((0.02, 0.05), 0.96, 0.9, transform=ax.transAxes,
                                   facecolor="#f5f8fc", edgecolor=colour, linewidth=2))
        ax.text(0.5, 0.6, value, ha="center", va="center", fontsize=17, weight="bold", color=colour, transform=ax.transAxes)
        ax.text(0.5, 0.22, label, ha="center", va="center", fontsize=8, color=GREY, transform=ax.transAxes)
    fig.tight_layout(pad=0.2)
    plt.show()


def journey_chart(steps, scores, title):
    fig, ax = plt.subplots(figsize=(7.2, 0.32 * len(steps) + 0.6))
    y = range(len(steps))
    ax.barh(y, scores, color=[score_color(s) for s in scores], height=0.6)
    ax.set_yticks(list(y), [f"{i + 1}. {s}" for i, s in enumerate(steps)])
    ax.invert_yaxis()
    ax.set_xlim(0, 5)
    ax.set_xticks(range(0, 6))
    ax.axvline(3, color="#c9d3e0", linestyle="--", linewidth=1)
    for i, s in enumerate(scores):
        ax.text(s + 0.08, i, str(s), va="center", fontsize=8, color=GREY)
    avg = sum(scores) / len(scores)
    ax.set_title(f"{title} · average {avg:.1f} / 5", loc="left", color=NAVY, fontsize=10, weight="bold")
    fig.tight_layout()
    plt.show()


def grouped_scores(labels, a, b, a_name, b_name, title):
    fig, ax = plt.subplots(figsize=(7.2, 0.3 * len(labels) + 0.8))
    y = list(range(len(labels)))
    ax.barh([i - 0.18 for i in y], a, height=0.34, color="#e67e22", label=a_name)
    ax.barh([i + 0.18 for i in y], b, height=0.34, color=NAVY, label=b_name)
    ax.set_yticks(y, labels)
    ax.invert_yaxis()
    ax.set_xlim(0, 5)
    ax.legend(loc="lower right", frameon=False, fontsize=8)
    ax.set_title(title, loc="left", color=NAVY, fontsize=10, weight="bold")
    fig.tight_layout()
    plt.show()


def severity_chart(df: pd.DataFrame):
    counts = df["Severity"].value_counts().reindex(SEVERITY_ORDER, fill_value=0)
    fig, ax = plt.subplots(figsize=(7.2, 1.6))
    ax.barh(counts.index, counts.values, color=[SEVERITY_COLORS[s] for s in counts.index], height=0.6)
    ax.invert_yaxis()
    for i, v in enumerate(counts.values):
        ax.text(v + 0.2, i, str(v), va="center", fontsize=9, color=GREY)
    ax.set_title(f"{len(df)} bugs by severity", loc="left", color=NAVY, fontsize=10, weight="bold")
    fig.tight_layout()
    plt.show()


def minutes_chart(runs):
    """runs: list of (label, minutes, colour)."""
    fig, ax = plt.subplots(figsize=(7.2, 1.7))
    labels = [r[0] for r in runs]
    ax.barh(labels, [r[1] for r in runs], color=[r[2] for r in runs], height=0.55)
    ax.invert_yaxis()
    for i, r in enumerate(runs):
        ax.text(r[1] + 0.2, i, f"{r[1]:.0f} min" if r[1] >= 1 else f"{r[1] * 60:.0f} s", va="center", fontsize=8, color=GREY)
    ax.set_xlabel("minutes from Send to a working app")
    ax.set_title("Time to a working app", loc="left", color=NAVY, fontsize=10, weight="bold")
    fig.tight_layout()
    plt.show()
