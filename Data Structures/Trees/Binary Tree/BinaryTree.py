"""
Binary Tree Data Structure with various tree operations.

This module provides a generic Binary Tree implementation with support for building,
querying, and manipulating binary trees.

Traversal Methods:
    - Recursive traversals are available in RecursiveTraversals.py
    - Iterative traversals are available in IterativeTraversals.py

These modules import BinaryTree and provide traversal functions without duplicating
the tree structure code.
"""


class BinaryTree:
    """
    A generic Binary Tree implementation with support for various tree operations.
    
    This class provides methods for building, traversing, and manipulating binary trees,
    including insertion, deletion, depth/height calculation, and advanced queries like
    finding ancestors and common ancestors.
    
    Note: Traversal methods (inorder, preorder, postorder, euler tour) have been
    separated into RecursiveTraversals.py and IterativeTraversals.py modules to
    maintain modularity and provide both recursive and iterative implementations.
    """
    
    class Node:
        """
        Internal node class representing a single element in the binary tree.
        
        Attributes:
            element: The data value stored in this node
            parent: Reference to the parent node (None if root)
            leftchild: Reference to the left child node
            rightchild: Reference to the right child node
        """
        def __init__(self) -> None:
            self.element = 0
            self.parent = None
            self.leftchild = None
            self.rightchild = None
    
    def __init__(self) -> None:
        """Initialize an empty binary tree with root node."""
        self.sz = 0  # Track the number of nodes in the tree
        self.root = self.Node()  # Create an empty root node

    def getChildren(self, curnode):
        """
        Get all children of a given node.
        
        Args:
            curnode: The node whose children are to be retrieved
            
        Returns:
            List of child nodes (empty list if node has no children)
        """
        children = []
        if curnode.leftchild != None:
            children.append(curnode.leftchild)
        if curnode.rightchild != None:
            children.append(curnode.rightchild)
        return children

    def isExternal(self, curnode):
        """
        Check if a node is a leaf (external node with no children).
        
        Args:
            curnode: The node to check
            
        Returns:
            True if node is a leaf, False otherwise
        """
        if curnode.leftchild == None and curnode.rightchild == None:
            return True
        return False
    
    def getRoot(self):
        """
        Get the element value stored in the root node.
        
        Returns:
            The element value at the root, or 0 if tree is empty
        """
        return self.root.element

    def isRoot(self, curnode):
        """
        Check if a given node is the root of the tree.
        
        Args:
            curnode: The node to check
            
        Returns:
            True if node has no parent (is root), False otherwise
        """
        if curnode.parent == None:
            return True
        return False
    
    def isEmpty(self):
        """
        Check if the binary tree is empty.
        
        Returns:
            True if tree has no nodes, False otherwise
        """
        return self.sz == 0

    def findDepth(self):
        """
        Calculate the depth (height) of the entire binary tree.
        Depth is the maximum number of edges from root to any leaf.
        
        Returns:
            The height of the tree (0 for single node, -1 for empty)
        """
        def depth(node):
            # Base case: empty node contributes 0 to depth
            if not node:
                return 0
            # Recursively find max depth from both subtrees and add 1
            return 1 + max(depth(node.leftchild), depth(node.rightchild))

        return depth(self.root)

    def findDepthofNode(self, root, x, depth):
        """
        Find the depth of a specific node within the tree.
        Depth is measured as the number of edges from root to the node.
        
        Args:
            root: The root node to start search from
            x: The target node to find
            depth: Current depth counter (start with 0)
            
        Returns:
            The depth of node x, or -1 if node not found
        """
        if not root:
            return -1
        
        # Found the target node
        if root == x:
            return depth
        
        # Search in left subtree first
        left = self.findDepthofNode(root.leftchild, x, depth + 1)
        if left != -1:
            return left
        # If not found in left, search right subtree
        return self.findDepthofNode(root.rightchild, x, depth + 1)

    def findHeightOfNode(self, node):
        """
        Calculate the height of a specific node.
        Height is the longest path from the node to any leaf below it.
        
        Args:
            node: The node whose height is to be calculated
            
        Returns:
            The height of the node (-1 if node is None)
        """
        def findHeight(root):
            # Base case: no node means -1 height
            if not root:
                return -1
            # Height is 1 plus the maximum height of its children
            return 1 + max(findHeight(root.leftchild), findHeight(root.rightchild))
        return findHeight(node)

    def displayTree(self):
        """
        Display the binary tree in a visual format with right-child bias.
        Shows the tree structure with connections, rotated 90 degrees clockwise.
        """
        def display(node, level):
            # Base case: stop if node is None
            if not node:
                return
            
            # Display right subtree first (top of output)
            display(node.rightchild, level + 1)

            # Display current node with indentation based on level
            if level != 0:
                # Add indentation for non-root nodes
                for _ in range(level - 1):
                    print('\t\t', end='')
                print('|-------->', node.element)
            else:
                # Root node has no prefix
                print(node.element)
            
            # Display left subtree (bottom of output)
            display(node.leftchild, level + 1)

        display(self.root, 0)

    def buildTree(self, eltlist):
        """
        Build a complete binary tree from a list of elements using level-order indexing.
        Elements are arranged as: [None, root, leftChild, rightChild, ...]
        Use -1 to represent None/empty positions in the tree.
        
        Args:
            eltlist: List with None at index 0, followed by tree elements
                    (use -1 for positions where nodes should not exist)
                    
        Returns:
            List of nodes in level-order, with None at index 0
        """
        nodelist = []
        nodelist.append(None)  # Index 0 is reserved
        
        # Build nodes starting from index 1
        for i in range(len(eltlist)):
            if i != 0:
                if eltlist[i] != -1:  # -1 represents no node at this position
                    tempnode = self.Node()
                    tempnode.element = eltlist[i]
                    
                    # Set parent and position for non-root nodes
                    if i != 1:
                        tempnode.parent = nodelist[i // 2]  # Parent at index i//2
                        if i % 2 == 0:  # Even index = left child
                            nodelist[i // 2].leftchild = tempnode
                        else:  # Odd index = right child
                            nodelist[i // 2].rightchild = tempnode
                    
                    nodelist.append(tempnode)
                    self.sz += 1
                else:
                    nodelist.append(None)
        
        # Set root to first actual node
        self.root = nodelist[1]
        return nodelist


    def insertNode(self, data):
        """
        Insert a new node with given data into the tree while maintaining level-order.
        Inserts in the first available position (left-to-right, top-to-bottom).
        
        Args:
            data: The element value to insert
            
        Returns:
            List of all nodes in the tree in level-order (with None at index 0)
        """
        newNode = self.Node()
        newNode.element = data
        
        # If tree is empty, make it the root
        if not self.root:
            self.root = newNode
        else:
            # Use BFS to find the first node with an empty child
            queue = [self.root]
            while queue:
                temp = queue.pop(0)
                
                # Try to insert as left child
                if not temp.leftchild:
                    temp.leftchild = newNode
                    newNode.parent = temp
                    break
                else:
                    queue.append(temp.leftchild)
                
                # Try to insert as right child
                if not temp.rightchild:
                    temp.rightchild = newNode
                    newNode.parent = temp
                    break
                else:
                    queue.append(temp.rightchild)
        
        # Return updated node list in level-order
        level = 0
        nlist = [None]
        while True:
            curNodes = self.getNodesAtALevel(level)
            if not curNodes:
                return nlist
            nlist.extend(curNodes)
            level += 1


    def getNodesAtALevel(self, level: int):
        """
        Get all nodes at a specific level in the tree.
        Root is at level 0, its children at level 1, etc.
        
        Args:
            level: The level number to retrieve nodes from
            
        Returns:
            List of nodes at the specified level (empty if level doesn't exist)
        """
        nodesList = []
        def nodesAtLevel(node, level):
            # Base case: empty node
            if not node:
                return
            # If at target level, add to result
            if level == 0:
                nodesList.append(node)
            else:
                # Otherwise, recurse to next level
                nodesAtLevel(node.leftchild, level - 1)
                nodesAtLevel(node.rightchild, level - 1)
        nodesAtLevel(self.root, level)
        return nodesList

    def getLeaves(self):
        """
        Get all leaf nodes (external nodes with no children) in the tree.
        
        Returns:
            List of element values at leaf nodes
        """
        leaves_ = []
        def leaves(node):
            if not node:
                return
            # Add node if it has no children
            if not node.leftchild and not node.rightchild:
                leaves_.append(node.element)
            # Recurse to children
            leaves(node.leftchild)
            leaves(node.rightchild)

        leaves(self.root)
        return leaves_

    def findSibling(self, node):
        """
        Find the sibling of a given node (the other child of its parent).
        
        Args:
            node: The node whose sibling is to be found
            
        Returns:
            The sibling node, or None if node has no sibling or is root
        """
        if not node or not node.parent:
            return None
        # If this node is the left child, return right sibling
        if node.parent.leftchild == node:
            return node.parent.rightchild
        # Otherwise return left sibling
        return node.parent.leftchild
    

    def findCousins(self, node):
        """
        Find all cousin nodes of a given node.
        Cousins are nodes at the same level with a different parent.
        
        Args:
            node: The node whose cousins are to be found
            
        Returns:
            List of element values of all cousin nodes
        """
        # Find the level of the target node
        level = self.findDepthofNode(self.root, node, 0)
        
        if level == -1:
            return []
        
        # Return all nodes at that level except the node itself
        return [x.element for x in self.getNodesAtALevel(level) if x != node]
    
    def deleteLeaves(self):
        """
        Delete all leaf nodes from the tree, leaving only internal nodes.
        
        Returns:
            List of remaining nodes in level-order (with None at index 0)
        """
        def delete(node):
            if not node:
                return
            # If this is a leaf node, remove it
            if not node.leftchild and not node.rightchild:
                if not node.parent:
                    return []  # Cannot delete root
                # Disconnect from parent
                if node.parent.leftchild == node:
                    temp = node
                    node.parent.leftchild = None
                    del temp
                else:
                    temp = node
                    node.parent.rightchild = None
                    del temp
                self.sz -= 1
            # Recurse to children
            delete(node.leftchild)
            delete(node.rightchild)
        
        delete(self.root)
        
        # Return updated node list
        newNodes = [None]
        level = 0
        while True:
            nodes = self.getNodesAtALevel(level)
            level += 1
            if nodes:
                newNodes.extend(nodes)
            else:
                return newNodes
    
    # def deleteNode(self,node):
    #     def delete(currnode):
    #         if currnode is None:
    #             return
    #         if currnode == node:
    #             if currnode.parent:
    #                 if currnode.leftchild and currnode.rightchild:
    #                     print("Cannot delete a node with 2 children!!")
    #                     return
    #                 if currnode.leftchild:
    #                     temp = currnode
    #                     currnode.parent.leftchild = currnode.leftchild
    #                     del temp
    #                 else:
    #                     temp = currnode
    #                     currnode.parent.rightchild = currnode.rightchild
    #                     del temp
    #         delete(currnode.leftchild)
    #         delete(currnode.rightchild)
    #     delete(self.root)
    #     newNodes = [None]
    #     level = 0
    #     while True:
    #         nodes = self.getNodesAtALevel(level)
    #         level += 1
    #         if nodes:
    #             newNodes.extend(nodes)
    #         else:
    #             return newNodes

    def deleteNode(self, node):
        """
        Delete a specific node from the tree.
        Node must not be root and must have at most one child.
        
        Args:
            node: The node to delete
            
        Raises:
            Prints warning if node is root or has two children
        """
        # Cannot delete root
        if not node.parent:
            print("Root of the tree cannot be deleted!!")
            return
        
        # Cannot delete node with two children
        if node.leftchild != None and node.rightchild != None:
            print("A node with 2 children cannot be deleted!!")
            return
        
        # Replace node in parent with its single child (if any)
        if node.parent.leftchild == node:
            if node.leftchild != None:
                node.parent.leftchild = node.leftchild
            else:
                node.parent.leftchild = node.rightchild
        elif node.leftchild != None:
            node.parent.rightchild = node.leftchild
        else:
            node.parent.rightchild = node.rightchild
        
        # Return updated node list
        newNodes = []
        level = 0
        while True:
            nodes = self.getNodesAtALevel(level)
            level += 1
            if nodes:
                newNodes.extend(nodes)
            else:
                return newNodes
    
    def findAncestors(self, node, ancestors):
        """
        Find all ancestors of a given node (nodes on the path from node to root).
        
        Args:
            node: The node whose ancestors are to be found
            ancestors: List to accumulate ancestor nodes (start with [])
            
        Returns:
            List of all ancestor nodes
        """
        # Base case: node has no parent or is None
        if not node or not node.parent:
            return ancestors
        
        # Add parent to ancestors and continue upward
        ancestors.append(node.parent)
        return self.findAncestors(node.parent, ancestors)

    def findCommonAncestors(self, val1, val2):
        """
        Find the lowest common ancestor (LCA) of two nodes given their values.
        The LCA is the deepest node that is an ancestor of both nodes.
        
        Args:
            val1: Value of first node
            val2: Value of second node
            
        Returns:
            The lowest common ancestor node, or False/None if not found
        """
        # Helper function to find node by value
        def findNode(root, val):
            if not root:
                return None
            if root.element == val:
                return root
            left = findNode(root.leftchild, val)
            if left != None:
                return left
            return findNode(root.rightchild, val)
        
        # Find both nodes in the tree
        node1 = findNode(self.root, val1)
        node2 = findNode(self.root, val2)

        # Both nodes must exist in the tree
        if not node1 or not node2:
            return False

        # If same node, return its parent as LCA
        if node1 == node2:
            return node1.parent if node1.parent else False
        
        # Get all ancestors for both nodes
        ancestors1 = []
        ancestors2 = []
        self.findAncestors(node1, ancestors1)
        self.findAncestors(node2, ancestors2)
        
        # If either node has no ancestors, no common ancestor exists
        if not ancestors1 or not ancestors2:
            print("No common ancestor!!")
            return
        
        # Find first common ancestor in the ancestor chains
        for ancestor in ancestors1:
            if ancestor in ancestors2:
                return ancestor
        
        # If no common ancestor found, return root
        return self.root

    def swapSubtrees(self):
        """
        Swap the left and right subtrees of all nodes in the tree.
        This mirrors/flips the entire binary tree horizontally.
        """
        def swap(node):
            # Base case: empty node
            if not node:
                return
            
            # Swap left and right children
            node.leftchild, node.rightchild = node.rightchild, node.leftchild
            
            # Recursively swap in both subtrees
            swap(node.leftchild)
            swap(node.rightchild)

        swap(self.root)


    
if __name__ == '__main__':
    tree = BinaryTree()
    # arr = list(map(int,input().split()))
    arr = [None,1,2,3,4,5,6,7,8,9]
    nlist = tree.buildTree(arr)
    # print(tree.inorderTraverse())
    # print(tree.preorderTraverse())
    # print(tree.postorderTraverse())
    # print(tree.findSibling(nlist[4]))
    # print(tree.findCousins(nlist[5]))
    # tree.displayTree()
    # print(tree.getLeaves())
    # print('\n',tree.getNodesAtALevel(3))
    # nlist = tree.deleteLeaves()
    # print(arr)
    # print(tree.calculateHeight())
    # print(tree.findDepthofNode(nlist[1],nlist[9],0))
    # print(tree.findDepth())
    # print(tree.findHeightOfNode(nlist[5]))

    # for i in range(23,38):
    #     nlist = tree.insertNode(i)
    # tree.displayTree()
    # for node in nlist:
    #     if node:
    #         print(node.element,end=' ')
    print(tree.eulerTourTraversal())
    # print(tree.findCommonAncestors(13,12).element)
    # print(tree.findDepthofNode(tree.root,nlist[11],0))