from graphviz import Digraph


class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.height = 0  # 노드의 높이는 0으로 초기화

    def __repr__(self):
        return f"Node with value {self.value}"

    def get_height(self):
        # 높이를 반환하는 메서드
        return self.height

    def update_height(self):
        # 자식 노드가 None인 경우를 처리하여 높이 업데이트
        left_height = self.left_child.get_height() if self.left_child else -1
        right_height = self.right_child.get_height() if self.right_child else -1
        self.height = max(left_height, right_height) + 1

    def check_balanced(self):
        # 현재 노드의 균형 상태 체크
        left_height = self.left_child.get_height() if self.left_child else -1
        right_height = self.right_child.get_height() if self.right_child else -1

        height_diff = abs(left_height - right_height)

        if height_diff > 1:
            return False

        # 왼쪽과 오른쪽 자식의 균형 상태 체크
        left_balanced = self.left_child.check_balanced() if self.left_child else True
        right_balanced = self.right_child.check_balanced() if self.right_child else True

        return left_balanced and right_balanced


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

        root.update_height()  # 노드의 높이를 업데이트
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


# 트리 생성 및 테스트
tree = BinarySearchTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(1)
tree.insert(4)
tree.insert(6)

tree.visualize('bst1')

# 트리가 AVL 트리인지 확인
print(tree.check_balanced())  # True라면 AVL 트리, False라면 불균형
