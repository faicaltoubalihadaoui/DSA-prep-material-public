# Using DP bottom up approach
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if not nums:
            return True

        dp = [0] * len(nums)
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            if dp[i - 1] < i:
                return False
            dp[i] = max(dp[i - 1], nums[i] + i)
        return dp[-1] >= len(nums) - 1


# Greedy Approach
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, nums[i] + i)
            if max_reach >= len(nums) - 1:
                return True
        return False


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = 0
        for n in nums:
            if gas < 0:
                return False
            if n >= gas:
                gas = n
            gas -= 1
        return True

    # n^n solution
    # class Solution:
    def canJump(self, nums: List[int]) -> bool:

        n = len(nums)

        def dfs(i):
            if i == n - 1:
                return True

            end = nums[i] + i
            if end >= n - 1:
                return True
            for j in range(i + 1, end + 1):
                if dfs(j):
                    return True
            return False

        return dfs(0)

    # BTop Down approach :
    def canJump(self, nums: List[int]) -> bool:

        memo = {}
        n = len(nums)

        def dfs(i):
            if i == n - 1:
                return True
            if i in memo:
                return memo[i]

            end = nums[i] + i
            if end >= n - 1:
                return True
            for j in range(i + 1, end + 1):
                if dfs(j):
                    memo[j] = True
                    return True
            memo[i] = False
            return False

        return dfs(0)
