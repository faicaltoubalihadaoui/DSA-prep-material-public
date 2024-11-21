# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 or not l2:
            return ListNode()

        pointer = ListNode()
        curr = pointer
        carry = 0
        while l1 or l2 or carry != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            summ = l1_val + l2_val + carry
            curr.next = ListNode(summ % 10)
            carry = summ // 10
            if l1:  ## l1 = l1.next if l1 else None
                l1 = l1.next
            if l2:
                l2 = l2.next
            curr = curr.next

        return pointer.next
