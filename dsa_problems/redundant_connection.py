class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        def path_exists(u, v):
            if u == v:
                return True

            visited.add(u)

            for neighbor in graph[u]:
                if neighbor not in visited:
                    if path_exists(neighbor, v):
                        return True
            return False

        graph = defaultdict(list)

        for u, v in edges:
            visited = set()

            if path_exists(u, v):
                return [u, v]
            else:
                graph[u].append(v)
                graph[v].append(u)
        return
