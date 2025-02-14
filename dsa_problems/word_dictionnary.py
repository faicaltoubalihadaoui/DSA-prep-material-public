class WordDictionary:

    def __init__(self, children=None):
        self.children = children if children is not None else {}

    def addWord(self, word: str) -> None:
        curr = self.children
        for c in word:
            if not c in curr:
                curr[c] = {}
            curr = curr[c]
        curr["*"] = {}

    def search(self, word: str) -> bool:
        curr = self.children
        for idx, c in enumerate(word):
            if c != "." and c not in curr:
                return False
            elif c == ".":
                found = False
                for element in curr:
                    to_seach = WordDictionary(curr[element])
                    a = to_seach.search(word[idx + 1 :])
                    if a:
                        found = True
                        break
                return found
            else:
                curr = curr[c]
        return "*" in curr


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
