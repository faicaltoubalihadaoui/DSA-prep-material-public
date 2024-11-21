class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(set(nums)) != len(nums)


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True

        return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_set = set()

        for n in nums:
            if n in num_set:
                return True
            num_set.add(n)

        return False
