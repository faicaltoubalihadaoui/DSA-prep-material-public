'''
class Node:
    def _init_(self,x):
        self.data = x
        self.next = None
'''
################################################## Solution 1 ######################################################
import heapq
class Solution:
    def mergeKLists(self, arr):
        pq = []
        idx = 0 
        # Add initial nodes of all K lists to the priority queue
        for node in arr:
            if node:
                heapq.heappush(pq, (node.data, idx,  node))  # Push tuple (data, idx, node)
                # the idx is used to differentiate between node elements
                idx +=1
                
        head = last = None
        while pq:
            # Extract the smallest node tuple
            _, _, min_node = heapq.heappop(pq)
            
            if head is None:
                head = last = min_node
            else:
                last.next = min_node
                last = last.next  # Move the pointer explicitly
            
            # If the smallest node has a next node, add it to the heap
            if min_node.next:
                heapq.heappush(pq, (min_node.next.data, idx, min_node.next))
                idx +=1
        return head

################################################## Solution 3 #####################################################
import heapq

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __lt__(self, other): # LESS THAN 
        # Compare nodes based on their data values
        return self.data < other.data

class Solution:
    def mergeKLists(self, arr):
        pq = []
        
        # Add initial nodes of all K lists to the priority queue
        for node in arr:
            if node:
                heapq.heappush(pq, node)  # Push the node directly

        head = last = None
        while pq:
            # Extract the smallest node
            min_node = heapq.heappop(pq)
            
            if head is None:
                head = last = min_node
            else:
                last.next = min_node
                last = last.next  # Move the pointer explicitly
            
            # If the smallest node has a next node, add it to the heap
            if min_node.next:
                heapq.heappush(pq, min_node.next)
        
        return head


################################################## Solution 2 ######################################################
import heapq
class Solution:
    def mergeKLists(self, arr):
        # code here
        # return head of merged list
        if not arr:
            return Node()
        
        min_heap = []
        
        
        merged = Node(0)
        head = merged
        for ll in arr: #n
            while ll:
                heapq.heappush(min_heap, ll.data) # log(k) tq k max size of an LL
                ll = ll.next
        
        # log(n)
        merged = Node(0)
        current = merged 
        while min_heap:
            current.next = Node(heapq.heappop(min_heap))
            current = current.next

        return merged.next