from collections import defaultdict


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # whenever we are asked an order for a DAG graph ( directed and acylic graph ) we need to think of topological sorting

        graph = defaultdict()
        for i, j in prerequisites:
            if i in graph:
                graph[i].append(j)
            else:
                graph[i] = [j]

        def topological_sort(graph):
            visited = set()
            recursion_stack = set()
            stack = []

            def dfs(node):
                if node in recursion_stack:
                    return True
                if node in visited:
                    return  # already processed node

                recursion_stack.add(node)
                if node in graph:
                    for neighbor in graph[node]:
                        if dfs(neighbor):
                            return True
                stack.append(node)
                recursion_stack.remove(node)
                visited.add(node)
                return False

            for element in range(numCourses):
                if element not in visited:
                    if dfs(element):  # has cycle
                        return []  # impossible to finish all courses
            return stack

        return topological_sort(graph)
