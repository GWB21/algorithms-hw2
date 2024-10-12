import bst
'''시험범위 quickSort까지!'''
'''AVL Tree ipythonenotefy 그릴수 있는 library 제공해주신다고 하니 그거 이용해서 과제 낼것'''

def height(node):
    if node is None:
        return -1
    else:
        return node.height

def update_height(node):
    node.height = max(height(node.left), height(node.right)) + 1

class AVL(bst.BST):
    """
AVL binary search tree implementation.
Supports insert, delete, find, find_min, next_larger each in O(lg n) time.
"""

    def left_rotate(self, x):       #left Rotate
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
        y.left = x          #x는 잘 붙였으니까 y랑 left child로 link
        x.parent = y
        update_height(x)    #height 바뀌었으니까 update
        update_height(y)
        print("left rotate 발생")

    def right_rotate(self, x):          #right Rotate
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

    def rebalanced(self, node):   # x가 처음으로 규칙을 위반했을때 => AVL 트리 property 안지켜졌을때 rebalance하는 (메인코드네) 그니까 insert 할때마다 rebalance해주는거라 rotate는 최대 2번임.
        while node is not None:
            if height(node.left) >= 2 + height(node.right):
                if height(node.left.left) >= height(node.left.right):     #이건 왼쪽으로 치우쳐진 경우중 일직선일때는 right rotate 한번만 해도 되는것임.
                    self.right_rotate(node)
                else:                                                      #왼쪽 치우쳐진 경우중 zigzag일때 left rotate후 right rotate.
                    self.left_rotate(node.left)
                    self.right_rotate(node)
            elif height(node.right) >= 2 + height(node.left):              #걍 반대. 오른쪽으로 치우쳐진 경우임.
                if height(node.right.right) >= height(node.right.left):
                    self.left_rotate(node)
                else:
                    self.right_rotate(node.right)
                    self.left_rotate(node)

            update_height(node)
            node = node.parent

    ## find(k), find_min(), and next_larger(k) inherited from bst.BST

    def insert(self, k):
        """
        Inserts a node with key k into the subtree rooted at this node.
        This AVL version guarantees the balance property: h = O(lg n).
        
        Args:
            k: The key of the node to be inserted.
        """
        node = super(AVL, self).insert(k)
        self.rebalanced(node)

    def delete(self, k):
        """
        Deletes and returns a node with key k if it exists from the BST.
        This AVL version guarantees the balance property: h = O(lg n).
        
        Args:
            k: The key of the node that we want to delete.

        Returns:
            The deleted node with key k.
        """
        node = super(AVL, self).delete(k)
        ## node.parent is actually the old parent of the node,
        ## which is the first potentially out-of-balance node.
        self.rebalanced(node.parent)

def test(args=None):
    bst.test(args, BSTtype=AVL)

if __name__ == '__main__': test(["100"])