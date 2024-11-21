from collections import defaultdict
import heapq

class Trie:
    def __init__(self):
        self.children = defaultdict(Trie)

class SearchEngine: # CamelCase
    def __init__(self, val=None):
        self.trie = Trie()
        self.cache = defaultdict()
        
    def add_query(self, query, frequency): # we just push the frequency 
        if query not in self.cache:
            self.cache[query] = frequency
            current_element = self.children
            for c in query:
                if c not in current_element:
                    current_element[c] = Trie()
                current_element = current_element[c]
            
            current_element["*"] = Trie()
            return True 
        return False

    def remove_query(self, query):
        if query in self.cache:
            del self.cache[query]
    
            current_element = self.children 
            for c in query:
                
        else: 
            raise Exception('Element doesn t exist in the list')

    def get_suggestions(prefix, k):
            
            
        
        
        

search_engine = SearchEngine()
