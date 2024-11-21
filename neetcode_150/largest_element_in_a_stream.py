import heapq


class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k if k is not None else 0
        self.elements = nums if nums is not None else []
        heapq.heapify(self.elements)
        while len(self.elements) > k:
            heapq.heappop(self.elements)

    def add(self, val: int) -> int:
        heapq.heappush(self.elements, val)
        if len(self.elements) > self.k:
            heapq.heappop(self.elements)
        return self.elements[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
