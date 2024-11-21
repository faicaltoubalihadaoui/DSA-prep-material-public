from collections import defaultdict
import heapq


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:

        graph = defaultdict(list)
        for flight in flights:
            graph[flight[0]].append((flight[1], flight[2]))

        min_heap = [(0, src, 0)]

        visited = dict()

        while min_heap:
            cost, node, stops = heapq.heappop(min_heap)

            if node == dst:
                return cost

            if stops > k:
                continue

            if (node, stops) in visited and visited[(node, stops)] <= cost:
                continue
            visited[(node, stops)] = cost

            for neighbor, price in graph[node]:
                heapq.heappush(min_heap, (cost + price, neighbor, stops + 1))

        return -1


class Solution:
    def findCheapestPrice(
        self, n: int, flights: List[List[int]], src: int, dst: int, k: int
    ) -> int:
        # Initialize distances: use n elements.
        distances = [float("inf")] * n
        distances[src] = 0

        # Relax edges up to k+1 times.
        for i in range(k + 1):
            temp = distances.copy()
            for u, v, price in flights:
                if distances[u] != float("inf") and distances[u] + price < temp[v]:
                    temp[v] = distances[u] + price
            distances = temp

        return -1 if distances[dst] == float("inf") else distances[dst]


# Djikstra : prix positive
# Bellman Ford
# A * Algo
