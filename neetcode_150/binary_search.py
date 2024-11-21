class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        low = 0
        right = len(nums) - 1
        while low <= right:
            middle = (low + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[middle] > target:
                right = middle - 1
            else:
                low = middle + 1
        return -1
