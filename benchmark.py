import time
import statistics
from pathlib import Path
import csv
from algorithms.jump_search import jump_search
from algorithms.merge_sort import arr_1_000, arr_10_000, arr_50_000, arr_100_000
from algorithms.draw_element import element_1_000, element_10_000, element_50_000, element_100_000

output_dir = Path('results')
output_dir.mkdir(exist_ok=True)

csv_path = output_dir / 'jump_search_results.csv'

def benchmark(arr: list[int], target: int, repetitions: int=100, trials: int = 50) -> dict:
    times = []
    
    for _ in range(10):
        jump_search(arr, target)
        
    for _ in range(trials):
        start = time.perf_counter()
        
        for _ in range(repetitions):
            jump_search(arr, target)

        end = time.perf_counter()
        elapsed = (end - start) / repetitions
        times.append(elapsed)    

    return {
        'mean': statistics.mean(times),
        'median': statistics.median(times),
        'min': min(times),
        'max': max(times)
    }
    
tests = [
    (arr_1_000, element_1_000),
    (arr_10_000, element_10_000),
    (arr_50_000, element_50_000),
    (arr_100_000, element_100_000),
]


with open(csv_path, 'w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(
        file,
        fieldnames=[
            'algorithm',
            'list_size',
            'target',
            'mean_us',
            'median_us',
            'min_us',
            'max_us'
        ]
    )

    writer.writeheader()

    for arr, target in tests:
        result = benchmark(arr, target)

        writer.writerow({
            'algorithm': 'Jump Search',
            'list_size': len(arr),
            'target': target,
            'mean_us': result['mean'] * 1_000_000,
            'median_us': result['median'] * 1_000_000,
            'min_us': result['min'] * 1_000_000,
            'max_us': result['max'] * 1_000_000
        })