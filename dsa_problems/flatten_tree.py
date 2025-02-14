# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return TreeNode()
        elif root and not root.right and not root.left:
            return root

        def dfs(node):
            if not node:
                return

            dfs(node.left)
            dfs(node.right)

            pointer_right = node.right
            node.right = node.left
            node.left = None

            current = node
            while current.right:
                current = current.right
            current.right = pointer_right

        dfs(root)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return TreeNode()
        elif root and not root.right and not root.left:
            return root

        prev = None

        def dfs(node):
            nonlocal prev
            if not node:
                return

            dfs(node.right)
            dfs(node.left)

            node.right = prev
            node.left = None
            prev = node

        dfs(root)
