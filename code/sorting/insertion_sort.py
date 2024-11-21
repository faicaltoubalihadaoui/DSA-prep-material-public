# https://www.geeksforgeeks.org/insertion-sort-algorithm/
# O(n2)
class Solution:
    def insertionSort(self, arr):
        if not arr:
            return []
        for i in range(1, len(arr)):
            key = arr[i]
            j = i - 1
            # Shift elements of the sorted portion to the right
            while j >= 0 and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            # Insert the current element in the correct position
            arr[j + 1] = key
        return arr
      