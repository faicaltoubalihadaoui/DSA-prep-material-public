class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(start, path):
            res.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1, path)
                path.pop()

        backtrack(0, [])
        return res


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def backtrack(index, path):
            if index == len(nums):
                ans.append(path[:])
                return

            backtrack(index + 1, path)

            path.append(nums[index])
            backtrack(index + 1, path)
            path.pop()

        backtrack(0, [])
        return ans
