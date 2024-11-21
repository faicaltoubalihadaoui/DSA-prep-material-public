from collections import deque


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        if not grid:
            return -1

        increment = 0
        visited = set()
        l = len(grid)
        c = len(grid[0])
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        queue = deque()
        fresh_oranges = 0
        for i in range(l):
            for j in range(c):
                if grid[i][j] == 2:
                    queue.append((i, j))
                elif grid[i][j] == 1:
                    fresh_oranges += 1

        if fresh_oranges == 0:
            return 0

        while queue:
            for _ in range(len(queue)):
                x, y = queue.popleft()
                for dx, dy in dirs:
                    nx, ny = dx + x, dy + y
                    if 0 <= nx < l and 0 <= ny < c and grid[nx][ny] == 1:
                        grid[nx][ny] = 2
                        queue.append((nx, ny))
                        fresh_oranges -= 1
            if queue:
                increment += 1

        return increment if fresh_oranges == 0 else -1
