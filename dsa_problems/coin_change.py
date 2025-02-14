class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins:
            return -1

        dp = [float("+Inf")] * (amount + 1)
        dp[0] = 0

        for i in range(1, amount + 1):
            # calculate the min coins needed to have i as amount
            for coin in coins:
                if i >= coin:
                    dp[i] = min(dp[i], dp[i - coin] + 1)

        return dp[amount] if dp[amount] <= amount else -1
