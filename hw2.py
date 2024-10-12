from graphviz import Digraph

from avl import update_height


class Node:
    def __init__(self, value):
        self.height = 0
        self.value = value
        self.left_child = None
        self.right_child = None


    def __repr__(self):
        return f"Node with value {self.value}"

    def height(self):
        return self.height

    def update_height(self):
        left_height = self.left_child.height() if self.left_child else -1
        right_height = self.right_child.height() if self.right_child else -1
        self.height = max(left_height, right_height) + 1

    def check_balanced(self):
        left_height = self.left_child.get_height() if self.left_child else -1
        right_height = self.right_child.get_height() if self.right_child else -1

        height_diff = abs(left_height - right_height)

        if height_diff > 1:
            return False
        if self.left_child:
            self.left_child.check_balanced()
        if self.right_child:
            self.right_child.check_balanced()
        return True


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

        root.update_height()
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

    def check_balanced(self):
        if not self.root:
            return True  # 트리가 비어있는 경우 균형을 이룬 것으로 간주
        return self.root.check_balanced()



tree = BinarySearchTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(4)
tree.insert(6)

tree.visualize('bst1')