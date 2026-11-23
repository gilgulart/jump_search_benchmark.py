import math
from merge_sort import arr_1_000, arr_10_000, arr_50_000, arr_100_000
from draw_element import element_1_000, element_10_000, element_50_000, element_100_000


def jump_search(arr: list[int], target: int) -> int:
    n = len(arr)
    step = int(math.sqrt(n))


    start = 0
    end = step

    while start < n and arr[min(end, n) - 1] < target:
        start = end
        end += step

        if start >= n:
            return -1


    for i in range(start, min(end, n)):
        if arr[i] == target:
            return i


        if arr[i] > target:
             return -1
   
    return -1


def jump_search_count(arr: list[int], target: int) -> tuple[int, int]:
    n = len(arr)
    comparisons = 0

    if n == 0:
        return -1, comparisons

    step = int(math.sqrt(n))
    start = 0
    end = step

    while start < n:
        comparisons += 1
        if arr[min(end, n) - 1] >= target:
            break

        start = end
        end += step

    if start >= n:
        return -1, comparisons

    for i in range(start, min(end, n)):
        comparisons += 1
        if arr[i] == target:
            return i, comparisons

        comparisons += 1
        if arr[i] > target:
            return -1, comparisons

    return -1, comparisons


def show_result(arr: list[int], target: int):

    index = jump_search(arr, target)

    if index != -1:
        return (
            f'Tamanho da lista: {len(arr)}\n'
            f'Elemento escolhido: {target}\n'
            f'Índice encontrado: {index}\n'
            f'Valor encontrado no índice: {index}\n'
            f'Busca correta: {arr[index] == target}'
            
        )
    
    return ('Elemento não encontrado')



