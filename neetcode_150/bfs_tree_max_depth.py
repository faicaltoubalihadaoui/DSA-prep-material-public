# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        stack = [root]
        depth = 1
        while stack:
            elements = []
            while stack:
                to_remove = stack.pop()
                if to_remove:
                    if to_remove.left:
                        elements.append(to_remove.left)
                    if to_remove.right:
                        elements.append(to_remove.right)
            if elements:
                depth += 1
            stack = elements
        return depth


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        q = deque()
        q.append(root)
        depth = 0

        while q:
            depth += 1

            for _ in range(len(q)):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return depth
