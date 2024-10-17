# from graphviz import Digraph
from statistics import median


class BSTNode:
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent
        self.left = None
        self.right = None
        self.height = 0

    def __repr__(self):
        return f"Node with value {self.value}"

    def insert(self, node):
        if node is None:
            return
        else:
            if node.value < self.value:
                if self.left is None:
                    self.left = node
                    node.parent = self
                else:
                    self.left.insert(node)
            else:
                if self.right is None:
                    self.right = node
                    self.right.parent = self
                else:
                    self.right.insert(node)


def update_height(node):
    while node is not None:
        node.height = max(height(node.left) , height(node.right)) + 1
        node = node.parent
def height(node):
    if node is None:
        return -1
    else:
        return node.height

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        node = BSTNode(value, None)

        if self.root is None:
            self.root = node
        else:
            self.root.insert(node)

        update_height(node)
        return node

    # def visualize(self, filename='tree'):
    #     dot = Digraph(comment='Binary Search Tree')
    #     self._add_nodes(dot, self.root)
    #     dot.render(filename, format='png', cleanup=True)
    #
    # def _add_nodes(self, dot, root):
    #     if root:
    #         dot.node(str(root.value))
    #         if root.left:
    #             dot.edge(str(root.value), str(root.left.value), label='L')
    #             self._add_nodes(dot, root.left)
    #         if root.right:
    #             dot.edge(str(root.value), str(root.right.value), label='R')
    #             self._add_nodes(dot, root.right)


def check_balance(node):
    if node is None:
        return "True it's balanced"

    # left_height = node.left.height if node.left else 0
    # right_height = node.right.height if node.right else 0

    left_right_height_diff = abs(height(node.left) - height(node.right))

    if left_right_height_diff >= 2:
        return "False it's not balanced"

    return check_balance(node.left) and check_balance(node.right)

class AVL(BinarySearchTree):
    def __init__(self):
        super().__init__()
        self.rot_count = 0

    def left_rotate(self, node):
        x = node
        y = x.right
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.right = y.left
        if x.right is not None:
            x.right.parent = x
        y.left = x
        x.parent = y
        update_height(x)
        update_height(y)
        print("left rotate 발생")
        self.rot_count += 1

    def right_rotate(self, node):          #right Rotate
        x = node
        y = x.left
        y.parent = x.parent
        if y.parent is None:
            self.root = y
        else:
            if y.parent.left is x:
                y.parent.left = y
            elif y.parent.right is x:
                y.parent.right = y
        x.left = y.right
        if x.left is not None:
            x.left.parent = x
        y.right = x
        x.parent = y
        update_height(x)
        update_height(y)
        print("right rotate 발생")
        self.rot_count += 1

    def rebalanced(self, node):   # x가 처음으로 규칙을 위반했을때 => AVL 트리 property 안지켜졌을때 rebalance하는 (메인코드네) 그니까 insert 할때마다 rebalance해주는거라 rotate는 최대 2번임.
        rot_count = 0
        while node is not None:
            if height(node.left) >= 2 + height(node.right):
                if height(node.left.left) >= height(node.left.right):  # 이건 왼쪽으로 치우쳐진 경우중 일직선일때는 right rotate 한번만 해도 되는것임.
                    self.right_rotate(node)
                else:  # 왼쪽 치우쳐진 경우중 zigzag일때 left rotate후 right rotate.
                    self.left_rotate(node.left)
                    self.right_rotate(node)
            elif height(node.right) >= 2 + height(node.left):  # 걍 반대. 오른쪽으로 치우쳐진 경우임.
                if height(node.right.right) >= height(node.right.left):
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right)
                    self.left_rotate(node)

            update_height(node)
            node = node.parent

    def insert(self, k):
        node = super(AVL, self).insert(k)
        self.rebalanced(node)

tree = AVL()
for i in range (1, 16):
    tree.insert(i)
print(tree.rot_count)


