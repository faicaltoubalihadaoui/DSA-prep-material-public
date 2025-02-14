# Backtracking Top down approach
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if (not s and wordDict) or (s and not wordDict):
            return False
        elif not s and not wordDict:
            return True

        def backtrack(index):
            if index == len(s):
                return True

            for right in range(index + 1, len(s) + 1):
                if s[index:right] not in wordDict:
                    continue
                else:
                    result = backtrack(right)
                    if result:
                        return True

            return False

        return backtrack(0)


# Backtracking Top down approach with memoization ( )


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if (not s and wordDict) or (s and not wordDict):
            return False
        elif not s and not wordDict:
            return True

        memo = [-1] * (len(s) + 1)

        def backtrack(index):
            if index == len(s):
                return True

            if memo[index] != -1:
                return memo[index]

            for right in range(index + 1, len(s) + 1):
                if s[index:right] not in wordDict:
                    continue
                else:
                    memo[right] = backtrack(right)
                    if memo[right]:
                        return True

            return False

        return backtrack(0)


# DP bottom up
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        if (not s and wordDict) or (s and not wordDict):
            return False
        elif not s and not wordDict:
            return True

        dp = [False] * (len(s) + 1)
        dp[0] = True  # Empty String

        for i in range(1, len(s) + 1):
            for j in range(i):
                if s[j:i] in wordDict and dp[j]:
                    dp[i] = True
                    break
        return dp[-1]
