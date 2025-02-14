class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return 0

        jumps = 0
        max_reach = 0
        curr_end = 0

        for i in range(n - 1):  # We don't need to check the last index
            max_reach = max(max_reach, i + nums[i])

            if i == curr_end:  # Time to jump
                jumps += 1
                curr_end = max_reach

            if curr_end >= n - 1:
                return jumps

        return jumps


### USING DP

from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        # dp[i] will hold the minimum jumps required to reach index i.
        dp = [float("inf")] * n
        dp[0] = 0  # No jump needed to reach the first index.

        # For every index, try to update the jumps for the reachable indices.
        for i in range(n):
            # The furthest index we can jump to from i is i + nums[i].
            # We iterate from i+1 up to and including i + nums[i] (but not exceeding n).
            furthest = min(n, i + nums[i] + 1)
            for j in range(i + 1, furthest):
                # Update dp[j] if a shorter jump sequence is found.
                dp[j] = min(dp[j], dp[i] + 1)

        # dp[n-1] holds the minimum jumps required to reach the last index.
        return dp[n - 1]


# not working
class Solution:
    def jump(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 0
        elif len(nums) == 2:
            return 1 if nums[0] >= 1 else 2

        dp = [(0, float("+Inf"))] * len(nums)
        dp[0] = (nums[0], 1)  # ( max_reach, min_step_required )
        for i in range(1, len(nums)):
            if dp[i - 1][0] < i:
                return -1

            if dp[i - 1][0] >= nums[i] + i:
                dp[i] = dp[i - 1]
            else:
                dp[i] = nums[i] + i, dp[i - 1][1] + 1

            if dp[i][0] >= len(nums) - 1:
                return dp[i][1]

        return dp[-1][1]
