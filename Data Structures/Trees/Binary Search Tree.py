"""
    Preamble:
        Class Signature:
            (class) BSTTree_LinkedList

        This class represents a Binary Search Tree (BST) with a linked node structure.

        Parameters:
            1) root : Node --> Root node of the BST.

        Methods:
            1) (method) def insert(self: Self@BSTTree_LinkedList, val: Any) -> None :- Inserts a value into the BST, maintaining its order.
            
            2) (method) def findNode(self: Self@BSTTree_LinkedList, node: Node, val: Any) -> Node :- Finds a node with the specified value in the BST.
            
            3) (method) def delete(self: Self@BSTTree_LinkedList, val: Any) -> None :- Deletes a node with a specified value from the BST.
            
            4) (method) def getRoot(self: Self@BSTTree_LinkedList) -> Node :- Returns the root of the BST.
            
            5) (method) def isLeaf(self: Self@BSTTree_LinkedList, node: Node) -> bool :- Checks if a node is a leaf (has no children).
            
            6) (method) def height(self: Self@BSTTree_LinkedList, node: Node) -> int :- Calculates the height of the tree or subtree rooted at the given node.
            
            7) (method) def depth(self: Self@BSTTree_LinkedList, root: Node, x: Node, depth: int) -> int :- Calculates the depth of a given node in the BST.
            
            8) (method) def balancedFactor(self: Self@BSTTree_LinkedList, node: Node) -> None :- Placeholder for calculating balance factor.
            
            9) (method) def levelordertraversal(self: Self@BSTTree_LinkedList, node: Node) -> None :- Performs a level-order (breadth-first) traversal of the tree.
            
            10) (method) def print_level(self: Self@BSTTree_LinkedList, node: Node, level: int) -> None :- Helper function to print nodes at a specific level.
            
            11) (method) def convertSortedArrayToBST(self: Self@BSTTree_LinkedList, eltList: List) -> Node :- Converts a sorted array into a balanced BST.
"""
class BSTTree_LinkedList:
    def __init__(self):
        self.root = None  # Root of the BST, initially None
    
    class Node:
        def __init__(self, val=None):
            self.value = val          # Value of the node
            self.parent = None        # Parent node reference
            self.leftchild = None     # Left child reference
            self.rightchild = None    # Right child reference

    def insert(self, val): # O(log(n)) [or] O(n) if the tree is skewed.
        """
            Inserts a new value into the BST, maintaining BST properties.
        """
        newNode = self.Node(val)
        if not self.root:
            self.root = newNode  # Set the new node as root if tree is empty
            self.levelordertraversal(self.root)  # Print the tree in level-order
            return

        def insertNode(node, val): 
            """
                Recursively inserts a new node into the correct position in the tree.
            """
            if not node:
                return newNode  # Return new node when found insertion point
            
            if val <= node.value:  # Insert in left subtree
                node.leftchild = insertNode(node.leftchild, val)
            else:  # Insert in right subtree
                node.rightchild = insertNode(node.rightchild, val)
            return node # Return node to the above recursive calls.
        
        insertNode(self.root, val) # Call the helper function
        self.levelordertraversal(self.root)  # Print the tree after insertion
    
    def findNode(self, node, val): # O(log(n)) [or] O(n) if the tree is skewed.
        """
            Finds and returns the node with the given value.
        """
        if not node:
            return -1  # Node not found
        
        if node.value < val:  # Search in left subtree
            return self.findNode(node.leftchild, val)
        elif node.value > val:  # Search in right subtree
            return self.findNode(node.rightchild, val)
        else:
            return node  # Return the node if found
    
    def delete(self, val): # O(log(n)) [or] O(n) if the tree is skewed.
        """
            Deletes a node with a given value from the BST.
        """
        node = self.findNode(self.root, val)  # Find the node to delete
        
        # Case 1: Node has no children (leaf node)
        if node.leftchild is None and node.rightchild is None:
            # If the node is the root, set root to None
            if not node.parent:
                self.root = None  
                return
            
            if node.parent.leftchild == node: # If the node is leftchild of it's parent, make leftchild of it as None
                node.parent.leftchild = None
            else: # If the node is rightchild of it's parent, make rightchild of it as None
                node.parent.rightchild = None
            return
        
        # Case 2: Node has one child
        if node.leftchild is None or node.rightchild is None:
            if node.leftchild is None:
                child = node.rightchild  # Use right child if left is absent
            else:
                child = node.leftchild  # Use left child if right is absent
            
            if node.parent:
                # Attach child to node's parent
                if node.parent.leftchild == node:
                    node.parent.leftchild = child
                else:
                    node.parent.rightchild = child
            else:
                self.root = child  # Set child as root if deleting root
            return
        
        # Case 3: Node has two children
        curr = node.rightchild  # Find in-order successor (smallest in right subtree)
        while curr.leftchild:
            curr = curr.leftchild
        
        node.value = curr.value  # Replace node's value with in-order successor's value
        
        # Delete the in-order successor
        curr.parent.leftchild = curr.rightchild

    def getRoot(self): # O(1)
        """
            Returns the root node of the BST.
        """
        return self.root

    def isLeaf(self, node): # O(1)
        """
            Checks if the given node is a leaf (has no children).
        """
        return node.leftchild is None and node.rightchild is None

    def height(self, node): # O(n)
        """
            Returns the height of the subtree rooted at the given node.
        """
        if not node:
            return 0
        return 1 + max(self.height(node.leftchild), self.height(node.rightchild))

    def depth(self, root, x, depth = 0): # O(log(n)) [or] O(n) if the tree is skewed.
        """
            Returns the depth of the given node in the BST.
        """
        if not root:
            return -1
        
        if root == x:
            return depth
        
        left = self.depth(root.leftchild, x, depth + 1)
        if left != -1:
            return left
        return self.depth(root.rightchild, x, depth + 1)

    def balancedFactor(self, node):
        """
            Placeholder for calculating the balance factor of a node.
        """
        pass

    def levelordertraversal(self, node): # O(n)
        """
            Prints the BST level-by-level (level-order traversal).
        """
        h = self.height(node)
        for i in range(1, h + 1):
            self.print_level(node, i)
    
    def print_level(self, node, level): # O(n)
        """
            Helper function to print nodes at a given level.
        """
        if node is None:
            return
        if level == 1:
            print(node.value, end=" ")
        elif level > 1:
            self.print_level(node.leftchild, level - 1)
            self.print_level(node.rightchild, level - 1)

    def convertSortedArrayToBST(self, eltList): # O(n)
        """
            Converts a sorted array into a balanced BST.
        """
        def helper(arr, s, e):
            if s > e:
                return None
            mid = s + (e - s) // 2 
            newNode = self.Node(arr[mid])  # Create new node from middle element
            newNode.leftchild = helper(arr, s, mid - 1)  # Recursively build left subtree
            newNode.rightchild = helper(arr, mid + 1, e)  # Recursively build right subtree
            return newNode
        
        return helper(eltList, 0, len(eltList) - 1)  # Start recursion with full array

    def isValidBST(self, root) -> bool: # O(n)
        """
            Checks if a given binary tree is a binary search tree.
        """
        def valid(node, minimum, maximum):
            """
                Helper function to validate if a given tree is binary tree is a binary search tree.
            """
            if not node: # If node does not exist it means either we reached the end or tree is empty. So, return true.
                return True

            # If a node violates search tree condition, then return False.
            if not (node.val > minimum and node.val < maximum):
                return False
            
            # Validate left subtree and right subtree and check if both left and right subtrees are BST's recursively.
            return valid(node.left,minimum,node.val) and valid(node.right,node.val,maximum)
        # Call helper function.
        return valid(root,float("-inf"), float("inf"))