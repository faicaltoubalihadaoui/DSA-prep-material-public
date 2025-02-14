# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        balanced = True

        def dfs(root):
            nonlocal balanced
            if not root:
                return 0

            dfs_left = dfs(root.left)
            dfs_right = dfs(root.right)

            if abs(dfs_right - dfs_left) > 1:
                balanced = False

            return 1 + max(dfs_left, dfs_right)

        dfs(root)
        return balanced


class Solution:
    def calculate_depth(self, root):
        if not root:
            return 0
        return 1 + max(
            self.calculate_depth(root.left), self.calculate_depth(root.right)
        )

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left_depth = self.calculate_depth(root.left)
        right_depth = self.calculate_depth(root.right)
        if abs(right_depth - left_depth) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)
