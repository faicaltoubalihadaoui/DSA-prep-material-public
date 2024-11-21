########################## Brute force O(n2) ##############################
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        max_substring = 0
        for i in range(len(s)):
            j = i + 1
            dict_char = set()
            dict_char.add(s[i])
            while j < len(s) and s[j] not in dict_char:
                dict_char.add(s[j])
                j += 1
            dis = j - i
            max_substring = max(max_substring, dis)
        return max_substring


########################### Frequency Map  O(n) ########################## 2 Pointers right, left
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        max_substring = 0
        char_map = {}
        for right, c in s:
            if c in char_map:
                char_map[c] += 1
            else:
                char_map[c] = 1

            while char_map[c] > 1:
                char_map[s[left]] -= 1
                left += 1
            max_substring = max(max_substring, right - left + 1)

        return max_substring


#####################


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        max_substring = 0
        left = 0
        char_map = {}
        for right, c in enumerate(s):
            char_map[c] = 1 + char_map.get(c, 0)
            while char_map[c] > 1:
                char_map[s[left]] -= 1
                left += 1

            max_substring = max(max_substring, right - left + 1)

        return max_substring
