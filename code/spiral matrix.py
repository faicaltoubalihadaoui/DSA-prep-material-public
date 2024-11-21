class Solution:
    # Function to return a list of integers denoting spiral traversal of matrix.
    def spirallyTraverse(self, mat):
        n = len(mat)       # Number of rows
        m = len(mat[0])    # Number of columns
        i, j = 0, 0        # Initial indices for top-left corner
        m_l = []           # Result list to store the spiral order
        
        while i < n and j < m:
            # Traverse the top row (left to right)
            for m_j in range(j, m):
                m_l.append(mat[i][m_j])

            # Traverse the right column (top to bottom)
            for m_i in range(i + 1, n):
                m_l.append(mat[m_i][m-1])

            # Traverse the bottom row (right to left)
            if i < n - 1:  # Ensure there is still a row to traverse
                for m_n in range(m - 2, j - 1, -1):
                    m_l.append(mat[n-1][m_n])

            # Traverse the left column (bottom to top)
            if j < m - 1:  # Ensure there is still a column to traverse
                for m_m in range(n - 2, i, -1):
                    m_l.append(mat[m_m][j])

            # Move boundaries inward after the loop
            i += 1
            j += 1
            n -= 1
            m -= 1

        return m_l
