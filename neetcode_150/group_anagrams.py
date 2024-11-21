from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []

        counter = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            counter[key].append(s)

        return counter.values()


class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        if not strs:
            return []

        counter = {}  # anagram sorted -> [ anagrams ]
        copy_strs = [sorted(i) for i in strs]
        for i in range(len(copy_strs)):
            key_element = "".join(sorted(copy_strs[i]))
            if key_element not in counter:
                counter[key_element] = [strs[i]]
            else:
                counter[key_element].append(strs[i])

        result = [i for i in counter.values()]
        return result
