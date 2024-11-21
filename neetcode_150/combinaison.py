# Better
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(start, tmp, total):
            if total == target:
                ans.append(list(tmp))
                return

            if total > target:
                return

            for i in range(start, len(candidates)):
                tmp.append(candidates[i])  #
                backtrack(i, tmp, total + candidates[i])
                tmp.pop()

        backtrack(0, [], 0)
        return ans


def combination_sum(candidates, target):
    ans = []

    def backtrack(start, path):
        if sum(path) == target and path[:] not in ans:
            ans.append(list(path))
        if sum(path) > target:
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path)
            path.pop()

    backtrack(0, [])
    return ans


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []

        def backtrack(start, tmp):
            if sum(tmp) == target and list(tmp) not in ans:
                ans.append(list(tmp))

            for i in range(start, len(candidates)):
                if sum(tmp) > target:
                    return
                tmp.append(candidates[i])
                backtrack(i, tmp)
                backtrack(i + 1, tmp)
                tmp.pop()

        backtrack(0, [])
        return ans
