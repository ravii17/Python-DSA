def max_subarray_sum(arr):
    curr = arr[0]
    best = arr[0]
    for i in arr[1:]:
        curr = max(i, curr + i)
        best = max(best, curr)
    return best

arr = [2, 3, 4, 5, 6, 7, 3, 4, 5, 6, 7, 2, 3, 4, 5, 6]
print(max_subarray_sum(arr))