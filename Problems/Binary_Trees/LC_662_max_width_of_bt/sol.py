# Link: https://leetcode.com/problems/maximum-width-of-binary-tree/

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


def widthOfBinaryTree(root: Optional[TreeNode]) -> int:
    """
        @intuition:
            # To find:
                Max. no. of nodes b/w any two nodes in a level(Including the imaginary nodes that would have been available if the tree is a complete tree).
            # Approach:
                - One of the common patterns in trees is labelling in a way that makes us easier to visualize the tree using numbers in code.
                    * We need the position of leftmost and rightmost nodes in each level
                    * To label properly including the missing nodes in b/w in that level, we can use indexing in array based representation of the tree.
                        - For ith node considering 0-based indexing:
                            * Left child: 2 * i + 1
                            * Right child: 2 * i + 2
                    * Based on these labels, we can find leftInd, rightInd in each level and find max(rightInd - leftInd + 1) among all the levels
    """                     
    q = [(0, root)] # (index, node)
    maxWidth = 1
    while q:
        size = len(q)
        levelMin, levelMax = float('inf'), 0
        for _ in range(size):
            i, node = q.pop(0)
            if node.left:
                levelMax = 2 * i + 1 # Need not do max() because we are traversing from left to right anyway!
                levelMin = min(levelMin, levelMax)
                q.append((levelMax, node.left))
            if node.right:
                levelMax = 2 * i + 2
                levelMin = min(levelMin, levelMax)
                q.append((levelMax, node.right))
        
        maxWidth = max(maxWidth, levelMax - levelMin + 1)
    
    return maxWidth
    

if __name__ == '__main__':
	testCases = [
		[1,3,2,5,3,None,9],
        [1,3,2,5,None,None,9,6,None,7],
        [1,3,2,5]
	]

	for i, testCase in enumerate(testCases):
		root = build_tree_from_list(testCase)
		print(f"Testcase {i}:- i/p: {testCase}")
		print(f"Output: {widthOfBinaryTree(root)}")