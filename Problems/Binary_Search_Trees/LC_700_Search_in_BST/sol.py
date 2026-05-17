# Link: https://leetcode.com/problems/search-in-a-binary-search-tree/

"""
    @question:
        You are given the root of a binary search tree (BST) and an integer val.

        Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

    -------------------------------------------------------------------------------
    -------------------------------------------------------------------------------
        
        Example 1:
            Input: root = [4,2,7,1,3], val = 2
            Output: [2,1,3]

        -------------------------------------------------------------------------------
            
        Example 2:
            Input: root = [4,2,7,1,3], val = 5
            Output: []

    -------------------------------------------------------------------------------
    -------------------------------------------------------------------------------

        Constraints:

            The number of nodes in the tree is in the range [1, 5000].
            1 <= Node.val <= 107
            root is a binary search tree.
            1 <= val <= 107
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from typing import Optional


_BINARY_TREE_PATH = (
	Path(__file__).resolve().parents[3]
	/ "Data Structures"
	/ "Trees"
	/ "Binary Tree"
	/ "BinaryTree.py"
)

_spec = spec_from_file_location("binary_tree", _BINARY_TREE_PATH)
if _spec is None or _spec.loader is None:
	raise ImportError(f"Cannot load BinaryTree from {_BINARY_TREE_PATH}")

_binary_tree_module = module_from_spec(_spec)
_spec.loader.exec_module(_binary_tree_module)

_TREE_UTILS_PATH = (
    Path(__file__).resolve().parents[3]
    / "Data Structures"
    / "Trees"
    / "Binary Tree"
    / "tree_utils.py"
)

_tree_utils_spec = spec_from_file_location("tree_utils", _TREE_UTILS_PATH)
if _tree_utils_spec is None or _tree_utils_spec.loader is None:
    raise ImportError(f"Cannot load tree_utils from {_TREE_UTILS_PATH}")

_tree_utils_module = module_from_spec(_tree_utils_spec)
_tree_utils_spec.loader.exec_module(_tree_utils_module)

display_tree = _tree_utils_module.display_tree

BinaryTree = _binary_tree_module.BinaryTree
TreeNode = _binary_tree_module.TreeNode
build_tree_from_list = _binary_tree_module.build_tree_from_list

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def searchBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root:
        return None
    
    if root.val == val:
        return root
    
    if root.val > val:
        return searchBST(root.left, val)
    
    return searchBST(root.right, val)
    
if __name__ == '__main__':
    testCases = [
         [[4,2,7,1,3], 2],
         [[4,2,7,1,3], 5]
    ]

    for i, (tree, val) in enumerate(testCases):
        root = build_tree_from_list(tree)

        op = searchBST(root, val)
        print(f"Testcase {i}:")
        print(f"Input: \n\troot:")
        display_tree(tree)
        print(f"\tval={val}")
        if op:
            print("Output subtree:")
            display_tree(op)
        else:
            print("Output: NULL")