# Link: https://www.geeksforgeeks.org/problems/root-to-leaf-paths/1

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

def allRootToLeaves(root: Optional[TreeNode]) -> List[List[int]]:
    if not root: return []
    path = []
    paths = []
    
    def helper(node, path):
        nonlocal paths
        if not node: return
        
        path.append(node.val)
        if not node.left and not node.right:
            paths.append(path[:])
            path.pop()
            return
        helper(node.left, path)
        helper(node.right, path)
        path.pop()
    
    helper(root, path)
    return paths
    

if __name__ == '__main__':
	testCases = [
        [1, 2, 3, None, 5, None, 4],
		[1, 2, 3],
		[1,2,2,3,4,4,3],
        [1, 2, None, 3, 4, 5, 6, 7, 8],
        [1, 2, 4, 5, None, None, 6, 7, 8, 9]
	]

	for i, testCase in enumerate(testCases):
		root = build_tree_from_list(testCase)
		print(f"Testcase {i}:- i/p: {testCase}")
		print(f"Output: {allRootToLeaves(root)}")