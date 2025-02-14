class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:
            return -1

        low = 0
        high = len(nums) - 1
        while low <= high:
            middle = (low + high) // 2

            if nums[middle] == target:
                return middle

            if nums[high] > nums[middle]:  # right part sorted
                if nums[middle] < target <= nums[high]:
                    low = middle + 1
                else:
                    high = middle - 1
            else:  # left part is sorted
                if nums[low] <= target < nums[middle]:
                    high = middle - 1
                else:
                    low = middle + 1
        return -1
