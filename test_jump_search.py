from jump_search import jump_search, jump_search_count

from merge_sort import (
    arr_1_000,
    arr_10_000,
    arr_50_000,
    arr_100_000
)

from draw_element import (
    element_1_000,
    element_10_000,
    element_50_000,
    element_100_000
)

test_cases = [
    (arr_1_000, element_1_000),
    (arr_10_000, element_10_000),
    (arr_50_000, element_50_000),
    (arr_100_000, element_100_000),
]

for arr, target in test_cases:
    original = jump_search(arr, target)
    instrumented, comparisons = jump_search_count(arr, target)

    assert original == instrumented, (
        f"Resultados divergentes para lista de {len(arr)} elementos"
    )

    print(
        f"n={len(arr):>7} | "
        f"índice={instrumented:>7} | "
        f"comparações={comparisons:>5} | "
        f"validação OK"
    )