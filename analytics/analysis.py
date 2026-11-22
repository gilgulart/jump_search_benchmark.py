import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
from pathlib import Path

output_dir = Path("results")
output_dir.mkdir(parents=True, exist_ok=True)

csv = pd.read_csv("../results/jump_search_results.csv")

df = pd.DataFrame(csv)


plt.style.use("seaborn-v0_8-ticks")
COLOR = "#2563EB"

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(
    df["list_size"],
    df["mean_us"],
    marker="o",
    linewidth=2,
    markersize=7,
    label="Tempo médio",
)


for x, y in zip(df["list_size"], df["mean_us"]):
    ax.annotate(
        f"{y:.2f} µs",
        (x, y),
        textcoords="offset points",
        xytext=(0, 12),
        ha="center",
        fontsize=9,
        bbox=dict(boxstyle="round,pad=0.3", fc="white", ec=COLOR, alpha=0.9),
    )

ax.set_title("Jump Search — Tempo médio de execução", fontsize=15, fontweight="bold", pad=15)
ax.set_xlabel("Tamanho da lista (elementos)", fontsize=11)
ax.set_ylabel("Tempo médio (µs)", fontsize=11)

ax.xaxis.set_major_formatter(StrMethodFormatter("{x:,.0f}"))

ax.grid(True, alpha=0.4)
ax.legend()

plt.tight_layout()
plt.savefig(output_dir / "jump_search_mean.png", dpi=300, bbox_inches="tight")
plt.show()



fig, ax = plt.subplots(figsize=(10, 6))

COLOR_MEAN = "#2563EB"
COLOR_MEDIAN = "#F59E0B"

ax.plot(
    df["list_size"],
    df["mean_us"],
    marker="o",
    linewidth=2,
    markersize=7,
    color=COLOR_MEAN,
    label="Média"
)

ax.plot(
    df["list_size"],
    df["median_us"],
    marker="o",
    linewidth=2,
    markersize=7,
    color=COLOR_MEDIAN,
    label="Mediana"
)

ax.set_title(
    "Jump Search — Média vs Mediana",
    fontsize=15,
    fontweight="bold",
    pad=15
)

ax.set_xlabel("Tamanho da lista (elementos)", fontsize=11)
ax.set_ylabel("Tempo de execução (µs)", fontsize=11)

ax.xaxis.set_major_formatter(StrMethodFormatter("{x:,.0f}"))

ax.grid(True, alpha=0.4)
ax.legend()

plt.tight_layout()
plt.savefig(
    output_dir / "jump_search_mean_median.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()


fig, ax = plt.subplots(figsize=(10, 6))

COLOR = "#2563EB"

lower_error = df["mean_us"] - df["min_us"]
upper_error = df["max_us"] - df["mean_us"]

ax.errorbar(
    df["list_size"],
    df["mean_us"],
    yerr=[lower_error, upper_error],
    marker="o",
    linewidth=2,
    markersize=7,
    capsize=5,
    color=COLOR,
    label="Média (mín. – máx.)"
)

ax.set_title(
    "Jump Search — Variação do tempo de execução",
    fontsize=15,
    fontweight="bold",
    pad=15
)

ax.set_xlabel("Tamanho da lista (elementos)", fontsize=11)
ax.set_ylabel("Tempo de execução (µs)", fontsize=11)

ax.xaxis.set_major_formatter(StrMethodFormatter("{x:,.0f}"))

ax.grid(True, alpha=0.4)
ax.legend()

plt.tight_layout()
plt.savefig(
    output_dir / "jump_search_execution_variation.png",
    dpi=300,
    bbox_inches="tight"
)
plt.show()

