def sorted_array_binary_search(arr,key):
    # Complete this function
    if not arr :
        return -1
    
    low = 0
    high = len(arr) -1 
    while low <= high:
        middle = (low + high) // 2
        if arr[middle] == key:
            return middle
        elif arr[middle] > key:
            high = middle - 1
        else:
            low = middle + 1
    return -1

print(sorted_array_binary_search([1,2,3], 1))