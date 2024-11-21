import heapq


class Solution:
    def kLargest(self, arr, k):
        if not arr or 0 > k >= len(arr):
            return []

        max_heap = []
        res = []
        for i in range(len(arr)):
            heapq.heappush(max_heap, -arr[i])

        for i in range(k):
            res.append(-heapq.heappop(max_heap))
        return res
