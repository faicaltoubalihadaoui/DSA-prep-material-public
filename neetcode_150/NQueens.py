class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        matrix = [["." for _ in range(n)] for _ in range(n)]
        ans = []

        def build_matrix(start, curr_matrix):
            if start == n:
                copy = ["".join(row) for row in curr_matrix]
                ans.append(copy)
                return

            for k in range(n):
                if check_validity_step(start, k, curr_matrix):
                    curr_matrix[start][k] = "Q"
                    build_matrix(start + 1, curr_matrix)
                    curr_matrix[start][k] = "."

        def check_validity_step(i, j, curr_matrix):
            row = i - 1
            while row >= 0:
                if curr_matrix[row][j] == "Q":
                    return False
                row -= 1

            row = i - 1
            col = j - 1
            while row >= 0 and col >= 0:
                if curr_matrix[row][col] == "Q":
                    return False
                row -= 1
                col -= 1

            row = i - 1
            col = j + 1
            while row >= 0 and col <= n - 1:
                if curr_matrix[row][col] == "Q":
                    return False
                row -= 1
                col += 1
            return True

        build_matrix(0, matrix)
        return ans  # contrains matrices
