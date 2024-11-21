# https://www.geeksforgeeks.org/bubble-sort-algorithm/
# O(n2)
def bubbleSort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False  # Track if any swaps are made
        for j in range(n - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:  # If no swaps, the array is already sorted
            break
    return arr
