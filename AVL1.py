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

    def left_rotate(self, value, cur_node=None, parent=None):
        if cur_node is None:
            cur_node = self.root

        if cur_node.value == value:
            right_branch = cur_node.right
            right_left_branch = right_branch.left

            right_branch.prev = parent
            if parent is None:
                self.root = right_branch
            elif parent.left is cur_node:
                parent.left = right_branch
            else:
                parent.right = right_branch

            right_branch.left = cur_node
            cur_node.prev = right_branch

            cur_node.right = right_left_branch
            if right_left_branch is not None:
                right_left_branch.prev = cur_node

            return self.root

        if value < cur_node.value and cur_node.left:
            return self.left_rotate(value, cur_node.left, cur_node)
        elif value > cur_node.value and cur_node.right:
            return self.left_rotate(value, cur_node.right, cur_node)

        return self.root

    def right_rotate(self, value, cur_node=None, parent=None):
        if cur_node is None:
            cur_node = self.root

        if cur_node.value == value:
            left_branch = cur_node.left
            left_right_branch = left_branch.right

            left_branch.prev = parent
            if parent is None:
                self.root = left_branch
            elif parent.left is cur_node:
                parent.left = left_branch
            else:
                parent.right = left_branch

            left_branch.right = cur_node
            cur_node.prev = left_branch

            cur_node.left = left_right_branch
            if left_right_branch is not None:
                left_right_branch.prev = cur_node

            return self.root

        if value < cur_node.value and cur_node.left:
            return self.right_rotate(value, cur_node.left, cur_node)
        elif value > cur_node.value and cur_node.right:
            return self.right_rotate(value, cur_node.right, cur_node)

        return self.root


N = int(input())
add_nums = list(map(int, input().split()))[:N]
M = int(input())

rotate_commands = []
for _ in range(M):
    cmd, x = input().split()
    rotate_commands.append((cmd, int(x)))

Tree = BST()
for num in add_nums:
    Tree.add_node(num)

for cmd, x in rotate_commands:
    if cmd == 'left':
        Tree.left_rotate(x)
    else:
        Tree.right_rotate(x)

    Tree.print()
    print()