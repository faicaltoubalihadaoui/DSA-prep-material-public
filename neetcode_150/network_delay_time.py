from collections import defaultdict
import heapq


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:

        graph = defaultdict(list)
        for element in times:
            graph[element[0]].append((element[1], element[2]))

        shortest_distances = {(val + 1): float("+Inf") for val in range(n)}
        shortest_distances[k] = 0
        min_heap = []
        heapq.heappush(min_heap, (0, k))  #
        while min_heap:
            current_distance, current_node = heapq.heappop(min_heap)

            if current_distance > shortest_distances[current_node]:
                continue
            else:
                for neighbor_node, weight in graph[current_node]:
                    neighbor_distance = weight + current_distance
                    if neighbor_distance < shortest_distances[neighbor_node]:
                        shortest_distances[neighbor_node] = neighbor_distance
                        heapq.heappush(min_heap, (neighbor_distance, neighbor_node))

        min_value = -1
        for node, distance in shortest_distances.items():
            if distance == float("+Inf"):
                return -1
            min_value = max(min_value, distance)
        return min_value
