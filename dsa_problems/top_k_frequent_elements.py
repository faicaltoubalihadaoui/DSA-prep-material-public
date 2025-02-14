import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        heap = []
        counter = {}
        for i in nums:
            counter[i] = 1 + counter.get(i, 0)

        for key, val in counter.items():
            heapq.heappush(heap, (-val, key))

        res = []
        while len(res) < k:
            res.append(heapq.heappop(heap)[1])
        return res


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        counter = {}
        for i in nums:
            counter[i] = 1 + counter.get(i, 0)

        sorted_dict = {
            k: v
            for k, v in sorted(counter.items(), key=lambda item: item[1], reverse=True)
        }
        count = 0
        res = []
        for key in sorted_dict.keys():
            res.append(key)
            count += 1
            if count == k:
                break

        return res
