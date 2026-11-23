import csv
from pathlib import Path
from algorithms.jump_search import jump_search_count
from algorithms.merge_sort import (
    arr_1_000,
    arr_10_000,
    arr_50_000,
    arr_100_000
)

datasets = [
    arr_1_000,
    arr_10_000,
    arr_50_000,
    arr_100_000
]

results = []

for arr in datasets:
    target = arr[-1]

    index, comparisons = jump_search_count(arr, target)

    results.append({
        "algorithm": "Jump Search",
        "list_size": len(arr),
        "target": target,
        "index": index,
        "comparisons": comparisons
    })

    print(
        f"Lista: {len(arr):>7} | "
        f"Comparações: {comparisons:>5} | "
        f"Índice: {index}"
    )

output_dir = Path("results")
output_dir.mkdir(parents=True, exist_ok=True)

csv_path = output_dir / "jump_search_comparisons.csv"

with open(csv_path, "w", newline="", encoding="utf-8") as file:
    fieldnames = [
        "algorithm",
        "list_size",
        "target",
        "index",
        "comparisons"
    ]

    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerows(results)

print(f"\nResultados salvos em: {csv_path}")

