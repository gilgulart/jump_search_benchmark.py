
import time
import statistics
import csv
from pathlib import Path

from algorithms.merge_sort import merge_sort
from algorithms.selection_sort import selection_sort
from algorithms.insertion_sort import insertion_sort
from algorithms.quick_sort import quick_sort
from algorithms.generate_lists import data


sorting_algorithms = {
    "Merge Sort": merge_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Quick Sort": quick_sort
}

tests = {
    1_000: data[1_000],
    10_000: data[10_000],
    50_000: data[50_000],
    100_000: data[100_000]
}


def benchmark(algorithm, arr: list[int], repetitions: int = 10, trials: int = 5):
    times = []

    for _ in range(trials):
        trial_times = []

        for _ in range(repetitions):
            arr_copy = arr.copy()

            start = time.perf_counter()
            algorithm(arr_copy)
            end = time.perf_counter()

            trial_times.append(end - start)

        times.append(statistics.mean(trial_times))

    return {
        "mean": statistics.mean(times),
        "median": statistics.median(times),
        "min": min(times),
        "max": max(times)
    }


def run_comparison():
    results = []

    for size, arr in tests.items():
        for name, algorithm in sorting_algorithms.items():

            if name in ("Selection Sort", "Insertion Sort") and size > 1_000:
                continue

            print(f"Executando {name} | {size:,} elementos")

            metrics = benchmark(
                algorithm,
                arr,
                repetitions=3,
                trials=3
            )

            results.append({
                "algorithm": name,
                "list_size": size,
                "mean": metrics["mean"],
                "median": metrics["median"],
                "min": metrics["min"],
                "max": metrics["max"
                ]
            })

    print("\nBenchmark concluído!")

    output_dir = Path("results")
    output_dir.mkdir(parents=True, exist_ok=True)

    csv_path = output_dir / "sorting_results.csv"

    with open(csv_path, "w", newline="", encoding="utf-8") as file:
        fieldnames = [
            "algorithm",
            "list_size",
            "mean",
            "median",
            "min",
            "max"
        ]

        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"Resultados salvos em: {csv_path}")


if __name__ == "__main__":
    run_comparison()
