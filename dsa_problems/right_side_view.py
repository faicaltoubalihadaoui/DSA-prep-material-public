# Level order traversal
def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
    if not root:
        return []

    queue = deque()
    queue.append(root)
    ans = []
    while queue:
        ans.append(queue[-1].val)
        for _ in range(len(queue)):
            node = queue.popleft()
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
    return ans
