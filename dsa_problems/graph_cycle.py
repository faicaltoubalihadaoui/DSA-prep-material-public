from collections import defaultdict


graph = {0: [1], 1: [2], 2: [0]}  # has cycle

graph_no_cycle = {0: [1], 1: [2], 2: []}  # has no cycle


def cycle_graph_dfs(graph, num_nodes):
    visited = set()
    recursion_stack = set()

    def dfs(node):
        if node in recursion_stack:
            return True
        if node in visited:
            return

        recursion_stack.add(node)
        for neighbor in graph[node]:
            if dfs(neighbor):
                return True

        recursion_stack.remove(node)
        visited.add(node)

        return False

    for node in range(num_nodes):
        if node not in visited:
            if dfs(node):
                return True
    return False


# TC  : O ( v + e ): each node and edge is processed once
# SC  : O ( v )