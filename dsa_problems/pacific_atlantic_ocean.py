## DFS
def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
    if not matrix:
        return []
    p_land = set()
    a_land = set()
    R, C = len(matrix), len(matrix[0])

    def dfs(i, j, land):
        land.add((i, j))
        for x, y in ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)):
            if (
                0 <= x < R
                and 0 <= y < C
                and matrix[x][y] >= matrix[i][j]
                and (x, y) not in land
            ):
                dfs(x, y, land)

    for i in range(R):
        dfs(i, 0, p_land)
        dfs(i, C - 1, a_land)
    for j in range(C):
        dfs(0, j, p_land)
        dfs(R - 1, j, a_land)
    return list(p_land & a_land)


### DFS 2


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []

        l = len(heights)
        c = len(heights[0])
        set_pacific = set()
        set_atlantic = set()
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs_pacific(i, j):
            set_pacific.add((i, j))
            for di, dj in dirs:
                dx = di + i
                dy = dj + j
                if (
                    0 <= dx < l
                    and 0 <= dy < c
                    and (dx, dy) not in set_pacific
                    and heights[dx][dy] >= heights[i][j]
                ):
                    dfs_pacific(dx, dy)

        def dfs_atlantic(i, j):
            set_atlantic.add((i, j))
            for di, dj in dirs:
                dx = di + i
                dy = dj + j
                if (
                    0 <= dx < l
                    and 0 <= dy < c
                    and (dx, dy) not in set_atlantic
                    and heights[dx][dy] >= heights[i][j]
                ):
                    dfs_atlantic(dx, dy)

        for i in range(l):
            dfs_pacific(i, 0)
            dfs_atlantic(i, c - 1)

        for j in range(c):
            dfs_pacific(0, j)
            dfs_atlantic(l - 1, j)

        ans = [[i, j] for (i, j) in set_atlantic if (i, j) in set_pacific]
        return ans


## BFS
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        m, n = len(matrix), len(matrix[0])
        pacific = [(0, i) for i in range(n)] + [(i, 0) for i in range(1, m)]
        atlantic = [(m - 1, i) for i in range(n)] + [(i, n - 1) for i in range(m - 1)]

        def bfs(q):
            visited = set()
            q = collections.deque(q)
            while q:
                i, j = q.popleft()
                visited.add((i, j))
                for ii, jj in map(
                    lambda x: (x[0] + i, x[1] + j), [(-1, 0), (1, 0), (0, -1), (0, 1)]
                ):
                    if (
                        0 <= ii < m
                        and 0 <= jj < n
                        and (ii, jj) not in visited
                        and matrix[ii][jj] >= matrix[i][j]
                    ):
                        q.append((ii, jj))
            return visited

        return bfs(pacific) & bfs(atlantic)
