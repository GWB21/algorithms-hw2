from graphviz import Digraph


class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def __repr__(self):
        return f"Node with value {self.value}"


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert(self.root, value)

    def _insert(self, root, value):
        if root is None:
            return Node(value)

        if value < root.value:
            root.left_child = self._insert(root.left_child, value)
        elif value > root.value:
            root.right_child = self._insert(root.right_child, value)

        return root

    def visualize(self, filename='tree'):
        dot = Digraph(comment='Binary Search Tree')
        self._add_nodes(dot, self.root)
        dot.render(filename, format='png', cleanup=True)

    def _add_nodes(self, dot, root):
        if root:
            dot.node(str(root.value))
            if root.left_child:
                dot.edge(str(root.value), str(root.left_child.value), label='L')
                self._add_nodes(dot, root.left_child)
            if root.right_child:
                dot.edge(str(root.value), str(root.right_child.value), label='R')
                self._add_nodes(dot, root.right_child)


tree = BinarySearchTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(4)
tree.insert(6)

tree.visualize('bst1')