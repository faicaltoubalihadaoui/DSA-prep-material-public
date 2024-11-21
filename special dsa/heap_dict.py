"""
Heap for efficient priority management O(log n)
Hashmap for fast lookups O(1)
Example : Dijkstra algo

A heap provides efficient operations:

Insertion: O(logn)
Deletion (extract min/max): O(logn)
    
"""

import heapq


def djikstra(graph, start):
    min_heap = []
    shortest_distances = {node: float("Inf") for node in graph}
    shortest_distances[start] = 0

    heapq.heappush(min_heap, (0, start))  # (distance, node)

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)

        if current_distance > shortest_distances[current_node]:
            continue
        else:
            for neighbor, weight in graph[current_node]:
                new_distance = current_distance + weight

                if new_distance < shortest_distances[neighbor]:
                    shortest_distances[neighbor] = new_distance
                    heapq.heappush(min_heap, (new_distance, neighbor))
    return shortest_distances


### djikstra between two nodes
def dijkstra(graph, start: int, end: int):
    min_heap = [(0, start, [start])]  # (distance, current_node, path_so_far)
    shortest_distances = {start: 0}  # Track shortest distance to each node

    while min_heap:
        current_dist, node, path = heapq.heappop(min_heap)

        # If we reached the target node, return the shortest path
        if node == end:
            return path, current_dist

        # Explore neighbors
        for neighbor, weight in graph.get(node, []):
            new_dist = current_dist + weight

            # Only consider this path if it's better than any previously found
            if (
                neighbor not in shortest_distances
                or new_dist < shortest_distances[neighbor]
            ):
                shortest_distances[neighbor] = new_dist
                heapq.heappush(min_heap, (new_dist, neighbor, path + [neighbor]))

    return [], -1  # If no path is found


### djikstra between two nodes
def shortest_path(graph, start, end):
    min_heap = []
    shortest_distance = float("Inf")
    heapq.heappush(min_heap, (shortest_distance, start))

    while min_heap:
        current_distance, current_node = heapq.heappop(min_heap)
        if current_node is end and shortest_distance > current_distance:
            continue

        for neighbor, weight in graph[current_node]:
            new_dist = current_distance + weight
            if neighbor is end and shortest_distance > new_dist:
                shortest_distance = new_dist
            heapq.heappush(min_heap, (new_dist, neighbor))
    return shortest_distance


#### shortest path from a node_1, u to a node_2 v


def shortest_path(graph, start, end):
    ##assumes no cycles in the graph
    res_path = []
    shortest_distance = float("inf")

    def backtrack(start, end, current_dist, path):
        nonlocal shortest_distance
        nonlocal res_path

        if start == end:  # we found our candidate
            if current_dist < shortest_distance:
                shortest_distance = current_dist
                res_path = path[:]

        for weight, neighbor in graph[start]:
            new_dist = weight + current_dist
            path.append(neighbor)
            backtrack(neighbor, end, new_dist, path)
            path.pop()

    backtrack(start, end, 0, res_path)
    if shortest_distance == float("inf"):
        return [], -1
    return res_path, shortest_distance


""" 
the local variable new_dist is specific to each recursive call, meaning that the value of new_dist does not persist across different recursion levels.
Explanation:

In Python, function arguments are passed by value for immutable types (like integers), meaning that within each function call, the variable new_dist is independent of the new_dist in other recursive calls.
Why new_dist -= weight is unnecessary:

Consider the recursive call sequence:

for weight, neighbor in graph[start]:
    new_dist = weight + current_dist  # Calculate the new distance
    path.append(neighbor)
    backtrack(neighbor, end, new_dist, path)
    path.pop()
    new_dist -= weight  # This line is unnecessary

    When the recursion goes deeper, each function call receives a fresh copy of new_dist, so after the function returns, the previous level's new_dist remains unchanged.
    There's no need to subtract the weight, as Python's call stack already handles scoping and variable shadowing for function calls. """
