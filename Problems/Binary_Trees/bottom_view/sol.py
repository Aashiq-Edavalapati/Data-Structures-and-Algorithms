# Link: https://www.geeksforgeeks.org/problems/top-view-of-binary-tree/1

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


def bottomView(root: Optional[TreeNode]) -> List[int]:
    """
        @intuition: 
            Last element of every col from left to right
    """
    q = [(0, root)] # (x, node)
    vals = {}
    minCol, maxCol = 0, 0
    
    while q:
        size = len(q)
        
        for _ in range(size):
            col, curr = q.pop(0)
            minCol = min(minCol, col)
            maxCol = max(maxCol, col)
            vals[col] = curr.val
            
            if curr.left: q.append((col - 1, curr.left))
            if curr.right: q.append((col + 1, curr.right))
    
    return [vals[k] for k in range(minCol, maxCol +  1)]
    

if __name__ == '__main__':
	testCases = [
		[1, 2, 3],
        [1, 2, None, 3, 4, 5, 6, 7, 8],
        [1, 2, 4, 5, None, None, 6, 7, 8, 9]
	]

	for i, testCase in enumerate(testCases):
		root = build_tree_from_list(testCase)
		print(f"Testcase {i}:- i/p: {testCase}")
		print(f"Output: {bottomView(root)}")