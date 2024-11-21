class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return
        l, r = 0, len(height) - 1
        max_surface = 0
        while r > l:
            a = abs(r - l) * min(height[r], height[l])
            if a >= max_surface:
                max_surface = a
            if height[r] > height[l]:
                l += 1
            else:
                r -= 1
        return max_surface
