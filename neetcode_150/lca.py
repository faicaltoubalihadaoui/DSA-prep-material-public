def lowestCommonAncestor(
    self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
) -> "TreeNode":

    if root is None:
        return None

    if root.val > p.val and root.val > q.val:
        return self.lowestCommonAncestor(root.left, p, q)

    if root.val < p.val and root.val < q.val:
        return self.lowestCommonAncestor(root.right, p, q)

    return root


class Solution:
    def lowestCommonAncestor(
        self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
    ) -> "TreeNode":

        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root


def lowestCommonAncestor(
    self, root: "TreeNode", p: "TreeNode", q: "TreeNode"
) -> "TreeNode":

    def is_ancestor(root, p):
        if not root:
            return False
        elif root and root.val == p.val:
            return True
        return is_ancestor(root.left, p) or is_ancestor(root.right, p)

    if not root:
        return None
    if root == p or root == q:
        return root

    p_left = is_ancestor(root.left, p)
    q_left = is_ancestor(root.left, q)
    if p_left != q_left:
        return root
    next_subtree = root.left if p_left else root.right
    return self.lowestCommonAncestor(next_subtree, p, q)
