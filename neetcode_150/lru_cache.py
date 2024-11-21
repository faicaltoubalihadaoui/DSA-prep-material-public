from collections import defaultdict


class Node:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.dict = {}
        self.head = None  # LRU
        self.tail = None  # Most recently used

    def _add_to_tail_ll(self, node):

        if not self.head:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            node.next = None

    def _remove_node_ll(self, node):

        if node.prev:
            node.prev.next = node.next
        else:  # node is head
            self.head = node.next

        if node.next:
            node.next.prev = node.prev
        else:  # node is tail
            self.tail = node.prev

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self._remove_node_ll(node)
            self._add_to_tail_ll(node)  # MRU
            return node.value

        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            node.value = value

            self._remove_node_ll(node)
            self._add_to_tail_ll(node)  # MRU

        else:
            new_node = Node(key, value)
            self.dict[key] = new_node

            if self.size < self.capacity:

                self._add_to_tail_ll(new_node)
                self.size += 1

            else:  # remove head ( lru )

                lru = self.head
                self._remove_node_ll(lru)
                del self.dict[lru.key]

                self._add_to_tail_ll(new_node)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
