"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""


class Solution:
    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        self.cache = {}  # original_id -> copied id

        current = head
        copy_list = Node(head.val)
        ll = copy_list
        self.cache[current] = copy_list
        while current.next:
            new_node = Node(current.next.val)
            self.cache[current.next] = new_node
            copy_list.next = new_node

            if current.random in self.cache:
                copied_random = self.cache[current.random]
                copy_list.random = copied_random

            current = current.next
            copy_list = copy_list.next

        for node_original, node_copy in self.cache.items():
            if not node_copy.random:
                random_origin = node_original.random
                if random_origin in self.cache:
                    random_copy = self.cache[random_origin]
                    node_copy.random = random_copy

        return ll
