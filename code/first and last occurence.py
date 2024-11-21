# Search
# Modified binary search algo
# Paradgim : Divide & Conquer and Two pass approach using same function for two pointers

class Solution:
    def find(self, arr, x):
        
        # code here
        if not arr or x not in arr: 
            return [-1, -1]
        
        output = [-1, -1]

        def binary_search(find_last):
            low = 0
            high = len(arr) - 1
            middle = -1
            while low <= high:
                middle = (low + high)// 2 
                if arr[middle] == x: # good we found an occurrence, now we continue
                    prev = middle 
                    if find_last: # we search for the top 
                        low = middle + 1
                    else: # we search for the bottom
                        high = middle - 1
                elif arr[middle] > x:
                    high = middle - 1
                else:
                    low = middle + 1
            return prev




        output[0] = binary_search(find_last=False) # find first element
        output[1] = binary_search(find_last=True) # find last element
        
        return output