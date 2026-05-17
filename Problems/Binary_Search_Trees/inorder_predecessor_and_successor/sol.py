# Link: https://www.geeksforgeeks.org/problems/predecessor-and-successor/1

"""
    @question:
        You are given the root of a BST and an integer key. You need to find the inorder predecessor and successor of the given key. If either predecessor or successor is not found, then set it to NULL.

        Note: In an inorder traversal the number just smaller than the target is the predecessor and the number just greater than the target is the successor. 

    --------------------------------------------------------------------------------------
    --------------------------------------------------------------------------------------
        
        Examples :
            Input: root = [50, 30, 70, 20, 40, 60, 80], key = 65
            Output: [60, 70]
            Explanation: In the given BST the inorder predecessor of 65 is 60 and inorder successor of 65 is 70.

        --------------------------------------------------------------------------------------

            Input: root = [8, 1, 9, N, 4, N, 10, 3], key = 8
            Output: [4, 9]
            Explanation: In the given BST the inorder predecessor of 8 is 4 and inorder successor of 8 is 9.

        Constraints: 
        1 ≤ no. of nodes ≤ 105
        0 ≤ node->data ≤ 106
        1 ≤ key ≤ 106
"""

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from typing import List

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

def findPreSuc(root, key):
    stack = [root]
    curr = root
    pre, suc = None, None
    while curr or stack:
        if not curr:
            node = stack.pop()
            if key < node.val:
                suc = node
                break
            if node.val < key:
                pre = node
            if node.right:
                curr = node.right
                stack.append(curr)
            continue
        
        if curr.left: stack.append(curr.left)
        curr = curr.left
    
    return [pre, suc]

if __name__ == '__main__':
    testCases = [
        [[50, 30, 70, 20, 40, 60, 80], 65],
        [[8, 1, 9, None, 4, None, 10, 3], 8],
    ]

    for i, (tree, key) in enumerate(testCases):
        root = build_tree_from_list(tree)

        pre, suc = findPreSuc(root, key)
        print(f"Testcase {i}:")
        print(f"Input: val={key}, root: ")
        display_tree(root)
        print(f"Output: predecessor = {pre.val}, successor = {suc.val}")