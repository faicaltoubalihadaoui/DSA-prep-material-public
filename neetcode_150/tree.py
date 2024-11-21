class Bst:
    def __init__(self, data=0, left_node=None, right_node=None):
        self.data = data
        self.left_node = left_node
        self.right_node = right_node

    def insert(self, d):
        if self.data == d:
            return False

        elif self.data > d:
            if self.left_node:
                return self.left_node.insert(d)
            else:
                self.left_node = Bst(d)
                return True

        elif self.data < d:
            if self.right_node:
                return self.right_node.insert(d)
            else:
                self.right_node = Bst(d)
                return True
        return False

    def search(self, d, l):
        l.append(self.data)
        if self.data == d:
            return l
        elif self.data > d and self.left_node:
            return self.left_node.search(d, l)
        elif self.data < d and self.right_node:
            return self.right_node.search(d, l)
        else:
            return False

    def preorder(self, l):
        """root => left => right"""
        if self:
            l.append(self.data)
            if self.left:
                self.left.preorder(l)
            if self.right:
                self.right.preorder(l)
        return l

    def inorder(self, l):
        """left => root => right"""
        if self:
            if self.left:
                self.left.inorder(l)
            l.append(self.data)
            if self.right:
                self.right.inorder(l)
        return l

    def postorder(self, l):
        """left => right => root"""
        if self:
            if self.left:
                self.left.postorder(l)
            if self.right:
                self.right.postorder(l)
            l.append(self.data)

            return l


root = Bst(10)
print(root.insert(9))
print(root.insert(11))
print(root.insert(10))
print(root.search(12, []))
