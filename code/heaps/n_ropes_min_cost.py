from typing import List
import heapq
class Solution:
    #Function to return the minimum cost of connecting the ropes.
   def minCost(self, arr: List[int]) -> int:
    
        min_heap = []
        for i in arr:
            heapq.heappush(min_heap, i)
            
        cost = 0
        while len(min_heap) > 1 :
            val_1 = heapq.heappop(min_heap)
            val_2 = heapq.heappop(min_heap)
            val = val_1 + val_2
            cost += val
            heapq.heappush(min_heap, val)
        return cost