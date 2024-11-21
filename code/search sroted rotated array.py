def search(self,arr,key):
    # Complete this function
    if not arr :
        return -1
    
    low = 0
    high = len(arr) -1 
    while low <= high:
        middle = (low + high) // 2

        if arr[middle] == key:
            return middle
            
        if arr[high] > arr[middle]: # right part sorted
            if arr[middle] < key <= arr[high]:
                low = middle + 1 
            else:
                high = middle - 1
        else: # left part is sorted
            if arr[low] <= key < arr[middle]:
                high = middle -1
            else:
                low = middle + 1
    return -1