"""
# Node Class

class Node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

# Iteration O(n)
class Solution:
    def reverseList(self, head):
        prev = None  # Initialize previous pointer
        current = head  # Start with the head of the list
        
        while current is not None:  # Traverse the list
            next_node = current.next  # Save the next node
            current.next = prev  # Reverse the current node's pointer
            prev = current  # Move the prev pointer forward
            current = next_node  # Move to the next node
        
        return prev  # At the end, prev will be the new head
    


# Recursion
class Solution:
    def reverseList(self, head):
        # base cases
        if head is None or head.next is None:
            return head

        # reverse the rest of the list
        rest = self.reverseList(head.next)

        # put the first element at the end
        head.next.next = head
        head.next = None

        # fix the head pointer
        return rest
    

#Stack principle LIFO 
class Solution:
    #Function to reverse a linked list.
    def reverseList(self, head):
        # Code here
        if head is None:
            return None
            
        stack = []  # Stack of Nodes
        current = head
        while current is not None:
            stack.append(current.data)
            current = current.next
            
        listtoreturn = Node(stack.pop())
        pointer = listtoreturn
        while stack:
            elementtoadd = stack.pop()
            pointer.next = Node(elementtoadd)
            pointer = pointer.next
        return listtoreturn

