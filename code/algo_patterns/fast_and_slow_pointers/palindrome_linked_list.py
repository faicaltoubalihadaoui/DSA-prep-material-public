# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: bool
        """
        # Stack to store the first half
        mid_stack = []
        slow, fast = head, head
        while fast and fast.next:
            mid_stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next

        # If the list has an odd number of nodes, skip the middle node
        if fast:
            slow = slow.next

        # Compare the second half of the LL with the stack
        while slow:
            if not mid_stack or mid_stack.pop() != slow.val:
                return False
            slow = slow.next

        return True


# T : 2 * O (n / 2)
# S : O( n / 2)
