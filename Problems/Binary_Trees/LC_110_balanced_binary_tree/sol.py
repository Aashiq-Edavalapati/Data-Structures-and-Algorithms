# Link: https://leetcode.com/problems/balanced-binary-tree/

from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path


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


def isBalanced(root: TreeNode | None) -> bool:
	"""
	Determine if a binary tree is balanced.
	
	A balanced binary tree is one where the heights of the left and right 
	subtrees of every node differ by at most 1.
	
	Args:
		root: The root node of the binary tree
		
	Returns:
		True if the tree is balanced, False otherwise
	"""
	def helper(node):
		if not node:
			return 0

		left = helper(node.left)
		if left == -1:
			return -1

		right = helper(node.right)
		if right == -1:
			return -1

		if abs(left - right) > 1:
			return -1

		return 1 + max(left, right)

	return helper(root) != -1


if __name__ == "__main__":
	# Test case 1: Balanced tree
	#       3
	#      / \
	#     9  20
	#       /  \
	#      15   7
	tree1_values = [3, 9, 20, None, None, 15, 7]
	tree1_root = build_tree_from_list(tree1_values)
	
	print("Test case 1 (Balanced tree):")
	print(f"Input: {tree1_values}")
	print(f"Expected: True, Got: {isBalanced(tree1_root)}\n")
	
	# Test case 2: Unbalanced tree
	#       1
	#      /
	#     2
	#    /
	#   3
	tree2_values = [1, 2, None, 3]
	tree2_root = build_tree_from_list(tree2_values)
	
	print("Test case 2 (Unbalanced tree):")
	print(f"Input: {tree2_values}")
	print(f"Expected: False, Got: {isBalanced(tree2_root)}\n")
	
	# Test case 3: Single node (balanced)
	tree3_values = [1]
	tree3_root = build_tree_from_list(tree3_values)
	
	print("Test case 3 (Single node):")
	print(f"Input: {tree3_values}")
	print(f"Expected: True, Got: {isBalanced(tree3_root)}\n")
	
	# Test case 4: Empty tree (balanced)
	tree4_values = []
	tree4_root = build_tree_from_list(tree4_values)
	
	print("Test case 4 (Empty tree):")
	print(f"Input: {tree4_values}")
	print(f"Expected: True, Got: {isBalanced(tree4_root)}\n")

	# Test case 5
	tree5_values = [3, 9, 20, None, None, 15, 7]
	tree5_root = build_tree_from_list(tree5_values)

	print(f"Input: {tree5_values}")
	print(f"Expected: True, Got: {isBalanced(tree5_root)}\n")

	# Test case 6
	tree6_values = [1, 2, 2, 3, 3, None, None, 4, 4]
	tree6_root = build_tree_from_list(tree6_values)

	print(f"Input: {tree6_values}")
	print(f"Expected: True, Got: {isBalanced(tree6_root)}\n")