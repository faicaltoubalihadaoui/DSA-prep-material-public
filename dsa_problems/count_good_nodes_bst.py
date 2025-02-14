# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        
        count = 1
        def dfs(node, path):
            nonlocal count
            if not node:
                return 
            
            if path and max(path) <= node.val:
                count +=1

            path.append(node.val)
            
            dfs(node.left, path)
            dfs(node.right, path)

            path.pop() # backtrack


        dfs(root, [])
        return count

# call stack
# 3 
        
        
 # Intuition :
# at each node, we should have the list of path to it, and then compare its value to the one in the path