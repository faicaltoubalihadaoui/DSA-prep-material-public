class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        elif len(s) == 1:
            return 1

        left = 0
        right = 0
        map_of_frequencies = {}
        max_val = 0
        while right < len(s):
            map_of_frequencies[s[right]] = 1 + map_of_frequencies.get(s[right], 0)
            while map_of_frequencies[s[right]] > 1 and left < right:
                map_of_frequencies[s[left]] -= 1
                left += 1
            dis = right - left + 1
            max_val = max(dis, max_val)
            right += 1

        return max_val
