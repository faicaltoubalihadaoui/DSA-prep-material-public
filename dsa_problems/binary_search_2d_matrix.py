# O( log(mn) )
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        def row_binary_search(row, target):
            low = 0
            right = len(row) - 1
            while low <= right:
                middle = (low + right) // 2
                if row[middle] == target:
                    return True
                elif row[middle] > target:
                    right = middle - 1
                else:
                    low = middle + 1
            return False

        if not matrix:
            return False
        nb_rows = len(matrix)
        nb_col = len(matrix[0])

        upper = 0
        bottom = nb_rows - 1
        while upper <= bottom:
            mid = (upper + bottom) // 2
            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return row_binary_search(matrix[mid], target)
            elif target > matrix[mid][-1]:
                upper = mid + 1
            else:
                bottom = mid - 1

        return False


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        left, right = 0, rows * cols - 1

        while left <= right:
            mid = (left + right) // 2
            row, col = mid // cols, mid % cols
            guess = matrix[row][col]

            if guess == target:
                return True
            elif guess < target:
                left = mid + 1
            else:
                right = mid - 1

        return False
