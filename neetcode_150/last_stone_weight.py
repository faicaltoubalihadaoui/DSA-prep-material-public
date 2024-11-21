import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones_heap = []
        for e in stones:
            heapq.heappush(stones_heap, -e)

        while len(stones_heap) > 1:
            y = -heapq.heappop(stones_heap)
            x = -heapq.heappop(stones_heap)
            diff = y - x
            if diff > 0:
                heapq.heappush(stones_heap, -diff)
        return -stones_heap[0] if stones_heap else 0
