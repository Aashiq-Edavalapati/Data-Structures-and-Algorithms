# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

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

TreeNode = _binary_tree_module.TreeNode
build_tree_from_list = _binary_tree_module.build_tree_from_list


def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    """
        @intuition:
            - Just do a normal traversal as we do in all the tree problems.
			- Backtrack if either one of the p or q is found or traversed till the end.
			- When backtracking, the 1st node that recieves both p and q at the same time one from the left and one from the right, then that node is the lowest common ancestor.
	"""
    if not root: return
    if root == p or root == q: return root

    left = lowestCommonAncestor(root.left, p, q)
    right = lowestCommonAncestor(root.right, p, q)

    if left and right: return root
    if left: return left
    return right

def find_node(root: 'TreeNode', target: int) -> 'TreeNode':
	if not root:
		return None
	if root.val == target:
		return root

	left = find_node(root.left, target)
	if left:
		return left
	return find_node(root.right, target)


if __name__ == '__main__':
	testCases = [
		[[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 1],
		[[3, 5, 1, 6, 2, 0, 8, None, None, 7, 4], 5, 4],
	]

	for i, (values, p_val, q_val) in enumerate(testCases):
		root = build_tree_from_list(values)
		p = find_node(root, p_val)
		q = find_node(root, q_val)
		ancestor = lowestCommonAncestor(root, p, q)

		print(f"Testcase {i}:")
		print(f"Input: values={values}, p={p_val}, q={q_val}")
		print(f"Output: {ancestor.val if ancestor else None}")