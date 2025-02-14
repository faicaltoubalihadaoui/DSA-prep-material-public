"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
import copy


#################################### BFS ############################################
class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        clones = {node.val: Node(node.val, [])}
        queue = deque([node])
        while queue:
            current = queue.popleft()
            current_clone = clones[current.val]
            for child in current.neighbors:
                if child.val not in clones:
                    clones[child.val] = Node(child.val, [])
                    queue.append(child)
                current_clone.neighbors.append(clones[child.val])

        return clones[node.val]


#################################### DFS ############################################
"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import deque
import copy


class Solution:
    def cloneGraph(self, node: Optional["Node"]) -> Optional["Node"]:
        if not node:
            return None

        cloned = {}

        def dfs(node):
            cloned_node = Node(node.val)
            cloned[cloned_node.val] = cloned_node
            for child in node.neighbors:
                if child.val in cloned:
                    cloned_node.neighbors.append(cloned[child.val])
                else:
                    # clone it first
                    cloned_child = dfs(child)
                    cloned_node.neighbors.append(cloned_child)

            return cloned_node

        return dfs(node)
