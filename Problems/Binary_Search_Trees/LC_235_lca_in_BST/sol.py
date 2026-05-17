# Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

"""
    @question:
        Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

        According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

    --------------------------------------------------------------------------------------
    --------------------------------------------------------------------------------------

        Example 1:
            Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
            Output: 6
            Explanation: The LCA of nodes 2 and 8 is 6.

        --------------------------------------------------------------------------------------
            
        Example 2:
            Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
            Output: 2
            Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

        --------------------------------------------------------------------------------------
            
        Example 3:
            Input: root = [2,1], p = 2, q = 1
            Output: 2

    --------------------------------------------------------------------------------------
    --------------------------------------------------------------------------------------

        Constraints:
            The number of nodes in the tree is in the range [2, 105].
            -109 <= Node.val <= 109
            All Node.val are unique.
            p != q
            p and q will exist in the BST.
"""

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

_TREE_UTILS_PATH = (
    Path(__file__).resolve().parents[3]
    / "Data Structures"
    / "Trees"
    / "Binary Tree"
    / "tree_utils.py"
)

_tree_utils_spec = spec_from_file_location("tree_utils", _TREE_UTILS_PATH)
if _tree_utils_spec is None or _tree_utils_spec.loader is None:
    raise ImportError(f"Cannot load tree_utils from {_TREE_UTILS_PATH}")

_tree_utils_module = module_from_spec(_tree_utils_spec)
_tree_utils_spec.loader.exec_module(_tree_utils_module)

display_tree = _tree_utils_module.display_tree

BinaryTree = _binary_tree_module.BinaryTree
TreeNode = _binary_tree_module.TreeNode
build_tree_from_list = _binary_tree_module.build_tree_from_list

def lowestCommonAncestor(root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    if not root:
        return None

    if root == p or root == q: return root
    if p.val < root.val < q.val or q.val < root.val < p.val: return root

    if p.val < root.val and q.val < root.val: return lowestCommonAncestor(root.left, p, q)
    
    return lowestCommonAncestor(root.right, p, q)

def find_node(root: 'TreeNode', target: int) -> 'TreeNode':
    """Find a node by value in a LeetCode-style TreeNode tree."""
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
        [[6,2,8,0,4,7,9,None,None,3,5], 2, 8],
        [[6,2,8,0,4,7,9,None,None,3,5], 2, 4],
        [[2,1], 2, 1]
    ]

    for i, (values, p_val, q_val) in enumerate(testCases):
        root = build_tree_from_list(values)

        p = find_node(root, p_val)
        q = find_node(root, q_val)

        print(f"Testcase {i}:")
        print("Input: root:\n")
        display_tree(root)

        ans = lowestCommonAncestor(root, p, q)
        print(f"Output: lca={ans.val if ans else None}")