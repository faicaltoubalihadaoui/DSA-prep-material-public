class Solution:

    # Recursive no memo
    def isSubsetSum(self, arr, target):
        # code here
        def backtrack(index, total):
            if total == target:
                return True
            elif total > target or index >= len(arr):
                return False

            return backtrack(index + 1, total + arr[index]) or backtrack(
                index + 1, total
            )

        return backtrack(0, 0)

    # Memozation
    def isSubsetSum(self, arr, target):
        # code here
        memo = [[-1 for _ in range(target + 1)] for _ in range(len(arr))]

        def backtrack(index, total):
            if total == target:
                return True
            elif total > target or index >= len(arr):
                return
            elif memo[index][total] != -1:
                return memo[index][total]

            memo[index][total] = backtrack(index + 1, total + arr[index]) or backtrack(
                index + 1, total
            )
            return memo[index][total]

        return backtrack(0, 0)

    # DP
    def isSubsetSum(self, arr, target):
        n = len(arr)

        dp = [[False] * (target + 1) for _ in range(n + 1)]

        for i in range(n + 1):
            dp[i][0] = True

        for i in range(1, n + 1):
            for j in range(1, target + 1):
                if arr[i - 1] > j:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] or dp[i - 1][j - arr[i - 1]]
        return dp[n, target]

    def isSubSum(self, arr, target):
        n = len(arr)
        prev = [False] * (target + 1)
        curr = [False] * (target + 1)

        prev[0] = True
        for i in range(n + 1):
            for j in range(target + 1):
                if arr[i - 1] > j:
                    curr[j] = prev[j]
                else:
                    curr[j] = prev[j] or prev[j - arr[i - 1]]
            prev = curr[:]
        return prev[target]
