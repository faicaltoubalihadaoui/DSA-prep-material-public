"""
OrderedDict - Python's built-in
Maintains insertion order linked a linked list with O(1) lookup
Userful for caches and frequency counters

Time Complexity:
get() -> O(1)
put() -> O(1)
move_to_end() -> O(1)
    
"""

# LRU cache
from collections import OrderedDict


class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = OrderedDict()

    def get(self, key: int):
        if key in self.cache:
            self.cache.move_to_end(key)
            return self.cache[key]
        return -1

    def put(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)
        elif len(self.cache) >= self.capacity:
            self.cache.popitem(last=False)  # remove LRU first inserted element
        self.cache[key] = value
