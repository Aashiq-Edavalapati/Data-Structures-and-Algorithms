# Link: https://leetcode.com/problems/symmetric-tree/

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

BinaryTree = _binary_tree_module.BinaryTree
TreeNode = _binary_tree_module.TreeNode
build_tree_from_list = _binary_tree_module.build_tree_from_list


def isSymmetric(root: Optional[TreeNode]) -> bool:
    if not root: return True
    
    def check(node1, node2):
        if not node1 or not node2: return not node1 and not node2
        return node1.val == node2.val and check(node1.left, node2.right) and check(node1.right, node2.left)

    return check(root.left, root.right)
    

if __name__ == '__main__':
	testCases = [
		[1, 2, 3],
		[1,2,2,3,4,4,3],
        [1, 2, None, 3, 4, 5, 6, 7, 8],
        [1, 2, 4, 5, None, None, 6, 7, 8, 9]
	]

	for i, testCase in enumerate(testCases):
		root = build_tree_from_list(testCase)
		print(f"Testcase {i}:- i/p: {testCase}")
		print(f"Output: {isSymmetric(root)}")