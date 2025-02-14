class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = float("-inf")

        def dfs(node):
            nonlocal max_sum
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)

            left_sum = max(left_sum, 0)
            right_sum = max(right_sum, 0)

            max_sum = max(max_sum, left_sum + right_sum + node.val)

            return max(left_sum, right_sum) + node.val

        dfs(root)
        return max_sum
