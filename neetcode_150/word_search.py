class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:
            return False

        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        def execute_dfs(i, j, word):
            if not word:
                return True

            temp, board[i][j] = board[i][j], "#"
            for dx, dy in dirs:
                nx = dx + i
                ny = dy + j
                if 0 <= nx <= n - 1 and 0 <= ny <= m - 1 and board[nx][ny] == word[0]:
                    if execute_dfs(nx, ny, word[1:]):
                        return True
            board[i][j] = temp
            return False

        n = len(board)
        m = len(board[0])
        for i in range(n):
            for j in range(m):
                if board[i][j] == word[0]:
                    if execute_dfs(i, j, word[1:]):
                        return True
        return False
