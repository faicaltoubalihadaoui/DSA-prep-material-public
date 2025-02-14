def permute(self, nums: List[int]) -> List[List[int]]:
    ans = []

    def backtrack(start):
        if start == len(nums):  # Base case: full permutation reached
            ans.append(nums[:])  # Append a copy of the current permutation
            return

        for j in range(start, len(nums)):

            # we switch
            nums[start], nums[j] = nums[j], nums[start]
            backtrack(start + 1)
            # backtrack switch
            nums[start], nums[j] = nums[j], nums[start]

    backtrack(0)
    return ans
