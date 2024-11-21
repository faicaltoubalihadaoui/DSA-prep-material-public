# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True

        stack = []
        pre = None
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            if pre and root.val <= pre.val:
                return False
            pre = root
            root = root.right
        return True


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        prev = float("-inf")

        def inorder(node):
            nonlocal prev
            if not node:
                return True
            if not (inorder(node.left) and prev < node.val):
                return False
            prev = node.val
            return inorder(node.right)

        return inorder(root)


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def validate_tree(tree, min_tree, max_tree):
            if not tree:
                return True
            elif not (tree.val < max_tree and min_tree < tree.val):
                return False
            return validate_tree(tree.left, min_tree, tree.val) and validate_tree(
                tree.right, tree.val, max_tree
            )

        return validate_tree(root, float("-Inf"), float("+Inf"))
