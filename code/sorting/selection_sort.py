# https://www.geeksforgeeks.org/selection-sort-algorithm-2/
# O(n2)
class Solution: 
    def select(self, arr, i):
        # code here 
        min_element = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_element]:
                min_element = j
        return min_element
                
            
        
    def selectionSort(self, arr,n):
        #code here
        if not arr:
            return []
        
        for i in range(n):
            small_index = self.select(arr, i) # returns the smallest starting from i 
            arr[i], arr[small_index] = arr[small_index], arr[i]
        return arr