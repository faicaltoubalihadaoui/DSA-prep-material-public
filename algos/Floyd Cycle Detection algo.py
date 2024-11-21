
# O (n)
class Solution:
    #Function to check if the linked list has a loop.
    def detectLoop(self, head):
        #code here
        if not head:
            return False
        
        slow_pointer = head
        fast_pointer = head
        while fast_pointer and fast_pointer.next:
            slow_pointer = slow_pointer.next
            fast_pointer = fast_pointer.next.next
            if slow_pointer == fast_pointer:
                return True
        return False