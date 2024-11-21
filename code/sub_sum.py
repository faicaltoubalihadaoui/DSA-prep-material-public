def maxSubArraySum_2(self,arr):
    ##Your code here
    if len(arr) == 0:
        return 0  # Edge case: empty array

    max_sum = arr[0]  # Initialize with the first element
    current_sum = arr[0]  # Keep track of the current sum
    
    for i in range(1, len(arr)):
        # If the current sum is negative, start a new subarray from arr[i]
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)  # Update max_sum
    
    return max_sum


class Solution:
    ##Complete this function
    #Function to find the sum of contiguous subarray with maximum sum.
    def maxSubArraySum(self,arr):
        ##Your code here
        i, j = 0, 1
        if len(arr) == 1:
            return arr[-1]
        else: 
            max_sum = max(arr[i], arr[j], sum(arr[i:j+1]))
            while j != len(arr):
                local_sum = arr[j]
                local_max_sum = local_sum
                i = j-1
                while i != -1:
                    local_sum += arr[i]
                    local_max_sum = max(local_max_sum, local_sum)
                    i -= 1
                max_sum = max(max_sum, local_max_sum)
                j += 1
            return max_sum
        
