from collections import defaultdict


############################################# DFS
# TC : O(V+E)
# SC : O(V)
def has_cycle_dfs(graph, num_nodes):
    visited = set()
    rec_stack = set()

    def dfs(node):
        if node in rec_stack:
            return True  # Cycle detected
        if node in visited:
            return False  # Already processed

        rec_stack.add(node)  # Mark node as being visited in current path

        for neighbor in graph[node]:
            if dfs(neighbor):
                return True

        rec_stack.remove(node)  # Remove node after exploring all neighbors
        visited.add(node)  # Mark node as fully processed

        return False

    for node in range(num_nodes):
        if node not in visited:
            if dfs(node):
                return True

    return False


######################### BFS Kahn's algorithm
# TC : O(V+E)
# SC : O(V)
from collections import deque, defaultdict


def kahn_topological_sort(graph, num_nodes):
    # Step 1: Calculate in-degrees
    indegree = {i: 0 for i in range(num_nodes)}
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    # Step 2: Collect nodes with in-degree 0
    queue = deque([node for node in indegree if indegree[node] == 0])
    topo_sort = []

    # Step 3: Process the queue
    while queue:
        node = queue.popleft()
        topo_sort.append(node)

        # Decrease in-degree for neighbors and add to queue if zero
        for neighbor in graph[node]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    # Step 4: Check if topological sort was possible (cycle detection)
    if len(topo_sort) != num_nodes:
        return "Cycle detected, no valid topological order"

    return topo_sort


#################################################


class Solution:

    # Function to return list containing vertices in Topological order.
    def topologicalSort(self, adj):
        # Code here

        stack = []
        visited = [False for _ in range(len(adj))]

        def dfs(index):
            visited[index] = True

            for i in adj[index]:
                if not visited[i]:
                    dfs(i)
            stack.append(index)

        for j in range(len(adj)):
            if not visited[j]:
                dfs(j)

        return stack[::-1]
