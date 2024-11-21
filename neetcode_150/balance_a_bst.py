# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return TreeNode()

        sorted_array = []

        def inorder(root):
            if not root:
                return
            inorder(root.left)
            sorted_array.append(root.val)
            inorder(root.right)

        inorder(root)

        def build_tree(sorted_array):
            if not sorted_array:
                return None

            start = len(sorted_array) // 2
            node = TreeNode(sorted_array[start])
            node.left = build_tree(sorted_array[:start])
            node.right = build_tree(sorted_array[start + 1 :])
            return node

        return build_tree(sorted_array)
