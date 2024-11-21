# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root or not k:
            return -1

        stack = []
        result = []
        count = 1
        while root or stack:
            while root:
                stack.append(root)
                root = root.left
            e = stack.pop()
            if count == k:
                return e.val
            else:
                count += 1
            root = e.right

        return -1


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        self.count = 0
        self.result = None

        def inorder(node):
            if not node or self.result is not None:
                return

            inorder(node.left)
            self.count += 1

            if self.count == k:
                self.result = node.val
                return  # Stop the recursion

            inorder(node.right)

        inorder(root)

        return self.result
