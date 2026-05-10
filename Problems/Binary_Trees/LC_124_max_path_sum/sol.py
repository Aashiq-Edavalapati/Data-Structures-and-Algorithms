# Link: https://leetcode.com/problems/binary-tree-maximum-path-sum/

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

def maxPathSum(root: Optional[TreeNode]) -> int:
    maxSum = [float('-inf')]
	
    def helper(node, maxSum):
        if not node: return 0
		
        leftMax = max(0, helper(node.left, maxSum))
        rightMax = max(0, helper(node.right, maxSum))
		
        maxSum[0] = max(maxSum[0], node.val + leftMax + rightMax)
		
        return node.val + max(leftMax, rightMax)

    helper(root, maxSum)
    return maxSum[0]

if __name__ == '__main__':
	testCases = [
		[5,4,8,11,None,13,4,7,2,None,None,None,1],
		[1,2,3],
		[-10,9,20,None,None,15,7],
		[-10,9,20,None,None,15,-7],
        [-1,-2,-3]
	]

	for i, testCase in enumerate(testCases):
		root = build_tree_from_list(testCase)
		print(f"Testcase {i}:- i/p: {testCase}")
		print(f"Output: {maxPathSum(root)}")