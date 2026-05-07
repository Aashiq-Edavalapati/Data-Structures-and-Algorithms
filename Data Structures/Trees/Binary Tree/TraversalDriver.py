"""
Driver script for testing recursive and iterative binary tree traversals.

Run this file directly to verify that all traversal implementations
produce the expected order on a sample tree.
"""

from pathlib import Path
import sys

CURRENT_DIR = Path(__file__).resolve().parent
if str(CURRENT_DIR) not in sys.path:
    sys.path.insert(0, str(CURRENT_DIR))

from BinaryTree import BinaryTree
from RecursiveTraversals import (
    inorderTraverse,
    preorderTraverse,
    postorderTraverse,
    eulerTourTraversal,
    levelOrderTraverse,
)
from IterativeTraversals import (
    inorderTraverseIterative,
    preorderTraverseIterative,
    postorderTraverseIterative,
    postorderTraverseIterativeOneStack,
    postorderTraversalIterativeModifiedPreorder,
    levelOrderTraverseIterative,
    allTraversals,
    spiralTraversal,
)


def build_sample_tree():
    """
    Build a sample binary tree using level-order indexing.

    Tree shape:
    1 as root, with 2 and 3 as children, and 4, 5, 6, 7 on the last level.
    """
    tree = BinaryTree()
    tree.buildTree([None, 1, 2, 3, 4, 5, 6, 7])
    return tree


def print_traversal_results(tree):
    """Print the output of every traversal function for the given tree."""
    print("Sample tree:")
    tree.displayTree()
    print()

    print("Recursive traversals:")
    print("In-order:     ", inorderTraverse(tree))
    print("Pre-order:    ", preorderTraverse(tree))
    print("Post-order:   ", postorderTraverse(tree))
    print("Euler tour:   ", eulerTourTraversal(tree))
    print("Level-order:  ", levelOrderTraverse(tree))
    print()

    print("Iterative traversals:")
    print("In-order:     ", inorderTraverseIterative(tree))
    print("Pre-order:    ", preorderTraverseIterative(tree))
    print("Post-order 2S:", postorderTraverseIterative(tree))
    print("Post-order 1S:", postorderTraverseIterativeOneStack(tree))
    print("Post-order (Modified Pre-Order):", postorderTraversalIterativeModifiedPreorder(tree))
    print("All Traversals: ", allTraversals(tree))
    print("Level-order:  ", levelOrderTraverseIterative(tree))
    print("Spiral order: ", spiralTraversal(tree))


if __name__ == "__main__":
    sample_tree = build_sample_tree()
    print_traversal_results(sample_tree)
