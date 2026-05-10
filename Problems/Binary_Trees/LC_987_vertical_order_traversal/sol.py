# Link: https://leetcode.com/problems/vertical-order-traversal-of-a-binary-tree/

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from typing import Optional, List
from collections import defaultdict


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

BinaryTree = _binary_tree_module.BinaryTree
TreeNode = _binary_tree_module.TreeNode
build_tree_from_list = _binary_tree_module.build_tree_from_list


def verticalTraversal(root: Optional[TreeNode]) -> List[List[int]]:
    """
        @Intuition:
            Since we need to find the levels and col num, we can label each node with row and col number. Then we can go col by col and sort by levels and then by values among els of same row(level) and col
    """
    colDict = defaultdict(list)
    
    def labelCols(node, row, col):
        nonlocal colDict

        if not node: return

        colDict[col].append((row, node.val))
        labelCols(node.left, row + 1, col - 1)
        labelCols(node.right, row + 1, col + 1)
    
    labelCols(root, 0, 0)

    traversal = []
    keys = sorted(list(colDict.keys()))
    for key in keys:
        row = sorted(colDict[key], key=lambda x : (x[0], x[1]))
        traversal.append([r[1] for r in row])
    
    return traversal

"""
    Alternative solutions:
        1. Can use nested hashmap with row as key and min heap as the value instead of a linear map with a tuple of unsorted els as value.
        2. Can use any traversal.
"""

if __name__ == '__main__':
	testCases = [
		[3,9,20,None,None,15,7],
        [1,2,3,4,5,6,7],
        [1,2,3,4,6,5,7],
        [3,1,4,0,2,2]
	]

	for i, testCase in enumerate(testCases):
		root = build_tree_from_list(testCase)
		print(f"Testcase {i}:- i/p: {testCase}")
		print(f"Output: {verticalTraversal(root)}")