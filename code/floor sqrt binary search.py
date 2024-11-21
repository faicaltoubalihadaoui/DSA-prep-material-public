class Solution:
    #Back-end complete function Template for Python 3

    def floorSqrt(self, n):

        # Base cases
        if (n == 0 or n == 1):
            return n

        start = 1
        end = n
        res = 0

        # binary search to find square root of a number
        while start <= end:
            mid = (start + end) // 2

            # if mid*mid == n, then mid is the required element
            if mid * mid == n:
                return mid

            # if mid*mid < n, then iterate for upper half
            if mid * mid < n:
                start = mid + 1
                res = mid

            # else, iterate for lower half
            else:
                end = mid - 1

        return res