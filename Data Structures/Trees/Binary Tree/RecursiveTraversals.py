"""
Recursive Traversal Methods for Binary Trees.

This module provides recursive traversal functions for binary trees.
These functions work with BinaryTree instances without modifying the original structure.
"""

from BinaryTree import BinaryTree


def inorderTraverse(tree):
    """
    Perform in-order traversal of the binary tree (Left, Root, Right).
    For a Binary Search Tree, this produces elements in sorted order.
    
    Args:
        tree: A BinaryTree instance
        
    Returns:
        List of elements in in-order sequence
    """
    traversal = []
    
    def inorder(node):
        if node:
            inorder(node.leftchild)  # Visit left subtree
            traversal.append(node.element)  # Visit node
            inorder(node.rightchild)  # Visit right subtree
        return traversal
    
    return inorder(tree.root)


def preorderTraverse(tree):
    """
    Perform pre-order traversal of the binary tree (Root, Left, Right).
    Useful for creating a copy of the tree or prefix expression evaluation.
    
    Args:
        tree: A BinaryTree instance
        
    Returns:
        List of elements in pre-order sequence
    """
    traversal = []
    
    def preorder(node):
        if node:
            traversal.append(node.element)  # Visit node
            preorder(node.leftchild)  # Visit left subtree
            preorder(node.rightchild)  # Visit right subtree
        return traversal
    
    return preorder(tree.root)


def postorderTraverse(tree):
    """
    Perform post-order traversal of the binary tree (Left, Right, Root).
    Useful for deleting trees or evaluating postfix expressions.
    
    Args:
        tree: A BinaryTree instance
        
    Returns:
        List of elements in post-order sequence
    """
    traversal = []
    
    def postorder(node):
        if node:
            postorder(node.leftchild)  # Visit left subtree
            postorder(node.rightchild)  # Visit right subtree
            traversal.append(node.element)  # Visit node
        return traversal
    
    return postorder(tree.root)


def eulerTourTraversal(tree):
    """
    Perform Euler tour traversal of the binary tree.
    Records multiple visits: before left subtree, between subtrees, and after right subtree.
    Useful for computing tree statistics and complex tree problems.
    
    Args:
        tree: A BinaryTree instance
        
    Returns:
        List of elements in Euler tour order
    """
    walk = []
    
    def traversal(node):
        if not node:
            return
        
        # First visit: include internal nodes (nodes with both children)
        if node.leftchild != None and node.rightchild != None:
            walk.append(node.element)
        
        # Traverse left subtree
        if node.leftchild != None:
            traversal(node.leftchild)

        # Traverse right subtree
        if node.rightchild != None:
            traversal(node.rightchild)
        
        # Final visit: include all nodes again
        walk.append(node.element)
    
    traversal(tree.root)
    return walk


def levelOrderTraverse(tree):
    """
    Perform level-order (breadth-first) traversal of the binary tree.
    Visits nodes level by level from left to right.
    
    Args:
        tree: A BinaryTree instance
        
    Returns:
        List of elements in level-order sequence
    """
    if not tree.root or not tree.root.element:
        return []
    
    traversal = []
    queue = [tree.root]
    
    while queue:
        node = queue.pop(0)
        traversal.append(node.element)
        
        if node.leftchild:
            queue.append(node.leftchild)
        if node.rightchild:
            queue.append(node.rightchild)
    
    return traversal
