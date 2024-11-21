# Clean Solution : Intuition We can't have two candidates , matrice carré meaning len(mat) == len(mat[0])

class Solution:
    def celebrity(self, mat):
        if not mat or not mat[0]:
            return -1

        n = len(mat)
        # Step 1: Find the potential celebrity
        candidate = 0
        for i in range(1, n):
            if mat[candidate][i] == 1:  # Candidate knows i, so candidate cannot be a celebrity
                candidate = i

        # Step 2: Verify the candidate
        for i in range(n):
            if i != candidate:
                # Candidate should not know i, and everyone should know the candidate
                if mat[candidate][i] == 1 or mat[i][candidate] == 0:
                    return -1

        return candidate




# Mine
class Solution:
    def celebrity(self, mat):
        # code here
        if not mat:
            return -1
        
        stack = []
        def populate_candidates(mat):
            for i in range(len(mat)):
                can = True
                for j in range(len(mat[0])):
                    if mat[i][j] != 0:
                        can = False
                        break
                if can: stack.append(i)    
        
        
        populate_candidates(mat)
        if not stack: return -1
        
        while stack:
            can = stack.pop()
            can_bool = True
            for j in range(len(mat[0])):
                if j != can and mat[j][can] != 1:
                    can_bool = False
                    break
            if can_bool:
                return can
        return -1