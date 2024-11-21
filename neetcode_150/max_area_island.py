class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        max_area = 0

        def dfs(r, c):
            if min(r, c) < 0 or r == ROWS or c == COLS or grid[r][c] == 0:
                return 0
            grid[r][c] = 0
            return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(ROWS):
            for c in range(COLS):
                max_area = max(max_area, dfs(r, c))
        return max_area


from collections import deque


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def execute_bfs(i, j):
            queue = deque()
            queue.append((i, j))
            local_surface = 1
            while queue:
                node = queue.popleft()
                for x, y in dirs:
                    dx = x + node[0]
                    dy = y + node[1]
                    if (
                        0 <= dx <= len(grid) - 1
                        and 0 <= dy <= len(grid[0]) - 1
                        and grid[dx][dy] == 1
                    ):
                        local_surface += 1
                        grid[dx][dy] = 0
                        queue.append((dx, dy))
            return local_surface

        max_area = 0
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    grid[i][j] = 0
                    island_surface = execute_bfs(i, j)
                    max_area = island_surface if island_surface > max_area else max_area
        return max_area
