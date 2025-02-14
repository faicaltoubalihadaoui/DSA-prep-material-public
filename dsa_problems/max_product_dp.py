class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif len(nums) == 2:
            return max(nums[0], nums[1], nums[0] * nums[1])

        dp_max = [1] * len(nums)
        dp_min = [1] * len(nums)
        for i in range(0, len(nums)):
            val = (nums[i], dp_max[i - 1] * nums[i], dp_min[i - 1] * nums[i])
            dp_max[i] = max(val)
            dp_min[i] = min(val)
        return max(dp_max)
