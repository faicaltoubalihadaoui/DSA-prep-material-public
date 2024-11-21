# A peak always exists in an array
class Solution:
    def peakElement(self, arr):
        if not arr:
            return -1
        
        low = 0
        high = len(arr) - 1

        while low <= high:
            middle = (low + high) // 2
            
            # Explicitly check if `middle` is a peak
            if (middle == 0 or arr[middle] >= arr[middle - 1]) and \
               (middle == len(arr) - 1 or arr[middle] >= arr[middle + 1]):
                return middle
            
            # Move to the side where the peak might exist
            if middle < len(arr) - 1 and arr[middle] < arr[middle + 1]:
                low = middle + 1
            else:
                high = middle - 1
        
        return -1
