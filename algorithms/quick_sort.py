def median_of_three(arr: list[int]) -> list[int]:
    first = arr[0]
    middle = arr[len(arr) // 2]
    last = arr[-1]

    candidates = [first, middle, last]
    candidates.sort()

    return candidates[1]

def quick_sort(arr: list[int]) -> list[int]:
    if len(arr) <= 1:
        return arr
    
    pivot = median_of_three(arr)
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)