import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

project_root = Path(__file__).resolve().parent.parent
results_dir = project_root / "results"

csv_path = results_dir / "jump_search_comparisons.csv"

df = pd.read_csv(csv_path)
df = df.sort_values("list_size")

# Análise de comparações por √n
df["sqrt_n"] = df["list_size"] ** 0.5

df["comparisons_per_sqrt_n"] = (
    df["comparisons"] / df["sqrt_n"]
)

print(
    df[
        [
            "list_size",
            "comparisons",
            "sqrt_n",
            "comparisons_per_sqrt_n"
        ]
    ]
)

print(df[["list_size", "target", "comparisons"]])

# Normalização
base_n = df["list_size"].iloc[0]
base_comparisons = df["comparisons"].iloc[0]

df["input_growth"] = df["list_size"] / base_n

df["sqrt_growth"] = (
    df["list_size"] / base_n
) ** 0.5

df["comparison_growth"] = (
    df["comparisons"] / base_comparisons
)

# Gráfico
fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(
    df["input_growth"],
    df["comparison_growth"],
    marker="o",
    linewidth=2,
    markersize=7,
    color="#2563EB",
    label="Comparações reais"
)

ax.plot(
    df["input_growth"],
    df["sqrt_growth"],
    marker="o",
    linestyle="--",
    linewidth=2,
    color="#F59E0B",
    label="Referência √n"
)

ax.plot(
    df["input_growth"],
    df["input_growth"],
    linestyle=":",
    linewidth=2,
    color="#DC2626",
    label="Referência linear (n)"
)

ax.set_title(
    "Jump Search — Crescimento das comparações",
    fontsize=15,
    fontweight="bold",
    pad=15
)

ax.set_xlabel(
    "Crescimento do tamanho da entrada (×)",
    fontsize=11
)

ax.set_ylabel(
    "Crescimento relativo das comparações (×)",
    fontsize=11
)

ax.grid(True, alpha=0.4)
ax.legend()

plt.tight_layout()

plt.savefig(
    results_dir / "jump_search_comparison_growth.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()

fig, ax = plt.subplots(figsize=(10, 6))

ax.plot(
    df["list_size"],
    df["comparisons_per_sqrt_n"],
    marker="o",
    linewidth=2,
    markersize=7,
    color="#2563EB",
    label="Comparações / √n"
)

for x, y in zip(
    df["list_size"],
    df["comparisons_per_sqrt_n"]
):
    ax.annotate(
        f"{y:.2f}",
        (x, y),
        textcoords="offset points",
        xytext=(0, 10),
        ha="center"
    )

ax.set_title(
    "Jump Search — Comparações normalizadas por √n",
    fontsize=15,
    fontweight="bold",
    pad=15
)

ax.set_xlabel("Tamanho da lista (elementos)", fontsize=11)
ax.set_ylabel("C(n) / √n", fontsize=11)

ax.grid(True, alpha=0.4)
ax.legend()

plt.tight_layout()

plt.savefig(
    results_dir / "jump_search_sqrt_ratio.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()