class TreeNode:
    def __init__(self, value, right=None, left=None, prev=None):
        self.value = value
        self.right = right
        self.left = left
        self.prev = prev
        self.height = 1


class BST:
    def __init__(self):
        self.root = None
        self.h = 0

    def get_height(self, node):
        if node is None:
            return 0
        return node.height

    def update_height(self, node):
        if node is not None:
            node.height = 1 + max(self.get_height(node.left), self.get_height(node.right))

    def get_balance(self, node):
        if node is None:
            return 0
        return self.get_height(node.right) - self.get_height(node.left)

    def height(self):
        if self.root is None:
            return 0
        return self.root.height

    def add_node(self, value: int, cur_node=None, parent=None) -> None | TreeNode:
        if cur_node is None:
            if self.root is None:
                self.root = TreeNode(value)
                return self.root
            cur_node = self.root
            parent = None

        if value < cur_node.value:
            if not cur_node.left:
                cur_node.left = TreeNode(value)
                cur_node.left.prev = cur_node
            else:
                self.add_node(value, cur_node.left, cur_node)
        elif value > cur_node.value:
            if not cur_node.right:
                cur_node.right = TreeNode(value)
                cur_node.right.prev = cur_node
            else:
                self.add_node(value, cur_node.right, cur_node)
        else:
            return self.root

        self.update_height(cur_node)
        balance = self.get_balance(cur_node)

        if balance == 2:
            u = cur_node.right
            if self.get_balance(u) >= 0:
                b = cur_node.right
                t = b.left
                b.prev = cur_node.prev
                if cur_node.prev is None:
                    self.root = b
                elif cur_node.prev.left is cur_node:
                    cur_node.prev.left = b
                else:
                    cur_node.prev.right = b
                b.left = cur_node
                cur_node.prev = b
                cur_node.right = t
                if t is not None:
                    t.prev = cur_node
                self.update_height(cur_node)
                self.update_height(b)
            else:
                u = cur_node.right
                c = u.left
                t2 = c.right
                c.right = u
                u.prev = c
                u.left = t2
                if t2 is not None:
                    t2.prev = u
                self.update_height(u)
                self.update_height(c)
                cur_node.right = c
                c.prev = cur_node

                b = cur_node.right
                t = b.left
                b.prev = cur_node.prev
                if cur_node.prev is None:
                    self.root = b
                elif cur_node.prev.left is cur_node:
                    cur_node.prev.left = b
                else:
                    cur_node.prev.right = b
                b.left = cur_node
                cur_node.prev = b
                cur_node.right = t
                if t is not None:
                    t.prev = cur_node
                self.update_height(cur_node)
                self.update_height(b)

        elif balance == -2:
            u = cur_node.left
            if self.get_balance(u) <= 0:
                b = cur_node.left
                t = b.right
                b.prev = cur_node.prev
                if cur_node.prev is None:
                    self.root = b
                elif cur_node.prev.left is cur_node:
                    cur_node.prev.left = b
                else:
                    cur_node.prev.right = b
                b.right = cur_node
                cur_node.prev = b
                cur_node.left = t
                if t is not None:
                    t.prev = cur_node
                self.update_height(cur_node)
                self.update_height(b)
            else:
                u = cur_node.left
                c = u.right
                t2 = c.left
                c.left = u
                u.prev = c
                u.right = t2
                if t2 is not None:
                    t2.prev = u
                self.update_height(u)
                self.update_height(c)
                cur_node.left = c
                c.prev = cur_node

                b = cur_node.left
                t = b.right
                b.prev = cur_node.prev
                if cur_node.prev is None:
                    self.root = b
                elif cur_node.prev.left is cur_node:
                    cur_node.prev.left = b
                else:
                    cur_node.prev.right = b
                b.right = cur_node
                cur_node.prev = b
                cur_node.left = t
                if t is not None:
                    t.prev = cur_node
                self.update_height(cur_node)
                self.update_height(b)

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

    def root_value(self):
        if self.root is None:
            print('Empty')
        else:
            print(self.root.value)

    def next(self, value, cur_node=None):
        if self.root is None:
            print('None')
            return
        if cur_node is None:
            cur_node = self.root

        result = None
        node = cur_node
        while node is not None:
            if node.value >= value:
                result = node.value
                node = node.left
            else:
                node = node.right

        if result is None:
            print('None')
        else:
            print(result)

    def prev(self, value, cur_node=None):
        if self.root is None:
            print('None')
            return
        if cur_node is None:
            cur_node = self.root

        result = None
        node = cur_node
        while node is not None:
            if node.value <= value:
                result = node.value
                node = node.right
            else:
                node = node.left

        if result is None:
            print('None')
        else:
            print(result)

    def del_node(self, value: int, cur_node=None) -> None:
        if self.root is None:
            return
        if cur_node is None:
            cur_node = self.root

        if value < cur_node.value:
            if cur_node.left:
                self.del_node(value, cur_node.left)
        elif value > cur_node.value:
            if cur_node.right:
                self.del_node(value, cur_node.right)
        else:
            if cur_node.left is None or cur_node.right is None:
                if cur_node.left:
                    child = cur_node.left
                else:
                    child = cur_node.right
                if child is not None:
                    child.prev = cur_node.prev
                if cur_node.prev is None:
                    self.root = child
                elif cur_node.prev.left is cur_node:
                    cur_node.prev.left = child
                else:
                    cur_node.prev.right = child
                start = cur_node.prev
            else:
                m = cur_node.right
                while m.left is not None:
                    m = m.left
                cur_node.value = m.value
                if m.right:
                    child = m.right
                else:
                    child = None
                if child is not None:
                    child.prev = m.prev
                if m.prev.left is m:
                    m.prev.left = child
                else:
                    m.prev.right = child
                start = m.prev

            node = start
            while node is not None:
                self.update_height(node)
                balance = self.get_balance(node)

                if balance == 2:
                    u = node.right
                    if self.get_balance(u) >= 0:
                        b = node.right
                        t = b.left
                        b.prev = node.prev
                        if node.prev is None:
                            self.root = b
                        elif node.prev.left is node:
                            node.prev.left = b
                        else:
                            node.prev.right = b
                        b.left = node
                        node.prev = b
                        node.right = t
                        if t is not None:
                            t.prev = node
                        self.update_height(node)
                        self.update_height(b)
                        new_top = b
                    else:
                        u = node.right
                        c = u.left
                        t2 = c.right
                        c.right = u
                        u.prev = c
                        u.left = t2
                        if t2 is not None:
                            t2.prev = u
                        self.update_height(u)
                        self.update_height(c)
                        node.right = c
                        c.prev = node

                        b = node.right
                        t = b.left
                        b.prev = node.prev
                        if node.prev is None:
                            self.root = b
                        elif node.prev.left is node:
                            node.prev.left = b
                        else:
                            node.prev.right = b
                        b.left = node
                        node.prev = b
                        node.right = t
                        if t is not None:
                            t.prev = node
                        self.update_height(node)
                        self.update_height(b)
                        new_top = b

                elif balance == -2:
                    u = node.left
                    if self.get_balance(u) <= 0:
                        b = node.left
                        t = b.right
                        b.prev = node.prev
                        if node.prev is None:
                            self.root = b
                        elif node.prev.left is node:
                            node.prev.left = b
                        else:
                            node.prev.right = b
                        b.right = node
                        node.prev = b
                        node.left = t
                        if t is not None:
                            t.prev = node
                        self.update_height(node)
                        self.update_height(b)
                        new_top = b
                    else:
                        u = node.left
                        c = u.right
                        t2 = c.left
                        c.left = u
                        u.prev = c
                        u.right = t2
                        if t2 is not None:
                            t2.prev = u
                        self.update_height(u)
                        self.update_height(c)
                        node.left = c
                        c.prev = node

                        b = node.left
                        t = b.right
                        b.prev = node.prev
                        if node.prev is None:
                            self.root = b
                        elif node.prev.left is node:
                            node.prev.left = b
                        else:
                            node.prev.right = b
                        b.right = node
                        node.prev = b
                        node.left = t
                        if t is not None:
                            t.prev = node
                        self.update_height(node)
                        self.update_height(b)
                        new_top = b

                else:
                    new_top = node

                if new_top is self.root or new_top.prev is None:
                    break
                node = new_top.prev

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


Q = int(input())
Tree = BST()

for _ in range(Q):
    parts = input().split()
    cmd = parts[0]

    if cmd == 'add':
        Tree.add_node(int(parts[1]))
    elif cmd == 'del':
        Tree.del_node(int(parts[1]))
    elif cmd == 'exists':
        Tree.exists(int(parts[1]))
    elif cmd == 'next':
        Tree.next(int(parts[1]))
    elif cmd == 'prev':
        Tree.prev(int(parts[1]))
    elif cmd == 'root':
        Tree.root_value()
    elif cmd == 'height':
        print(Tree.height())
    elif cmd == 'print':
        Tree.print()
        print()