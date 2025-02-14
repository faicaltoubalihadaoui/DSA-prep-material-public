class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        if not s:
            return None

        max_val = 0
        left = 0
        map_of_frequencies = {}
        max_freq_c = 0
        for idx, e in enumerate(s):
            map_of_frequencies[e] = 1 + map_of_frequencies.get(e, 0)
            max_freq_c = max(map_of_frequencies[e], max_freq_c)

            dis = idx - left + 1
            needed = dis - max_freq_c

            while k < needed and left <= idx:
                map_of_frequencies[s[left]] -= 1
                left += 1
                dis = idx - left + 1
                needed = dis - max_freq_c
            max_val = max(max_val, dis)

        return max_val
