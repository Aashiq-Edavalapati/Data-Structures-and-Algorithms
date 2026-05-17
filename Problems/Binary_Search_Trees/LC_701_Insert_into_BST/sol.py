# Link: https://leetcode.com/problems/insert-into-a-binary-search-tree/

"""
    @question:
        You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

        Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

    --------------------------------------------------------------------------------------
    --------------------------------------------------------------------------------------

        Example 1:
            Input: root = [4,2,7,1,3], val = 5
            Output: [4,2,7,1,3,5]
            Explanation: Another accepted tree is:

        --------------------------------------------------------------------------------------
            
        Example 2:
            Input: root = [40,20,60,10,30,50,70], val = 25
            Output: [40,20,60,10,30,50,70,null,null,25]

        --------------------------------------------------------------------------------------
            
        Example 3:
            Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
            Output: [4,2,7,1,3,5]

    --------------------------------------------------------------------------------------
    --------------------------------------------------------------------------------------

        Constraints:
            The number of nodes in the tree will be in the range [0, 104].
            -108 <= Node.val <= 108
            All the values Node.val are unique.
            -108 <= val <= 108
            It's guaranteed that val does not exist in the original BST.
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

def insertIntoBST(root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
    if not root: return TreeNode(val)

    if root.val > val:
        if not root.left: root.left = TreeNode(val)
        else: insertIntoBST(root.left, val)
    else:
        if not root.right: root.right = TreeNode(val)
        else: insertIntoBST(root.right, val)

    return root

if __name__ == '__main__':
    testCases = [
        [[8, 4, 12, 2, 6, 10, 14] , 11],
        [[8, 4, 12, 2, 6, 10, 14] , 15],
        [[8, 4, 12, 2, 6, 10, 14] , 1],
        [[8, 4, 12, 2, 6, 10, 14] , 6]
    ]

    for i, (tree, val) in enumerate(testCases):
        root = build_tree_from_list(tree)

        newRoot = insertIntoBST(root, val)
        print(f"Testcase {i}:")
        print(f"Input: val={val}, root: \n")
        display_tree(root)
        print(f"Output: \n")
        display_tree(newRoot)