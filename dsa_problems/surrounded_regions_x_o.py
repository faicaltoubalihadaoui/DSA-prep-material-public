class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        l = len(board)
        c = len(board[0])
        visited = set()

        def dfs(i, j):
            for dx, dy in dirs:
                nx, ny = dx + i, dy + j
                if (
                    0 <= nx < l
                    and 0 <= ny < c
                    and (nx, ny) not in visited
                    and board[nx][ny] == "O"
                ):
                    visited.add((nx, ny))
                    dfs(nx, ny)

        # n
        for i in range(l):
            for j in [0, c - 1]:
                if board[i][j] == "O" and (i, j) not in visited:
                    visited.add((i, j))
                    dfs(i, j)
        # m
        for j in range(c):
            for i in [0, l - 1]:
                if board[i][j] == "O" and (i, j) not in visited:
                    visited.add((i, j))
                    dfs(i, j)
        # n * m
        for i in range(l):
            for j in range(c):
                if board[i][j] == "O" and (i, j) not in visited:
                    board[i][j] = "X"


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        l = len(board)
        c = len(board[0])
        regions = []
        visited = set()

        def dfs(i, j, region_candidate):
            visited.add((i, j))
            region_candidate.add((i, j))
            if board[i][j] == "O" and (i == 0 or i == l - 1 or j == 0 or j == c - 1):
                return False
            for dx, dy in dirs:
                if (
                    0 <= dx + i < l
                    and 0 <= dy + j < c
                    and (dx + i, dy + j) not in region_candidate
                    and board[dx + i][dy + j] == "O"
                ):
                    if not (dfs(dx + i, dy + j, region_candidate)):
                        return False
            return True

        for i in range(l):
            for j in range(c):
                if board[i][j] == "O" and (i, j) not in visited:
                    region_candidate = set()
                    is_candidate = dfs(i, j, region_candidate)
                    if is_candidate:
                        regions.append(region_candidate)

        for region in regions:
            for couple in region:
                board[couple[0]][couple[1]] = "X"

        return board
