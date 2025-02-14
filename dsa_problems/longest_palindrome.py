# Dynamic programming approach
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        elif len(s) == 1:
            return s

        n = len(s)
        dp = [[False for _ in range(n)] for _ in range(n)]  # 0 0 inclusive   # 0 n

        left = 0
        right = 0

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                left = i
                right = i + 1

        # size 3  len 6     i = 0   j = 2
        for size in range(3, n + 1):
            for i in range(n - size + 1):
                j = i + size - 1
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    left = i
                    right = j

        return s[left : right + 1]


# Brute force ( O(n^3))
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        elif len(s) == 1:
            return s

        def check_palindrome(i, j):
            left = i
            right = j
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        for n in range(len(s), 0, -1):
            for left in range(len(s) - n + 1):
                right = left + n - 1
                if check_palindrome(left, right):
                    return s[left : right + 1]
        return ""


# Brute force ( O(n^3))
class Solution:
    def longestPalindrome(self, s: str) -> str:

        max_val = 0
        i = 0
        j = 0
        for left in range(len(s)):
            for right in range(left + 1, len(s)):
                a = s[left : right + 1 :]
                if a == a[::-1]:
                    dis = right - left + 1
                    if dis > max_val:
                        max_val = dis
                        i = left
                        j = right
        return s[i : j + 1]
