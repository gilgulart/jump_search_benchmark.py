
import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Diretório raiz do projeto
BASE_DIR = Path(__file__).resolve().parent.parent

# Diretórios e arquivos
output_dir = BASE_DIR / "results" / "graphs"
csv_path = BASE_DIR / "results" / "sorting_results.csv"

# Cria a pasta dos gráficos caso não exista
output_dir.mkdir(parents=True, exist_ok=True)

df = pd.read_csv(csv_path)

# Análise empírica de crescimento
algorithms = ["Merge Sort", "Quick Sort"]

growth = df[df["algorithm"].isin(algorithms)].copy()

growth = growth.sort_values(["algorithm", "list_size"])

growth["previous_time"] = growth.groupby("algorithm")["mean"].shift(1)
growth["previous_size"] = growth.groupby("algorithm")["list_size"].shift(1)

growth["size_growth"] = growth["list_size"] / growth["previous_size"]
growth["time_growth"] = growth["mean"] / growth["previous_time"]

growth["nlogn_expected"] = (
    growth["list_size"] * growth["list_size"].apply(lambda n: __import__("math").log2(n))
)

growth["previous_nlogn"] = (
    growth["previous_size"] *
    growth["previous_size"].apply(lambda n: __import__("math").log2(n))
)

growth["theoretical_growth"] = (
    growth["nlogn_expected"] / growth["previous_nlogn"]
)

print("\nAnálise de crescimento empírico:")

print(
    growth[
        [
            "algorithm",
            "list_size",
            "size_growth",
            "time_growth",
            "theoretical_growth"
        ]
    ].round(2).to_string(index=False)
)
# ==========================================
# GRÁFICO 1 - COMPARAÇÃO COM 1.000 ELEMENTOS
# ==========================================

comparison_1000 = df[df["list_size"] == 1000]

plt.figure(figsize=(10, 6))

plt.bar(
    comparison_1000["algorithm"],
    comparison_1000["mean"] * 1000
)

plt.title("Comparação dos Algoritmos de Ordenação (1.000 elementos)")
plt.xlabel("Algoritmo")
plt.ylabel("Tempo médio (ms)")

plt.grid(axis="y", linestyle="--", alpha=0.3)
plt.tight_layout()

plt.savefig(
    output_dir / "sorting_comparison_1000.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()

# ==========================================
# GRÁFICO 2 - MERGE SORT VS QUICK SORT
# ==========================================

comparison_nlogn = df[
    df["algorithm"].isin(["Merge Sort", "Quick Sort"])
]

plt.figure(figsize=(10, 6))

for algorithm in comparison_nlogn["algorithm"].unique():
    algorithm_data = comparison_nlogn[
        comparison_nlogn["algorithm"] == algorithm
    ].sort_values("list_size")

    plt.plot(
        algorithm_data["list_size"],
        algorithm_data["mean"] * 1000,
        marker="o",
        label=algorithm
    )

plt.title("Merge Sort vs Quick Sort")
plt.xlabel("Quantidade de elementos")
plt.ylabel("Tempo médio (ms)")

plt.xscale("log")
plt.xticks(
    [1_000, 10_000, 50_000, 100_000],
    ["1.000", "10.000", "50.000", "100.000"]
)

plt.grid(True, linestyle="--", alpha=0.3)
plt.legend()
plt.tight_layout()

plt.savefig(
    output_dir / "merge_vs_quick_sort.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()

print("Gráficos salvos com sucesso!")
print(f"Diretório: {output_dir}")

# ==========================================
# GRÁFICO 3 - CRESCIMENTO EMPÍRICO VS TEÓRICO
# ==========================================

growth_plot = growth.dropna().copy()

growth_plot["interval"] = (
    growth_plot["previous_size"].astype(int).astype(str)
    + " → "
    + growth_plot["list_size"].astype(int).astype(str)
)

plt.figure(figsize=(10, 6))

# Merge Sort
merge_data = growth_plot[
    growth_plot["algorithm"] == "Merge Sort"
]

plt.plot(
    merge_data["interval"],
    merge_data["time_growth"],
    marker="o",
    label="Merge Sort"
)

# Quick Sort
quick_data = growth_plot[
    growth_plot["algorithm"] == "Quick Sort"
]

plt.plot(
    quick_data["interval"],
    quick_data["time_growth"],
    marker="o",
    label="Quick Sort"
)

# Crescimento teórico n log n
plt.plot(
    merge_data["interval"],
    merge_data["theoretical_growth"],
    marker="o",
    linestyle="--",
    label="Modelo n log n"
)

plt.title("Crescimento Empírico vs Teórico")
plt.xlabel("Intervalo de crescimento da entrada")
plt.ylabel("Fator de crescimento do tempo")

plt.grid(True, linestyle="--", alpha=0.3)
plt.legend()
plt.tight_layout()

plt.savefig(
    output_dir / "empirical_vs_theoretical_growth.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()
plt.close()