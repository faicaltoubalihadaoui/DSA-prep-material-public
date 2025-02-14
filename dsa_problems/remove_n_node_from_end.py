class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        size = 0

        head_copy = head
        current = head
        while current:
            size += 1
            current = current.next

        tmp = 0
        current = head
        prev = None
        while tmp != size - n and current:
            tmp += 1
            prev = current
            current = current.next

        next_one = current.next
        if prev:
            prev.next = next_one
        else:
            return head.next

        return head_copy


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        slow_pointer = head
        fast_pointer = head
        prev = None
        k = 0
        while fast_pointer:
            if k != n:
                k += 1
                fast_pointer = fast_pointer.next
            else:
                prev = slow_pointer
                fast_pointer = fast_pointer.next
                slow_pointer = slow_pointer.next
        if prev:
            prev.next = slow_pointer.next
        else:
            return head.next
        return head


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        fast, slow = head, head
        for _ in range(n):
            fast = fast.next

        if not fast:
            return head.next

        while fast.next:
            fast, slow = fast.next, slow.next

        slow.next = slow.next.next
        return head
