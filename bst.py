import random
import sys

class BSTNode:
    """A node in the vanilla BST tree."""

    #bst의 node가 가지고 있는 값들을 설정하는것.
    def __init__(self, parent, k):
        """Creates a node.

        Args:
            parent: The node's parent.
            k: key of the node.
        """
        self.key = k
        self.parent = parent
        self.left = None
        self.right = None

    def find(self, k):
        """Finds and returns the node with key k from the subtree rooted at this
        node.

        Args:
            k: The key of the node we want to find.

        Returns:
            The node with key k.
        """
        #내가 찾고 싶은 노드를 key를 통해서 찾는 알고리즘.
        # 매개변수 k가 self.key이면 바로 자기 자신인거고.
        if k == self.key:
            return self

        # k가 자기 key보다 작다면 자기 left로 찾아 내려가서(있다면) 재귀 (없다면) 뭐 error인거지 내가 찾는 k가 없는거지.
        elif k < self.key:
            if self.left is None:
                return None
            else:
                return self.left.find(k)

        # k가 크다면 자기 right로 찾아내려가는 것이고.
        else:
            if self.right is None:
                return None
            else:
                return self.right.find(k)

    def find_min(self):
        """Finds the node with the minimum key in the subtree rooted at this
        node.

        Returns:
            The node with the minimum key.
        """
        current = self
        while current.left is not None:
            current = current.left
        return current              #아 bst에서 작은건 계속 왼쪽꺼니까 왼쪽으로 계속 찾아서 내려가는거구나 subtree에서 가장 작은 노드를 찾고싶어서?

    def next_larger(self):          #해당 노드에서 다음으로 큰 값을 찾는다는것은 자신의 right child중 가장 작은 친구를 찾는것 그러니 오른쪽 child에 대한 findmin 수행하면 됨.
        """Returns the node with the next larger key (the successor) in the BST.
        """
        if self.right is not None:          #해당 노드에서 다음으로 큰 값을 찾는다는것은 자신의 right child중 가장 작은 친구를 찾는것 그러니 오른쪽 child에 대한 findmin 수행하면 됨.
            return self.right.find_min()

        current = self                       #right child가 None이라면 next larger은 left child를 가지는 첫번재 parent이다!!
        while current.parent is not None and current is current.parent.right:
            current = current.parent
        return current.parent

    def insert(self, node):         #한 node를 삽입하는 알고리즘.
        """Inserts a node into the subtree rooted at this node.

        Args:
            node: The node to be inserted.
        """
        if node is None:    #node가 None이면 insert 할 것 자체가 없는데.. 걍 end
            return
        if node.key < self.key:     #None이 아니라는것이므로 진행. key값을 통해서 배치하기. key값이 더 작다면 왼쪽으로 가야하고. 없다면 바로 배치 있다면 left child에 대한 재귀 진행
            if self.left is None:
                node.parent = self
                self.left = node
            else:
                self.left.insert(node)
        else:                       #큰 경우 => right쪽으로 똑같이 진행
            if self.right is None:
                node.parent = self
                self.right = node
            else:
                self.right.insert(node)

    def delete(self):                #삭제하기..
        """Deletes and returns this node from the BST."""
        if self.left is None or self.right is None:     #일단 full child가 아닌경우를 control하는것.
            if self is self.parent.left:                # 그 경우에 self 가 parent의 left child인지 right child인지 가 중요함.
                self.parent.left = self.left or self.right  #만약 self가 left child라면, self의 left child던 right child던 parent의 left에 가져다가 붙인다. 여기는 하나 이하만 붙음. 왜냐? 애초에 full child가 아닌경우를 control하는것이기 때문.
                if self.parent.left is not None:        # 연결했는데 그 child가 None이 아니라면, => self의 left던 right던 하나가 딱 붙었으면?
                    self.parent.left.parent = self.parent   # self의 그 child는 parent가 self라고 생각할 것 이기 때문에 linking을 이제 self의 parent로 변경하는것 => 이렇게 되면 이제 self는 child랑 parent가 누구인지는 가지고 있지만, 더이상 다른 노드에서 self를 참조하지 않음
            else:                                       #right의 경우에도 똑같이 실행하면 되는거고.
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
            return self
        else:                                           #근데 만약 left랑 right가 둘 다 있어. 그러면 내 자리에 left를 넣을지 right를 넣을지가 고민되겠지?
            s = self.next_larger()                      #무조건 left아니면 right를 넣는거야? 아냐 right 중에서도 가장 왼쪽 leaf노드가 들어가야겠지. 왜나면 그게 들어가야 bst property가 유지되니까.
            self.key, s.key = s.key, self.key           #그걸 찾았으면 그냥 단순히 self node랑 next_larger node의 key만 바꾸면 되는거야. key라는것은 노드가 가지고 있는 값을 의미하는것임. 트리 구조를 변경하지 않고 그저 값만 변경하면 되는거니까. 매우 편리하지. 막 복잡한 pointer 변경 하지 않아도 되는거니까.
            return s.delete()                           #key값만 변경하고 나면 삭제하면 되는거겠지. 왜냐? right child를 가지고 있을때의 next larger node는 무조건 ? leaf 노드이니까.
        # if self.left and self.right:  # 둘 다 자식이 있는 경우
        #     s = self.next_larger()  # 오른쪽 서브트리에서 가장 작은 노드를 찾음
        #     self.key, s.key = s.key, self.key  # self와 next_larger 노드의 키 값만 교환
        #     return s.delete()  # next_larger 노드를 삭제 (재귀적으로 처리)
        #
        #     # 자식이 하나만 있거나 없는 경우 처리
        # if self is self.parent.left:  # self가 부모의 왼쪽 자식인 경우
        #     self.parent.left = self.left or self.right  # 자식 중 존재하는 것을 부모의 왼쪽에 연결
        # else:  # self가 부모의 오른쪽 자식인 경우
        #     self.parent.right = self.left or self.right  # 자식 중 존재하는 것을 부모의 오른쪽에 연결
        #
        #     # 자식이 있을 경우 그 자식의 부모를 업데이트
        # if self.left or self.right:
        #     (self.left or self.right).parent = self.parent
        #
        # return self  # self 노드를 반환

    def check_ri(self):                 #### 해당 노드가 bst의 property를 지키고 있는지 check하는 함수.
        """Checks the BST representation invariant around this node.

        Raises an exception if the RI is violated.
        """
        if self.left is not None:           ###일단 child가 없으면 무조건 property는 지키고 있다는거고. ㅋㅋㅋ
            if self.left.key > self.key:        ###만약 left 가 자신보다 크면 ? => 오류
                raise RuntimeError("BST RI violated by a left node key")
            if self.left.parent is not self:        ###만약 left의 parent pointer가 self가 아니라면? 그것도 이상한거고. => 무결성 유지 위한 방어적 프로그래밍.
                raise RuntimeError("BST RI violated by a left node parent "
                                   "pointer")
            self.left.check_ri()                    ### 내 child가 porperty를 지키지 못하고 있다면 나도 못 지키고 있는거니까 검사해봐야겠죠? => 재귀
        if self.right is not None:                  ### right에 대해서도 똑같은 알고리즘 돌리기.
            if self.right.key < self.key:
                raise RuntimeError("BST RI violated by a right node key")
            if self.right.parent is not self:
                raise RuntimeError("BST RI violated by a right node parent "
                                   "pointer")
            self.right.check_ri()

    def _str(self):
        """Internal method for ASCII art."""
        label = str(self.key)
        if self.left is None:
            left_lines, left_pos, left_width = [], 0, 0
        else:
            left_lines, left_pos, left_width = self.left._str()
        if self.right is None:
            right_lines, right_pos, right_width = [], 0, 0
        else:
            right_lines, right_pos, right_width = self.right._str()
        middle = max(right_pos + left_width - left_pos + 1, len(label), 2)
        pos = left_pos + middle // 2
        width = left_pos + middle + right_width - right_pos
        while len(left_lines) < len(right_lines):
            left_lines.append(' ' * left_width)
        while len(right_lines) < len(left_lines):
            right_lines.append(' ' * right_width)
        if (middle - len(label)) % 2 == 1 and self.parent is not None and \
                self is self.parent.left and len(label) < middle:
            label += '.'
        label = label.center(middle, '.')
        if label[0] == '.': label = ' ' + label[1:]
        if label[-1] == '.': label = label[:-1] + ' '
        lines = [' ' * left_pos + label + ' ' * (right_width - right_pos),
                 ' ' * left_pos + '/' + ' ' * (middle - 2) +
                 '\\' + ' ' * (right_width - right_pos)] + \
                [left_line + ' ' * (width - left_width - right_width) + right_line
                 for left_line, right_line in zip(left_lines, right_lines)]
        return lines, pos, width

    def __str__(self):
        return '\n'.join(self._str()[0])

