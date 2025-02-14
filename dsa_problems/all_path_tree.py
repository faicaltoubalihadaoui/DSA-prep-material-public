class Solution:
    def Paths(self, root):
        # code here  TC O(n)   SP O(h)
        ans = []

        def traverse_tree(root, path):
            if not root:
                return

            path.append(root.data)

            if not root.left and not root.right:
                ans.append(path[:])

            traverse_tree(root.left, path)
            traverse_tree(root.right, path)
            path.pop()

        traverse_tree(root, [])
        return ans


class Solution:
    def Paths(self, root):
        if not root:
            return []

        stack = [(root, [root.data])]
        ans = []

        while stack:
            node, path = stack.pop()

            # If it's a leaf node, store the path
            if not node.left and not node.right:
                ans.append(path)

            # Add right and left children to the stack
            if node.right:
                stack.append((node.right, path + [node.right.data]))
            if node.left:
                stack.append((node.left, path + [node.left.data]))

        return ans
