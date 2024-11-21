# ITERATION USING QUEUE MODULE
class Solution:
    # Function to reverse the queue.
    def rev(self, q):
        if q.empty():
            return q

        # Use a stack to reverse the elements
        stack = []

        # Dequeue all elements from the queue and push them onto the stack
        while not q.empty():
            stack.append(q.get())

        # Pop all elements from the stack and enqueue them back to the queue
        while stack:
            q.put(stack.pop())

        return q




# RECURSION USING QUEUE MODULE
class Solution:
    # Function to reverse the queue using recursion.
    def rev(self, q):
        if q.empty():
            return q

        # Remove the front element
        front = q.get()
        
        # Recur to reverse the remaining queue
        self.rev(q)
        
        # we will come here as soon as the recursion unwinds then we start filling
        
        # Add the front element back to the end
        q.put(front)

        return q
    

#USING DEQUE MODULE
class Solution:
    # Function to reverse the queue.
    def rev(self, q):
        if not q:
            return None

        # Create a new deque to store reversed elements
        new_q = deque()
        
        # Transfer elements from q to new_q
        while q:
            new_q.append(q.pop())  # pop() to reverse order
        
        # Rebuild the original queue in reverse
        while new_q:
            q.append(new_q.popleft())
        
        return q

# USING DEQUE MODULE 2
class Solution:
    # Function to reverse the queue.
    def rev(self, q):
        if not q:
            return None

        # Use a stack to reverse the order
        stack = []
        
        # Transfer elements from the queue to the stack
        while q:
            stack.append(q.popleft())  # Remove from front of the queue
        
        # Transfer elements back to the queue from the stack
        while stack:
            q.append(stack.pop())  # Add to the back of the queue
        
        return q