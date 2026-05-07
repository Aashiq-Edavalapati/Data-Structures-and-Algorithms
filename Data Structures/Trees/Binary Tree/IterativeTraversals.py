"""
Iterative Traversal Methods for Binary Trees.

This module provides iterative traversal functions for binary trees using stacks and queues.
These functions work with BinaryTree instances without modifying the original structure.
Iterative approaches are useful for avoiding recursion depth issues with very deep trees.
"""

from BinaryTree import BinaryTree


def inorderTraverseIterative(tree):
    """
    Perform in-order traversal iteratively using a stack (Left, Root, Right).
    For a Binary Search Tree, this produces elements in sorted order.
    
    Args:
        tree: A BinaryTree instance
        
    Returns:
        List of elements in in-order sequence
    """
    traversal = []
    stack = []
    node = tree.root
    
    # Continue while there are nodes to process
    while stack or node:
        # Go to the leftmost node
        if node:
            stack.append(node)
            node = node.leftchild
        else:
            # Current node is None, pop from stack
            node = stack.pop()
            traversal.append(node.element)  # Visit node
            # Visit right subtree
            node = node.rightchild
    
    return traversal


def preorderTraverseIterative(tree):
    """
    Perform pre-order traversal iteratively using a stack (Root, Left, Right).
    Useful for creating a copy of the tree without recursion depth issues.
    
    Args:
        tree: A BinaryTree instance
        
    Returns:
        List of elements in pre-order sequence
    """
    if not tree.root or not tree.root.element:
        return []
    
    traversal = []
    stack = [tree.root]
    
    # Process each node from the stack
    while stack:
        node = stack.pop()
        traversal.append(node.element)  # Visit node first
        
        # Push right child first so left is processed first
        if node.rightchild:
            stack.append(node.rightchild)
        if node.leftchild:
            stack.append(node.leftchild)
    
    return traversal


def postorderTraverseIterative(tree):
    """
    Perform post-order traversal iteratively using two stacks (Left, Right, Root).
    Useful for deleting trees without using recursion.
    
    Args:
        tree: A BinaryTree instance
        
    Returns:
        List of elements in post-order sequence
    """
    if not tree.root or not tree.root.element:
        return []
    
    traversal = []
    stack1 = [tree.root]
    stack2 = []
    
    # Fill stack2 with reverse post-order
    while stack1:
        node = stack1.pop()
        stack2.append(node)
        
        # Push left and right (note: order is reversed for post-order)
        if node.leftchild:
            stack1.append(node.leftchild)
        if node.rightchild:
            stack1.append(node.rightchild)
    
    # Pop from stack2 to get post-order sequence
    while stack2:
        node = stack2.pop()
        traversal.append(node.element)
    
    return traversal


def postorderTraverseIterativeOneStack(tree):
    """
    Perform post-order traversal iteratively using a single stack.
    Alternative approach that tracks visited nodes.
    
    Args:
        tree: A BinaryTree instance
        
    Returns:
        List of elements in post-order sequence
    """
    if not tree.root or not tree.root.element:
        return []
    
    traversal = []
    stack = []
    node = tree.root
    last_visited = None
    
    # Continue while there are nodes to process
    while stack or node:
        if node:
            # Go to the leftmost node
            stack.append(node)
            node = node.leftchild
        else:
            # Peek at the stack top
            peek_node = stack[-1]
            
            # If right child exists and not visited yet, go to right child
            if peek_node.rightchild and last_visited != peek_node.rightchild:
                node = peek_node.rightchild
            else:
                # Process current node
                traversal.append(peek_node.element)
                last_visited = stack.pop()
    
    return traversal


def levelOrderTraverseIterative(tree):
    """
    Perform level-order (breadth-first) traversal iteratively using a queue.
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
    
    # Process nodes level by level
    while queue:
        node = queue.pop(0)
        traversal.append(node.element)
        
        if node.leftchild:
            queue.append(node.leftchild)
        if node.rightchild:
            queue.append(node.rightchild)
    
    return traversal


def spiralTraversal(tree):
    """
    Perform spiral level-order traversal (zigzag pattern).
    Alternates between left-to-right and right-to-left at each level.
    
    Args:
        tree: A BinaryTree instance
        
    Returns:
        List of elements in spiral order
    """
    if not tree.root or not tree.root.element:
        return []
    
    traversal = []
    queue = [tree.root]
    left_to_right = True
    
    while queue:
        level_size = len(queue)
        current_level = []
        
        # Process all nodes at current level
        for _ in range(level_size):
            node = queue.pop(0)
            current_level.append(node.element)
            
            if node.leftchild:
                queue.append(node.leftchild)
            if node.rightchild:
                queue.append(node.rightchild)
        
        # Add level in appropriate direction
        if left_to_right:
            traversal.extend(current_level)
        else:
            traversal.extend(reversed(current_level))
        
        left_to_right = not left_to_right
    
    return traversal