#이 코드는 MinBSTNode라는 클래스를 정의하고 있습니다. 이 클래스는 기본 BSTNode를 확장하여 각 노드에서 해당 서브트리의 최소 키를 추적하는 기능을 추가한 것입니다. 주요 특징은 다음과 같습니다:
# 최소값 추적:
# 각 노드는 self.min이라는 속성을 가지며, 이는 해당 노드를 루트로 하는 서브트리에서 가장 작은 키를 가진 노드를 가리킵니다.
# 삽입 시 최소값 업데이트:
# 새 노드를 삽입할 때, 해당 노드의 키가 현재 서브트리의 최소값보다 작으면 self.min을 업데이트합니다.
# 삭제 시 최소값 조정:
# 노드를 삭제할 때, 최소값 노드가 변경될 수 있으므로 이를 적절히 조정합니다.
# 삭제된 노드가 왼쪽 자식이었다면, 부모 노드부터 시작해 트리를 위로 올라가며 min 값을 재조정합니다.
# 효율적인 최소값 찾기:
# find_min() 메서드를 통해 O(1) 시간에 서브트리의 최소값을 찾을 수 있습니다.
# 기본 BST 연산 유지:
# 기본적인 BST의 삽입, 삭제 연산을 유지하면서 최소값 추적 기능을 추가했습니다.
# 이 구현의 주요 이점은 각 노드에서 해당 서브트리의 최소값을 즉시 알 수 있다는 것입니다. 이는 특정 연산(예: 범위 쿼리)을 더 효율적으로 수행할 수 있게 해줍니다.
# 그러나 이 구현은 추가적인 메모리를 사용하며, 삽입과 삭제 연산 시 최소값을 업데이트하는 추가적인 작업이 필요합니다. 따라서 최소값을 자주 조회해야 하는 경우에 유용한 구현이라고 할 수 있습니다.
class MinBSTNode(BSTNode):
    """A BSTNode which is augmented to keep track of the node with the
    minimum key in the subtree rooted at this node.
    """

    def __init__(self, parent, key):
        super().__init__(parent, key)
        self.min = self

    def find_min(self):
        """Finds the node with the minimum key in the subtree rooted at this
        node.

        Returns:
            The node with the minimum key.
        """
        return self.min

    def insert(self, node):
        """Inserts a node into the subtree rooted at this node.

        Args:
            node: The node to be inserted.
        """
        if node is None:
            return
        if node.key < self.key:
            # Updates the min of this node if the inserted node has a smaller
            # key.
            if node.key < self.min.key:
                self.min = node
            if self.left is None:
                node.parent = self
                self.left = node
            else:
                self.left.insert(node)
        else:
            if self.right is None:
                node.parent = self
                self.right = node
            else:
                self.right.insert(node)

    def delete(self):
        """Deletes this node itself.

        Returns:
            This node.
        """
        if self.left is None or self.right is None:
            if self is self.parent.left:
                self.parent.left = self.left or self.right
                if self.parent.left is not None:
                    self.parent.left.parent = self.parent
                    self.parent.min = self.parent.left.min
                else:
                    self.parent.min = self.parent
                # Propagates the changes upwards.
                c = self.parent
                while c.parent is not None and c is c.parent.left:
                    c.parent.min = c.min
                    c = c.parent
            else:
                self.parent.right = self.left or self.right
                if self.parent.right is not None:
                    self.parent.right.parent = self.parent
            return self
        else:
            s = self.next_larger()
            self.key, s.key = s.key, self.key
            return s.delete()


