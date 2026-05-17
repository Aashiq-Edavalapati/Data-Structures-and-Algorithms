# Link: https://leetcode.com/problems/validate-binary-search-tree/

"""
    @question:
        Given the root of a binary tree, determine if it is a valid binary search tree (BST).

        A valid BST is defined as follows:

            The left of a node contains only nodes with keys strictly less than the node's key.
            The right subtree of a node contains only nodes with keys strictly greater than the node's key.
            Both the left and right subtrees must also be binary search trees.

    --------------------------------------------------------------------------------------
    --------------------------------------------------------------------------------------

        Example 1:
            Input: root = [2,1,3]
            Output: true

        --------------------------------------------------------------------------------------
            
        Example 2:
            Input: root = [5,1,4,null,null,3,6]
            Output: false
            Explanation: The root node's value is 5 but its right child's value is 4.

    --------------------------------------------------------------------------------------
    --------------------------------------------------------------------------------------

        Constraints:
            The number of nodes in the tree is in the range [1, 104].
            -231 <= Node.val <= 231 - 1
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

def isValidBST(root: Optional[TreeNode]) -> bool:
    def valid(root, mini, maxi):
        if not root: return True
        if root.val <= mini or root.val >= maxi: return False

        return valid(root.left, mini, root.val) and valid(root.right, root.val, maxi)
    
    return valid(root, float('-inf'), float('inf'))

if __name__ == '__main__':
    testCases = [
        [2,1,3],
        [5,1,4,None,None,3,6]
    ]

    for i, tree in enumerate(testCases):
        root = build_tree_from_list(tree)

        print(f"Testcase {i}:")
        print(f"Input: root: \n")
        display_tree(root)
        ans = isValidBST(root)
        print(f"Output: isValidBST={ans}")