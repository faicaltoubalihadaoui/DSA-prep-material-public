class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_nums = sorted(nums)
        i = 0
        k = 1
        tmp = 1
        for i in range(len(nums) - 1):
            if sorted_nums[i] + 1 == sorted_nums[i + 1]:
                tmp += 1
            elif sorted_nums[i] == sorted_nums[i + 1]:
                continue
            else:
                k = max(tmp, k)
                tmp = 1
        return max(k, tmp)


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        sorted_nums = sorted(nums)
        i = 0
        k = 1
        tmp = 1
        while i < len(sorted_nums) - 1:
            if sorted_nums[i] + 1 == sorted_nums[i + 1]:
                tmp += 1
            elif sorted_nums[i] == sorted_nums[i + 1]:
                i += 1
                continue
            else:
                k = max(tmp, k)
                tmp = 1
            i += 1
        k = max(k, tmp)
        return k
