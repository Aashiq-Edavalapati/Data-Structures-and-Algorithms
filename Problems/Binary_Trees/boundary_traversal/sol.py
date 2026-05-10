# Link: https://www.geeksforgeeks.org/problems/boundary-traversal-of-binary-tree/1

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

def boundaryTraversal(root):
    if not root: return []
    if not root.left and not root.right: return [root.val]
    
    traversal = [root.val]
    
    # Left boundary excluding leftmost leaf
    if root.left:
        node = root.left
        while node.left or node.right:
            traversal.append(node.val)
            if node.left:
                node = node.left
            else:
                node = node.right
    
    # Leaf nodes using in-order traversal
    stack = [root]
    while stack:
        curr = stack.pop()
        if not curr.left and not curr.right:
            traversal.append(curr.val)
        if curr.right: stack.append(curr.right)
        if curr.left: stack.append(curr.left)
        
    # Right boundary excluding rightmost leaf
    if not root.right:
        return traversal
    stack = []
    node = root.right
    while node.left or node.right:
        stack.append(node.val)
        if node.right:
            node = node.right
        else:
            node = node.left
    
    while stack:
        traversal.append(stack.pop())
    
    return traversal
	

if __name__ == '__main__':
	testCases = [
		[1, None, 2, 3, 4, None, None, None, None],
        [1, 2, None, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, None, None],
        [1, 2, 3, 4, 5, 6, 7, None, None, 8, 9, None, None, None, None]
	]

	for i, testCase in enumerate(testCases):
		root = build_tree_from_list(testCase)
		print(f"Testcase {i}:- i/p: {testCase}")
		print(f"Output: {boundaryTraversal(root)}")