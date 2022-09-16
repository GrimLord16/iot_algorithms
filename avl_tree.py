class Node:
    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        self.height = 0
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.__root = None

    def insert(self, data):

        if not self.__root:
            self.__root = Node(data)
        else:
            self.__insert_data(data, self.__root)

    def remove(self, data):
        try:
            if not self.__root:
                print("No data!")
            else:
                self.__remove_data(data, self.__root)
        except TypeError:
            print("Incorrect Type!")

    def __insert_data(self, data, node):
        if data < node.data:
            if node.left:
                self.__insert_data(data, node.left)
            else:
                node.left = Node(data, node)
                self.__violation_handler(node.left)
        if data > node.data:
            if node.right:
                self.__insert_data(data, node.right)
            else:
                node.right = Node(data, node)
                self.__violation_handler(node.right)

    def __remove_data(self, data, node):
        if data < node.data:
            if node.left:
                self.__remove_data(data, node.left)
        elif data > node.data:
            if node.right:
                self.__remove_data(data, node.right)
        elif data == node.data:

            if not node.left and not node.right:
                parent_node = node.parent
                if parent_node:
                    if parent_node.left == node:
                        parent_node.left = None
                    elif parent_node.right == node:
                        parent_node.right = None

                else:
                    self.__root = None
                del node
                self.__violation_handler(parent_node)

            elif node.left and not node.right:
                parent_node = node.parent

                if parent_node:
                    if parent_node.left == node:
                        parent_node.left = node.left
                    elif parent_node.right == node:
                        parent_node.right = node.left
                else:
                    self.__root = node.left

                node.left.parent = parent_node
                del node
                self.__violation_handler(parent_node)

            elif node.right and not node.left:
                parent_node = node.parent

                if parent_node:
                    if parent_node.left == node:
                        parent_node.left = node.right
                    elif parent_node.right == node:
                        parent_node.right = node.right
                else:
                    self.__root = node.right

                node.right.parent = parent_node
                del node
                self.__violation_handler(parent_node)

            elif node.left and node.right:

                successor_node = self.__find_successor(node.right)
                successor_node.data, node.data = node.data, successor_node.data
                self.__remove_data(successor_node.data, node.right)

    def __find_successor(self, node):
        if node.left:
            return self.__find_successor(node.left)
        return node

    def __violation_handler(self, node):
        while node:
            node.height = max(self.__get_height(node.left), self.__get_height(node.right)) + 1
            self.__violation_fix(node)
            node = node.parent

    def __get_height(self, node):
        if not node:
            return -1
        return node.height

    def __violation_fix(self, node):

        if self.__balance_factor(node) > 1:

            if self.__balance_factor(node.left) < 0:
                self.__left_rotation(node.left)
            self.__right_rotation(node)

        if self.__balance_factor(node) < -1:

            if self.__balance_factor(node.right) > 0:
                self.__right_rotation(node.right)
            self.__left_rotation(node)

    def __balance_factor(self, node):

        if not node:
            return 0
        return self.__get_height(node.left) - self.__get_height(node.right)

    def __left_rotation(self, node):
        temp_right_node = node.right
        t = node.right.left

        temp_right_node.left = node
        node.right = t

        temp_parent = node.parent
        temp_right_node.parent = temp_parent
        node.parent = temp_right_node
        if t:
            t.parent = node

        if temp_right_node.parent:
            if temp_right_node.parent.left == node:
                temp_right_node.parent.left = temp_right_node
            elif temp_right_node.parent.right == node:
                temp_right_node.parent.right = temp_right_node

        else:
            self.__root = temp_right_node

        node.height = max(self.__get_height(node.left), self.__get_height(node.right)) + 1
        temp_right_node.height = max(self.__get_height(temp_right_node.left),
                                     self.__get_height(temp_right_node.right)) + 1

        print(f"left rotation on {node.data}")

    def __right_rotation(self, node):
        temp_left_node = node.left
        t = node.left.right

        temp_left_node.right = node
        node.left = t

        temp_parent = node.parent
        temp_left_node.parent = temp_parent
        node.parent = temp_left_node
        if t:
            t.parent = node

        if temp_left_node.parent:
            if temp_left_node.parent.left == node:
                temp_left_node.parent.left = temp_left_node
            elif temp_left_node.parent.right == node:
                temp_left_node.parent.right = temp_left_node
        else:
            self.__root = temp_left_node

        node.height = max(self.__get_height(node.left), self.__get_height(node.right)) + 1
        temp_left_node.height = max(self.__get_height(temp_left_node.left),
                                    self.__get_height(temp_left_node.right)) + 1

        print(f"right rotation on {node.data}")

    def find(self, data):
        if self.__root:
            return self.__find_data(data, self.__root)

    def __find_data(self, data, node):
        try:
            if data < node.data:
                if node.left:
                    return self.__find_data(data, node.left)
            elif data > node.data:
                if node.right:
                    return self.__find_data(data, node.right)
            elif data == node.data:
                return True
            return False
        except TypeError:
            return "Incorrect Type!"

    def print_scheme(self, node, level=0):

        if node is not None:
            self.print_scheme(node.left, level + 1)
            print(' ' * 4 * level + f"-> {node.data}")
            self.print_scheme(node.right, level + 1)

    def print_tree(self):
        self.print_scheme(self.__root)


if __name__ == "__main__":
    tree = AVLTree()

    tree.insert(12)
    tree.insert(24)
    tree.insert(10)
    tree.insert(0)
    tree.insert(-2)
    tree.insert(20)
    tree.insert(21)
    tree.insert(19)
    tree.insert(-6)
    tree.insert(-3)
    tree.insert(-10)
    tree.remove("sam")
    tree.remove(-10)

    print(tree.find('-222'))
    print(tree.find(18))
    print(tree.find(19))
    tree.print_tree()
