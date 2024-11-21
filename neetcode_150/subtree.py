# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        if not subRoot and root:
            return True
        elif not root and subRoot:
            return False
        elif self.is_same_tree(root, subRoot):
            return True

        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def is_same_tree(self, s, t):
        if not s and not t:
            return True
        elif not s or not t:
            return False
        elif s.val == t.val:
            return self.is_same_tree(s.left, t.left) and self.is_same_tree(
                s.right, t.right
            )

        return False
