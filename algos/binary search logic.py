# divide the array in two halves : Divide & Conquer Paradigm  O(log(n))
# the problem of searching an element is divided into smaller subproblems by narrowing the search range
# Binary search logic can be modified and adapted to search efficiently for elements within a DS
# Binary search works for all arrays of different lengths, no need to check edge cases 

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