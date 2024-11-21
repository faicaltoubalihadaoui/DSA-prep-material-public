class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        if not nums:
            return None

        largest = None
        nums_sum = sum(nums)
        freq_map = defaultdict(int)
        for element in nums:
            freq_map[element] = freq_map.get(element, 0) + 1

        for idx, element in enumerate(nums):
            # element eventual outlier
            remaining_sum = nums_sum - element
            if not (remaining_sum % 2 == 0):
                continue

            target = remaining_sum // 2
            if target in freq_map and (
                target != element or freq_map.get(target, 0) > 1
            ):
                largest = max(largest, element) if largest else element

        return largest


class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        # Gather all the possible n - 2 arrays and for each array check the remaining two indices
        candidates = []
        n = len(nums)

        def backtrack(index, candidate):
            if len(candidate) == n - 2:
                candidates.append(set(candidate[:]))
                return
            if index >= n:
                return

            candidate.append(index)
            backtrack(index + 1, candidate)
            candidate.pop()
            backtrack(index + 1, candidate)

        backtrack(0, [])

        for candidate in candidates:
            original_set = set(range(n))
            result_set = original_set - candidate
            candidate_sum = sum(nums[i] for i in candidate)
            result_list = list(result_set)
            if len(result_list) == 2:
                if nums[result_list[0]] == candidate_sum:
                    return nums[result_list[1]]
                if nums[result_list[1]] == candidate_sum:
                    return nums[result_list[0]]

        return None
