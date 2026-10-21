class TreeNode:
    def __init__(self, value, right=None, left=None, prev=None):
        self.value = value
        self.right = right
        self.left = left
        self.prev = prev


class BST:
    def __init__(self):
        self.root = None
        self.h = 0

    def height(self, cur_node=None, cur_height=1):
        if self.root is None:
            return 0

        if cur_node is None:
            cur_node = self.root

        if cur_height > self.h:
            self.h = cur_height

        if cur_node.left:
            self.height(cur_node.left, cur_height + 1)

        if cur_node.right:
            self.height(cur_node.right, cur_height + 1)

    def add_node(self, value: int, cur_node=None) -> None | TreeNode:
        if cur_node is None:
            cur_node = self.root

        if cur_node is None:
            self.root = TreeNode(value)
            return self.root

        if value < cur_node.value:
            if not cur_node.left:
                cur_node.left = TreeNode(value)
                cur_node.left.prev = cur_node
                return self.root
            self.add_node(value, cur_node.left)

        elif value > cur_node.value:
            if not cur_node.right:
                cur_node.right = TreeNode(value)
                cur_node.right.prev = cur_node
                return self.root
            self.add_node(value, cur_node.right)

        else:
            return self.root

    def find_min(self, tree: TreeNode) -> None | TreeNode:
        if tree.left:
            return self.find_min(tree.left)
        else:
            return tree.value

    def delete_node(self, value: int, cur_node=None) -> None | TreeNode:
        if not self.root:
            return None

        if cur_node is None:
            cur_node = self.root

        if value < cur_node.value:
            if not cur_node.left:
                return self.root
            self.delete_node(value, cur_node.left)

        elif value > cur_node.value:
            if not cur_node.right:
                return self.root
            self.delete_node(value, cur_node.right)

        else:
            if cur_node.left and not cur_node.right:
                if cur_node is self.root:
                    self.root = cur_node.left
                    self.root.prev = None
                else:
                    cur_node.left.prev = cur_node.prev
                    if cur_node.prev.left is cur_node:
                        cur_node.prev.left = cur_node.left
                    else:
                        cur_node.prev.right = cur_node.left

            elif not cur_node.left and cur_node.right:
                if cur_node is self.root:
                    self.root = cur_node.right
                    self.root.prev = None
                else:
                    cur_node.right.prev = cur_node.prev
                    if cur_node.prev.left is cur_node:
                        cur_node.prev.left = cur_node.right
                    else:
                        cur_node.prev.right = cur_node.right

            elif not cur_node.left and not cur_node.right:
                if cur_node is self.root:
                    self.root = None
                else:
                    if cur_node.prev.left is cur_node:
                        cur_node.prev.left = None
                    else:
                        cur_node.prev.right = None

            elif cur_node.left and cur_node.right:
                min_elem = self.find_min(cur_node.right)
                self.delete_node(min_elem, cur_node.right)
                cur_node.value = min_elem

    def exists(self, value, cur_node=None):
        if self.root is None:
            print('NO')
            return self.root
        if cur_node is None:
            cur_node = self.root

        if cur_node.value == value:
            print('YES')
        elif cur_node.left and value < cur_node.value:
            self.exists(value, cur_node.left)
        elif cur_node.right and value > cur_node.value:
            self.exists(value, cur_node.right)
        else:
            print('NO')       
                
    def print(self, cur_node=None):
        if self.root is None:
            print('Empty')
            return

        if cur_node is None:
            cur_node = self.root

        print(cur_node.value, end=' ')

        if cur_node.left:
            self.print(cur_node.left)
        if cur_node.right:
            self.print(cur_node.right)


n = int(input())
Tree = BST()

for i in range(n):
    raw_command = input().split()
    if raw_command:
        if raw_command[0] == 'add':
            Tree.add_node(int(raw_command[1]))
        if raw_command[0] == 'print':
            Tree.print()
        if raw_command[0] == 'exists':
            Tree.exists(int(raw_command[1]))
        if raw_command[0] == 'del':
            Tree.delete_node(int(raw_command[1]))
        if raw_command[0] == 'height':
            Tree.h = 0
            Tree.height()
            print(Tree.h)