class BST(object):
    """A binary search tree."""

    def __init__(self, klass=BSTNode):
        """Creates an empty BST.

        Args:
            klass (optional): The class of the node in the BST. Default to
                BSTNode. 근데? self의 min값을 가지고 있는 MinBST node 를 지정할수도 있다는거지.
        """
        self.root = None
        self.klass = klass

    def __str__(self):
        if self.root is None: return '<empty tree>'
        return str(self.root)

    def find(self, k):
        """Finds and returns the node with key k from the subtree rooted at this
        node.

        Args:
            k: The key of the node we want to find.

        Returns:
            The node with key k or None if the tree is empty.
        """
        return self.root and self.root.find(k) ### 왜 self.root and ~ 야?? =>트리가 비어있는 경우 안전 처리 위함. 자주 사용 관용 표현 방식, 코드를 간결화 & None 체크 효과적 수행

    def find_min(self):
        """Returns the minimum node of this BST."""

        return self.root and self.root.find_min()                   # => find 와 똑같이 안전 처리 위한 코드

    def insert(self, k):
        """Inserts a node with key k into the subtree rooted at this node.

        Args:
            k: The key of the node to be inserted.

        Returns:
            The node inserted.
        """
        node = self.klass(None, k)   #klass는 node임. 그냥 bst node 든 minbst node든 둘다 parent랑, key값을 가지고 있으니까. parent는 당연히 none이고. k값은 지정해주는거고.
        if self.root is None:           #만약 root노드가 none 이면 그건 그냥 empty tree라는거니까 넣을려고 하는 node를 root로 지정
            # The root's parent is None.
            self.root = node
        else:
            self.root.insert(node)      #아니라면? root node에 대한 내장 함수 실행시키면 되는것임.
        return node                     #method chaining을 위해서 해당 노드를 반환하는것임. bst.insert(5).parent.key 같은?

    def delete(self, k):
        """Deletes and returns a node with key k if it exists from the BST.

        Args:
            k: The key of the node that we want to delete.

        Returns:
            The deleted node with key k.
        """
        node = self.find(k)
        if node is None:
            return None
        if node is self.root:                       #근데 만약 내가 없애려고 하는게 root노드라면 ?
            pseudoroot = self.klass(None, 0)        #임시 노드를 생성
            pseudoroot.left = self.root             #임시 노드 left는 root
            self.root.parent = pseudoroot           #root의 parent는 임시노드
            deleted = self.root.delete()            #노드를 삭제하면 이제 root자리에는 next large key값이 들어와 있을것임.(left right 둘다 있을때) left만 있으면 left가 root 되어 있을것이고. 사실 이것도 next large긴 하지만.
            self.root = pseudoroot.left             #이제 바뀐 root를 임시노드의 left로 정하고.
            if self.root is not None:               #만약 바뀐 root가 none이 아니라면, root parent는 none.
                self.root.parent = None             #임시 노드를 생성하는 것은 그저 linking을 끊기 위한것이라고 생각하면 되는것임.
            return deleted
        else:
            return node.delete()

    def next_larger(self, k):
        """Returns the node that contains the next larger (the successor) key in
        the BST in relation to the node with key k.

        Args:
            k: The key of the node of which the successor is to be found.

        Returns:
            The successor node.
        """
        node = self.find(k)
        return node and node.next_larger()

    def check_ri(self):
        """Checks the BST representation invariant.

        Raises:
            An exception if the RI is violated.
        """
        if self.root is not None:
            if self.root.parent is not None:    ## 이거 왜 굳이 하냐고? 내가 생각지도 못한 오류를 잡아내기 위해서야. 방어적 프로그래밍이라구 이런게!
                raise RuntimeError("BST RI violated by the root node's parent "
                                   "pointer.")
            self.root.check_ri()


class MinBST(BST): #Bst extend해서 그냥 node에 MinBSTNode 들어가게 한거.
    """An augmented BST that keeps track of the node with the minimum key."""

    def __init__(self):
        super().__init__(MinBSTNode)


def test(args=None, BSTtype=BST):
    if not args:
        args = sys.argv[1:]
    if not args:
        print('usage: %s <number-of-random-items | item item item ...>' % sys.argv[0])
        sys.exit()
    elif len(args) == 1:
        items = (random.randrange(100) for i in range(int(args[0])))
    else:
        items = [int(i) for i in args]

    tree = BSTtype()
    print(tree)
    for item in items:
        tree.insert(item)
        print()
        print(tree)


if __name__ == '__main__':
    test(["10"])
