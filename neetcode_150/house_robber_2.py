class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        elif 0 < len(nums) <= 2:
            return max(nums)

        def rob_linear(houses: List[int]) -> int:
            dp = [0] * len(houses)
            dp[0] = houses[0]
            dp[1] = max(houses[0], houses[1])
            for i in range(2, len(houses)):
                dp[i] = max(houses[i] + dp[i - 2], dp[i - 1])
            return dp[-1]

        return max(rob_linear(nums[:-1]), rob_linear(nums[1:]))
