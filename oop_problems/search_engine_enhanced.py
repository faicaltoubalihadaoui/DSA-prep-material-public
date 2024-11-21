from collections import defaultdict
import heapq


class SearchEngine:
    def __init__(self):
        self.trie = {}
        self.cache = defaultdict(int)

    def add_query(self, query, frequency):
        if query not in self.cache:
            self.cache[query] = frequency

            current_element = self.trie
            for c in query:
                if c not in current_element:
                    current_element[c] = {}
                current_element = current_element[c]
            current_element["*"] = {}

    def remove_query(self, query):
        if query not in self.cache:
            return False

        del self.cache[query]

        def _delete(node, word, index):
            if index == len(word):
                if "*" in node:
                    del node["*"]
                    return len(node) == 0
                else:
                    return False

            char = word[index]
            if char not in node:
                return False

            if _delete(node[char], word, index + 1):
                del node[char]
            return len(node) == 0

        _delete(self.trie, query, 0)
        return True

    def get_suggestions(self, prefix, k):
        current = self.trie

        for c in prefix:
            if c in current:
                current = current[c]
            else:
                return []

        words = self._collect_words(current, prefix)

        max_heap = []
        for word in words:
            heapq.heappush(max_heap, (-self.cache[word], word))

        suggestions = []
        while max_heap and len(suggestions) < k:
            _, word = heapq.heappop()
            suggestions.append(word)
        return suggestions

    def _collect_words(self, current, prefix):

        result = []

        def dfs(node, current_word):
            if "*" in node:
                result.append(current_word)

            for c in current:
                if c != "*":
                    dfs(current[c], prefix + c)

        dfs(current, prefix)
        return result
