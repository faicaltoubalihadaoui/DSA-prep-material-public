##################### Recursion Approach without memozation
# TC : O(2^n)
# SC : O(n)


def knapSack(self, capacity, val, wt):
    # code here

    def helper(capa, i):
        if i >= len(val):
            return 0

        if capa + wt[i] > capacity:
            return helper(capa, i + 1)
        else:
            taking_item_i = helper(wt[i] + capa, i + 1)
            not_taking_item_i = helper(capa, i + 1)

        return max(val[i] + taking_item_i, not_taking_item_i)

    return helper(0, 0)


##################### Memozation approach O( n * W ) TC and SP( n * W )


def knapSack(self, capacity, val, wt):

    memo = {}

    def helper(capa, i):
        if i >= len(val):
            return 0

        if (i, capa) in memo:
            return memo[(i, capa)]

        if capa + wt[i] > capacity:
            memo[(i, capa)] = helper(capa, i + 1)
        else:
            memo[(i, capa)] = max(
                val[i] + helper(wt[i] + capa, i + 1), helper(capa, i + 1)
            )
        return memo[(i, capa)]

    return helper(0, 0)


#################################### Bottom Up approach


def knapSack(capacity, val, wt):
    n = len(val)

    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(n + 1):
        for c in range(capacity + 1):
            if wt[i] > c:
                dp[i + 1][c] = dp[i][c]
            else:
                dp[i + 1][c] = max(dp[i][c], val[i] + dp[i][c - wt[i]])
    return dp[n][capacity]
