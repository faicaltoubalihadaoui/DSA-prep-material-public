from collections import defaultdict


class Trie:

    def __init__(self, val=None):
        self.children = defaultdict(Trie)

    def insert(self, word: str) -> None:
        if not word:
            return
        next_element = self.children  # Trie instance
        for c in word:
            if c not in next_element:
                next_element[c] = defaultdict(Trie)
            next_element = next_element[c]
        next_element["*"] = defaultdict(Trie)

    def search(self, word: str) -> bool:
        next_element = self.children
        for c in word:
            if c not in next_element:
                return False
            next_element = next_element[c]
        return "*" in next_element

    def startsWith(self, prefix: str) -> bool:
        next_element = self.children
        for c in prefix:
            if c not in next_element:
                return False
            next_element = next_element[c]
        return True if next_element else False


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
