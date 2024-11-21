class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        def map_of_frequencies(ele):
            mapfre = {}
            for i in ele:
                if not i in mapfre:
                    mapfre[i] = 1
                else:
                    mapfre[i] += 1
            return mapfre

        s_map_of_freq = map_of_frequencies(s)
        t_map_of_freq = map_of_frequencies(t)
        if len(s_map_of_freq) != len(t_map_of_freq):
            return False
        for key, val in s_map_of_freq.items():
            if t_map_of_freq.get(key, -1) != val:
                return False
        return True


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s_count = {}
        t_count = {}

        for i in range(len(s)):
            s_count[s[i]] = 1 + s_count.get(s[i], 0)
            t_count[t[i]] = 1 + t_count.get(t[i], 0)

        return s_count == t_count
