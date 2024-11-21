# https://www.geeksforgeeks.org/merge-sort/
# O(nlog(n))
class Solution:
    def merge(self, arr, left, mid, right):
        # Sizes of the two subarrays
        left_size = mid - left + 1
        right_size = right - mid
        
        # Create temporary arrays for left and right subarrays
        left_array = arr[left:mid + 1]
        right_array = arr[mid + 1:right + 1]
        
        # Initialize pointers for left, right, and merged arrays
        left_index = 0
        right_index = 0
        merge_index = left
        
        # Merge elements back into the original array
        while left_index < left_size and right_index < right_size:
            if left_array[left_index] <= right_array[right_index]:
                arr[merge_index] = left_array[left_index]
                left_index += 1
            else:
                arr[merge_index] = right_array[right_index]
                right_index += 1
            merge_index += 1
        
        # Copy any remaining elements from the left subarray
        while left_index < left_size:
            arr[merge_index] = left_array[left_index]
            left_index += 1
            merge_index += 1
        
        # Copy any remaining elements from the right subarray
        while right_index < right_size:
            arr[merge_index] = right_array[right_index]
            right_index += 1
            merge_index += 1

    def mergeSort(self, arr, left, right):
        if left < right:  # Base condition: Only sort if the subarray has more than one element
            mid = (left + right) // 2
            
            # Recursively sort the two halves
            self.mergeSort(arr, left, mid)
            self.mergeSort(arr, mid + 1, right)
            
            # Merge the sorted halves
            self.merge(arr, left, mid, right)

