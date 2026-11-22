from generate_lists import data

def merge_sort(arr: list[int]) -> list :
    if len(arr) <= 1:
        return arr


    mid = len(arr) // 2


    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
   
    result = []


    while left and right:
        if left[0] < right[0]:
            result.append(left.pop(0))
       
        else:
            result.append(right.pop(0))


    return result + left + right


arr_1_000 = merge_sort(data[1_000])
arr_10_000 = merge_sort(data[10_000])
arr_50_000 = merge_sort(data[50_000])
arr_100_000 = merge_sort(data[100_000])