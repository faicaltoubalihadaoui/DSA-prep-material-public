class Solution:
    def climbStairs(self, n: int) -> int:
        memo = [0] * (n + 1)
        for i in range(n + 1):
            if i in [0, 1, 2]:
                memo[i] = i
            else:
                memo[i] = memo[i - 1] + memo[i - 2]

        return memo[-1]


class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 0 or n == 1:
            return 1

        dp = [0] * (n + 1)
        dp[0] = dp[1] = 1

        for i in range(2, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[n]
