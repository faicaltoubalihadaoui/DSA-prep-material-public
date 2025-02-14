class Solution:
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == "0":
            return 0

        n = len(s)
        dp = [0] * n
        dp[0] = 1  # Single character decoding is valid if it's not "0"

        # Initialize dp[1] based on the first two characters
        if n > 1:
            if s[1] != "0":
                dp[1] = dp[0]
            if 10 <= int(s[0:2]) <= 26:
                dp[1] += 1

        # Fill dp array for the rest of the string
        for i in range(2, n):
            # Single-digit decoding
            if s[i] != "0":
                dp[i] += dp[i - 1]

            # Two-digit decoding
            if 10 <= int(s[i - 1 : i + 1]) <= 26:
                dp[i] += dp[i - 2]

        return dp[-1]
