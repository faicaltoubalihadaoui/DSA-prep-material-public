from collections import defaultdict


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # we need to look if there is a cycle in the graph
        if not prerequisites:
            return True

        graph = defaultdict()
        for a, b in prerequisites:
            if a in graph:
                graph[a].append(b)
            else:
                graph[a] = [b]

        visited = set()
        recursion_stack = set()

        def dfs(node):
            if node in recursion_stack:
                return True  # cycle detected
            if node in visited:
                return  # was already visited

            recursion_stack.add(node)
            if node in graph:
                for neighbor in graph[node]:
                    if dfs(neighbor):
                        return True

            recursion_stack.remove(node)
            visited.add(node)
            return False

        for course in range(numCourses):
            if course not in visited:
                if dfs(course):
                    return False
        return True
