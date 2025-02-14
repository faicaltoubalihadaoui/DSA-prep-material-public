class Solution:
    # O(n3)
    def largestRectangleArea(self, heights: List[int]) -> int:

        max_val = 0

        def backtrack(i, j):
            nonlocal max_val
            if i >= len(heights) or j >= len(heights) or not heights[i : j + 1]:
                return
            horizontal_surface = min(heights[i : j + 1]) * (j - i + 1)
            vertical_surface = max(heights[i : j + 1])
            max_val = max(max_val, horizontal_surface, vertical_surface)
            backtrack(i + 1, j)
            backtrack(i, j + 1)

        backtrack(0, 0)
        return max_val


# O(n2)
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0  # Variable to store the maximum rectangle area

        for i in range(len(heights)):
            left_index, right_index = i - 1, i + 1

            while left_index >= 0 and heights[left_index] >= heights[i]:
                left_index -= 1

            while right_index < len(heights) and heights[right_index] >= heights[i]:
                right_index += 1

            width = right_index - left_index - 1
            local_area = width * heights[i]

            max_area = max(max_area, local_area)

        return max_area


class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        max_area = 0
        n = len(heights)

        for i in range(n + 1):
            current_height = heights[i] if i < n else 0

            while stack and heights[stack[-1]] > current_height:
                height = heights[stack.pop()]
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area
