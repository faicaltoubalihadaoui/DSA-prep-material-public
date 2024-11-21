# matrix = 1 1 8 1
#          3 2 1 2
#          0 2 5 8

# we can use dfs, to reach the depth first of any possible path, once we achieve the base case
# we backtrack going in reverse to maximize the path


def max_path_finder(matrix):

    line = len(matrix)
    column = len(matrix[0])

    def dfs(i, j):
        # BC
        if i == line - 1 and j == column - 1:
            return matrix[i][j], [(i, j)]  # no comparison done, matrix[line][column]

        max_val = 0
        best_path = []

        if i + 1 < line:  # move by line
            max_val_l, best_path_l = dfs(i + 1, j)
            max_val = max(max_val, max_val_l)
            if max_val == max_val_l:
                best_path = best_path_l

        if j + 1 < column:
            max_val_c, best_path_c = dfs(i, j + 1)
            max_val = max(max_val, max_val_c)
            if max_val == max_val_c:
                best_path = best_path_c

        return matrix[i][j] + max_val, [(i, j)] + best_path

    max_val, best_path = dfs(0, 0)
    return max_val, best_path


def max_path_finder_memo(matrix):

    line = len(matrix)
    column = len(matrix[0])

    memo = {}  # Pour chaque i,j => max_value at i,j , best_path

    def dfs_memo(i, j):
        # BC
        if i == line - 1 and j == column - 1:
            return matrix[i][j], [(i, j)]  # no comparison done, matrix[line][column]

        if (i, j) in memo:
            return memo[(i, j)]

        max_val = 0
        best_path = []
        max_val_l, max_val_c = None, None

        if i + 1 < line:
            max_val_l, best_path_l = dfs_memo(i + 1, j)
        if j + 1 < column:
            max_val_c, best_path_c = dfs_memo(i, j + 1)

        if not max_val_l:
            max_val_l = float("-Inf")
        if not max_val_c:
            max_val_c = float("-Inf")

        if max_val_l >= max_val_c:
            max_val = max_val_l + matrix[i][j]
            best_path = [(i, j)] + best_path_l
        else:
            max_val = max_val_c + matrix[i][j]
            best_path = [(i, j)] + best_path_c

        memo[(i, j)] = (max_val, best_path)

        return memo[(i, j)]

    max_val, best_path = dfs_memo(0, 0)
    return max_val, best_path


def max_path_finder_memo_2(matrix):
    if not matrix or not matrix[0]:
        return 0, []

    m, n = len(matrix), len(matrix[0])
    memo = {}  # Cache for memoization

    def dfs(i, j):
        # If out of bounds, return impossible result
        if i >= m or j >= n:
            return float("-inf"), []

        # If reached the bottom-right corner
        if (i, j) == (m - 1, n - 1):
            return matrix[i][j], [(i, j)]

        # If already computed, return from memo
        if (i, j) in memo:
            return memo[(i, j)]

        # Explore right and down paths
        right_sum, right_path = dfs(i, j + 1)
        down_sum, down_path = dfs(i + 1, j)

        # Choose the maximum path
        if right_sum > down_sum:
            max_sum = right_sum + matrix[i][j]
            max_path = [(i, j)] + right_path
        else:
            max_sum = down_sum + matrix[i][j]
            max_path = [(i, j)] + down_path

        # Memoize the result
        memo[(i, j)] = (max_sum, max_path)
        return memo[(i, j)]

    # Start DFS from the top-left corner
    return dfs(0, 0)


max_path_finder([[1, 2, 3], [3, 4, 5]])

assert max_path_finder_memo([[1, 2, 3], [3, 4, 5]]) == (
    13,
    [(0, 0), (1, 0), (1, 1), (1, 2)],
)
assert max_path_finder_memo([[1, 2, 25], [3, 4, 5]]) == (
    33,
    [(0, 0), (0, 1), (0, 2), (1, 2)],
)

assert max_path_finder([[1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]) == (
    5,
    [(0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (4, 1), (4, 2)],
)
assert max_path_finder([[1, 0, 5], [1, 0, 0], [1, 0, 0], [1, 0, 0], [1, 0, 0]]) == (
    6,
    [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2), (3, 2), (4, 2)],
)
assert max_path_finder([[1, 0, 5], [1, 0, 0], [1, 10, 1], [1, 0, 1], [1, 0, 0]]) == (
    15,
    [(0, 0), (1, 0), (2, 0), (2, 1), (2, 2), (3, 2), (4, 2)],
)
