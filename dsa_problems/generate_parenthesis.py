class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(tmp, nbr_opened, nbr_closed):
            # Base case: if the current string is valid and complete
            if len(tmp) == 2 * n:
                res.append(tmp)
                return

            # Add '(' if open parentheses can still be used
            if nbr_opened < n:
                backtrack(tmp + "(", nbr_opened + 1, nbr_closed)

            # Add ')' if close parentheses can balance
            if nbr_closed < nbr_opened:
                backtrack(tmp + ")", nbr_opened, nbr_closed + 1)

        # Start the recursion
        backtrack("", 0, 0)
        return res


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []

        def backtrack(nbr_opened, nbr_closed):
            # Base case:
            if nbr_opened == nbr_closed == n:
                res.append("".join(stack))
                return  # the candidate is valid

            if nbr_opened < n:
                stack.append("(")
                backtrack(nbr_opened + 1, nbr_closed)
                stack.pop()  # backtrack

            if nbr_closed < nbr_opened:
                stack.append(")")
                backtrack(nbr_opened, nbr_closed + 1)
                stack.pop()  # backtrack

        backtrack(0, 0)
        return res
