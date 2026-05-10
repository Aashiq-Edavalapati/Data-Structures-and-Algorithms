# Link: https://leetcode.com/problems/same-tree/

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

BinaryTree = _binary_tree_module.BinaryTree
TreeNode = _binary_tree_module.TreeNode
build_tree_from_list = _binary_tree_module.build_tree_from_list

def isSameTree(root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
    if not root1 and not root2: return True
    
    if root1 and root2 and root1.val == root2.val:
        return isSameTree(root1.left, root2.left) and isSameTree(root1.right, root2.right)

    return False
	

if __name__ == '__main__':
	testCases = [
		[[1,2,3], [1,2,3]],
		[[1,2], [1, None,2]],
		[[1,2,1], [1,1,2]]
	]

	for i, testCase in enumerate(testCases):
		root1, root2 = build_tree_from_list(testCase[0]), build_tree_from_list(testCase[1])
		print(f"Testcase {i}:- i/p: {testCase}")
		print(f"Output: {isSameTree(root1, root2)}")