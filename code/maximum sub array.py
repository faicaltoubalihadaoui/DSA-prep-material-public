# Kadane's algo
def maxSubArraySum(self,arr):
    ##Your code here
    if not arr:
        return 0
    
    max_sum = arr[0]
    local_sum = arr[0]
    for i in range(1, len(arr)):
        local_sum = max(local_sum + arr[i], arr[i])
        max_sum = max(max_sum, local_sum)
    return max_sum
                