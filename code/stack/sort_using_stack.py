class Solution:
    # your task is to complete this function
    # function sort the stack such that top element is max
    # funciton should return nothing
    # s is a stack
    def Sorted(self, s):
        # Code here
        if not s:
            return 
        peek = s.pop()
        self.Sorted(s)
        
        #Insert peek in the sorted stack 
        tmp_stack = []
        while s and peek < s[-1]:
            tmp_stack.append(s.pop())
        s.append(peek)
        while tmp_stack:
            s.append(tmp_stack.pop())
        

class Solution:
    def Sorted(self, s):
        # Base case: An empty stack or a single-element stack is already sorted
        if not s:
            return
        # Remove the top element
        top = s.pop()
        # Recursively sort the remaining stack
        self.Sorted(s)
        # Insert the top element back in its correct position
        self._insert_sorted(s, top)

    def _insert_sorted(self, s, element):
        # Base case: If the stack is empty or the element is greater than the top
        if not s or element > s[-1]:
            s.append(element)
            return
        
        top = s.pop()
        self._insert_sorted(s, element)
        
        # Put the top element back
        s.append(top)

