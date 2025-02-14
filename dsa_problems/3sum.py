class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if not nums or len(nums) < 3:
            return []

        nums = sorted(nums)
        ans = set()
        for i in range(len(nums)):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == 0:
                    ans.add((nums[left], nums[i], nums[right]))
                    right -= 1
                    left += 1
                elif current_sum > 0:  # decrease the sum
                    right -= 1
                else:  # increase the sum
                    left += 1

        return list(ans)
