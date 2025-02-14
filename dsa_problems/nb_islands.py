######################## DFS ####################################


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def execute_dfs(i, j):
            for x, y in dirs:
                dx = x + i
                dy = y + j
                if (
                    0 <= dx <= (len(grid) - 1)
                    and 0 <= dy <= (len(grid[0]) - 1)
                    and int(grid[dx][dy]) == 1
                ):
                    grid[dx][dy] = 0
                    execute_dfs(dx, dy)

        if not grid:
            return 0

        k = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if int(grid[i][j]) == 1:
                    k += 1
                    grid[i][j] = 0
                    execute_dfs(i, j)

        return k


######################## BFS ####################################

from collections import deque


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def execute_bfs(i, j):
            queue = deque()
            queue.append((i, j))
            while queue:
                a = queue.popleft()
                x_i = a[0]
                y_j = a[1]
                for x, y in dirs:
                    dx = x + x_i
                    dy = y + y_j
                    if (
                        0 <= dx <= len(grid) - 1
                        and 0 <= dy <= len(grid[0]) - 1
                        and int(grid[dx][dy]) == 1
                    ):
                        grid[dx][dy] = 0
                        queue.append((dx, dy))

        if not grid:
            return 0

        k = 0
        n = len(grid)
        m = len(grid[0])
        for i in range(n):
            for j in range(m):
                if int(grid[i][j]) == 1:
                    k += 1
                    grid[i][j] = 0
                    execute_bfs(i, j)

        return k
