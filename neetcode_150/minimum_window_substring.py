from collections import Counter


from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if (not t and s) or (not s and t) or (len(t) > len(s)):
            return ""

        t_freq_map = Counter(t)
        min_len = float("Inf")
        left = 0
        needed_characters = len(t)

        for right, element in enumerate(s):
            if t_freq_map.get(element, 0) > 0:
                needed_characters -= 1
            if element in t:
                t_freq_map[element] -= 1

            while needed_characters == 0:
                if right - left + 1 <= min_len:
                    start_index = left
                    min_len = right - left + 1

                if s[left] in t and t_freq_map[s[left]] == 0:
                    needed_characters += 1  # window no more valid

                if s[left] in t:
                    t_freq_map[s[left]] += 1
                left += 1

        return "" if min_len == float("Inf") else s[start_index : start_index + min_len]

        # t  =  a
        # s =


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if (not t and s) or (not s and t) or (len(t) > len(s)):
            return ""

        t_freq_map = Counter(t)

        def valid_window(s_map, left, right):
            valid_window = True
            for k, v in t_freq_map.items():
                if not (s_map.get(k, 0) >= v):
                    valid_window = False
                    break
            return valid_window

        s_current_freq_map = {}
        min_window = ""
        left = 0

        for right, element in enumerate(s):  # n * len(t)
            s_current_freq_map[element] = 1 + s_current_freq_map.get(element, 0)

            # check if every k, v in t exists in current s_current_freq_map,
            # If yes, update the window, and move
            # If No, move to the next right element  and do the same operation
            while left <= right and valid_window(s_current_freq_map, left, right):
                if (not min_window) or (right - left + 1 <= len(min_window)):
                    min_window = s[left : right + 1]
                s_current_freq_map[s[left]] -= 1
                left += 1

        return min_window
