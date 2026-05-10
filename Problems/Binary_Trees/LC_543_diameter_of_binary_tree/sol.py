# Link: https://leetcode.com/problems/diameter-of-binary-tree/

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


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
	ans = [0]
	
	def helper(node, ans):
		if not node: return 0

		left = helper(node.left, ans)
		right = helper(node.right, ans)
		
		ans[0] = max(ans[0], left + right)
		
		return 1 + max(left, right)
    
	helper(root, ans)
	return ans[0]

if __name__ == '__main__':
	testCases = [
		[1,2,3,4,5],
		[1,2],
		[1, 2, 3, 4, 5, None, None, 8, None, None, 6, 9, None, None, 7]
	]

	for i, testCase in enumerate(testCases):
		root = build_tree_from_list(testCase)
		print(f"Testcase {i}:- i/p: {testCase}")
		print(f"Output: {diameterOfBinaryTree(root)}")