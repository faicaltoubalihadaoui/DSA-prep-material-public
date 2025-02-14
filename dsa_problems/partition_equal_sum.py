# Backtrack + Memozation 
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1 :
            return False

        if sum(nums) % 2 != 0:
            return False
        target = sum(nums) // 2 

        memo = [[-1 for _ in range(target + 1)] for _ in range(len(nums))]

        def backtrack(index, total):
            if total == target:
                return True 
            elif index >= len(nums) or total > target:
                return False
            elif memo[index][total] != -1:
                return memo[index][total]
            memo[index][total] = backtrack(index + 1, total + nums[index]) or backtrack(index + 1, total)
            return memo[index][total]


        return backtrack(0, 0)



# Very bad approach time complexity wise
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return False

        ans = (
            []
        )  # Array that will store the indices of different subsets within the nums

        def backtrack(index, path):
            if path[:] and set(path[:]) not in ans:
                ans.append(set(path[:]))
            if index >= len(nums):
                return  # Stop recusrion for current candidate

            path.append(index)
            backtrack(index + 1, path)
            path.pop()
            backtrack(index + 1, path)

        backtrack(0, [])
        for partition in ans:  # partition is a set of indices
            candidate_equal_partition = 0
            for idx, val in enumerate(nums):
                if idx not in partition:
                    candidate_equal_partition += val
            partition_sum = 0
            for idx in partition:
                partition_sum += nums[idx]
            if partition_sum == candidate_equal_partition:
                return True

        return False


# Not working
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if not nums or len(nums) == 1:
            return False

        def backtracking(index, total, path, ans):
            if sum(path) == total:
                ans.append(path[:])
                return
            elif sum(path) > total or index >= len(nums):
                return False

            path.append(nums[index])
            included = backtracking(index + 1, total, path, ans)
            if included:
                return True
            else:
                path.pop()
                return backtracking(index + 1, total, path, ans)

        for sum_element in range(1, max(nums) + 1):
            ans = []
            backtracking(0, sum_element, [], ans)
            if len(ans) >= 2:
                tmp_len = 0
                for l in ans:
                    tmp_len += len(l)
                if tmp_len == len(nums):
                    return True

        return False
