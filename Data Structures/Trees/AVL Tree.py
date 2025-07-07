class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class AVLTree:
    def __init__(self):
        self.root = None

    def height(self, node):
        if not node:
            return -1
        return 1 + max(self.height(node.left), self.height(node.right))

    def balance(self, node):
        if not node:
            return 0
        return self.height(node.left) - self.height(node.right)

    def insert(self, root, value):
        if not root:
            return Node(value)
        elif value < root.value:
            root.left = self.insert(root.left, value)
        else:
            root.right = self.insert(root.right, value)

        balance = self.balance(root)

        # Right rotation: If balance > 1 => Left subtree has more height than right subtree, 
        # value < root.left.value => new node is inserted in the left of left subtree.
        # So, directly right rotate the node at which inbalance is identified.
        if balance > 1 and value < root.left.value:
            return self.right_rotate(root)

        # Left rotation: If balance < -1 => Right subtree has more height than left subtree, 
        # value > root.right.value => new node is inserted in the right of right subtree.
        # So, directly left rotate the node at which inbalance is identified.
        if balance < -1 and value > root.right.value:
            return self.left_rotate(root)

        # Left-Right rotation: balance > 1 => Left subtree has more height than right subtree, 
        # value > root.left.value => new node is inserted in the right of left subtree.
        # So, left rotate the left child and right rotate the node at which inbalance is identified.
        if balance > 1 and value > root.left.value:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation: balance < -1 => Right subtree has more height than left subtree, 
        # value < root.right.value => new node is inserted in the left of right subtree.
        # So, right rotate the right child and left rotate the node at which inbalance is identified.
        if balance < -1 and value < root.right.value:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def delete(self, root, value):
        if not root:
            return root

        if value < root.value:
            root.left = self.delete(root.left, value)
        elif value > root.value:
            root.right = self.delete(root.right, value)
        else:
            if not root.left:
                temp = root.right
                root = None
                return temp
            elif not root.right:
                temp = root.left
                root = None
                return temp

            temp = self.min_value_node(root.right)
            root.value = temp.value
            root.right = self.delete(root.right, temp.value)

        if not root:
            return root

        balance = self.balance(root)

        # Right rotation: 
        if balance > 1 and self.balance(root.left) >= 0:
            return self.right_rotate(root)

        # Left rotation
        if balance < -1 and self.balance(root.right) <= 0:
            return self.left_rotate(root)

        # Left-Right rotation
        if balance > 1 and self.balance(root.left) < 0:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Right-Left rotation
        if balance < -1 and self.balance(root.right) > 0:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        return y

    def min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def search(self, root, value):
        if not root or root.value == value:
            return root
        if root.value < value:
            return self.search(root.right, value)
        return self.search(root.left, value)

    def insert_value(self, value):
        self.root = self.insert(self.root, value)

    def delete_value(self, value):
        self.root = self.delete(self.root, value)

    def search_value(self, value):
        return self.search(self.root, value)



if __name__ == "__main__":
    tree = AVLTree()
    tree.insert_value(8)
    tree.insert_value(6)
    tree.insert_value(10)
    tree.insert_value(3)
    tree.insert_value(7)
    tree.insert_value(17)
    print(tree.height(tree.root))
    # print("Tree after insertion:")
    # def inorder_traversal(root):
    #     if root:
    #         inorder_traversal(root.left)
    #         print(root.value),
    #         inorder_traversal(root.right)

    # inorder_traversal(tree.root)
    # print()

    # tree.delete_value(20)
    # print("Tree after deletion of 20:")
    # inorder_traversal(tree.root)
    # print()

    # result = tree.search_value(30)
    # if result:
    #     print("Node found")
    # else:
    #     print("Node not found")
