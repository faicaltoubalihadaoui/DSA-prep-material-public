class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if not temperatures:
            return []

        ans = [0] * len(temperatures)
        stack = [] # decreasing monotonic stack
        for idx, temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:
                idx_to_resolve = stack.pop()
                ans[idx_to_resolve] = idx - idx_to_resolve

            stack.append(idx)
        return ans         