# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import heapq


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:

        self.heap = []
        for l in lists:
            if l:
                heapq.heappush(self.heap, (l.val, id(l), l))

        current = ListNode()
        point_current = current
        while self.heap:
            value, id_pop, node = heapq.heappop(self.heap)

            node_to_make = ListNode(value)
            current.next = node_to_make
            current = current.next
            node = node.next
            if node:
                heapq.heappush(self.heap, (node.val, id(node), node))

        return point_current.next
