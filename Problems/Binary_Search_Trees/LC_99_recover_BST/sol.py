# Link: https://leetcode.com/problems/recover-binary-search-tree/

"""
    @question:
        You are given the root of a binary search tree (BST), where the values of exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

    --------------------------------------------------------------------------------------
    --------------------------------------------------------------------------------------

        Example 1:
            Input: root = [1,3,null,null,2]
            Output: [3,1,null,null,2]
            Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.

        --------------------------------------------------------------------------------------
            
        Example 2:
            Input: root = [3,1,4,null,null,2]
            Output: [2,1,4,null,null,3]
            Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.

    --------------------------------------------------------------------------------------
    --------------------------------------------------------------------------------------

        Constraints:
            The number of nodes in the tree is in the range [2, 1000].
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

def recoverTree(root: Optional[TreeNode]) -> None:
    """
    Do not return anything, modify root in-place instead.
    """
    first, second, prev = None, None, None
    def checkAndMark(node):
        nonlocal first, second, prev
        if not node: return
        checkAndMark(node.left)
        if prev and prev.val > node.val:
            if not first:
                first = prev
                second = node
            else: 
                second = node
                return
        prev = node
        checkAndMark(node.right)
    
    checkAndMark(root)
    first.val, second.val = second.val, first.val

if __name__ == '__main__':
    testCases = [
        [1,3,None,None,2],
        [3,1,4,None,None,2]
    ]

    for i, tree in enumerate(testCases):
        root = build_tree_from_list(tree)

        print(f"Testcase {i}:")
        print(f"Input: root: \n")
        display_tree(root)
        recoverTree(root)
        print(f"Output: \n")
        display_tree(root)