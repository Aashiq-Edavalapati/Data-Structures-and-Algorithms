# Link: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/

"""
    @question:
        Given an array of integers preorder, which represents the preorder traversal of a BST (i.e., binary search tree), construct the tree and return its root.

        It is guaranteed that there is always possible to find a binary search tree with the given requirements for the given test cases.

        A binary search tree is a binary tree where for every node, any descendant of Node.left has a value strictly less than Node.val, and any descendant of Node.right has a value strictly greater than Node.val.

        A preorder traversal of a binary tree displays the value of the node first, then traverses Node.left, then traverses Node.right.

    --------------------------------------------------------------------------------------
    --------------------------------------------------------------------------------------

        Example 1:
            Input: preorder = [8,5,1,7,10,12]
            Output: [8,5,10,1,7,null,12]

        --------------------------------------------------------------------------------------
            
        Example 2:
            Input: preorder = [1,3]
            Output: [1,null,3]

    --------------------------------------------------------------------------------------
    --------------------------------------------------------------------------------------

        Constraints:
            1 <= preorder.length <= 100
            1 <= preorder[i] <= 1000
            All the values of preorder are unique.
"""
from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from typing import Optional, List

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

def bstFromPreorder(preorder: List[int]) -> Optional[TreeNode]:
    def build(pre, start, end):
        if start > end: return
        if start == len(pre) - 1: return TreeNode(pre[start])
        root = TreeNode(pre[start])
        if pre[start + 1] > pre[start]:
            root.right = build(pre, start + 1, end)
            return root
        for i in range(start + 2, end + 1):
            if pre[i] > pre[start]:
                root.left = build(pre, start + 1, i - 1)
                root.right = build(pre, i, end)
                return root

        root.left = build(pre, start + 1, end)
        return root
    
    return build(preorder, 0, len(preorder) - 1)

if __name__ == '__main__':
    testCases = [
        [8,5,1,7,10,12],
        [1,3]
    ]

    for i, preorder in enumerate(testCases):
        print(f"Testcase {i}:")
        print(f"Input: preorder={preorder}")
        root = bstFromPreorder(preorder)
        print(f"Output: tree: \n")
        display_tree(root)