class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        index = 0
        first = strs[0]
        ans = ""
        while index < len(first):
            for st in range(1, len(strs)):
                if not (index < len(strs[st])) or strs[st][index] != first[index]:
                    return ans
            ans += first[index]
            index += 1
        return ans
