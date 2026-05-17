# Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/

"""
    @question:
        Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

    --------------------------------------------------------------------------------------
    --------------------------------------------------------------------------------------

        Example 1:
            Input: root = [3,1,4,null,2], k = 1
            Output: 1

        --------------------------------------------------------------------------------------
            
        Example 2:
            Input: root = [5,3,6,2,4,null,null,1], k = 3
            Output: 3

    --------------------------------------------------------------------------------------
    --------------------------------------------------------------------------------------

        Constraints:
            The number of nodes in the tree is n.
            1 <= k <= n <= 104
            0 <= Node.val <= 104
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

def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    stack = [root]
    cnt = 0
    curr = root
    while curr or stack:
        if not curr:
            node = stack.pop()
            cnt += 1
            if cnt == k: return node.val
            if node.right: 
                stack.append(node.right)
                curr = node.right
            continue

        if curr.left: stack.append(curr.left)
        curr = curr.left

if __name__ == '__main__':
    testCases = [
        [[3,1,4,None,2], 1],
        [[5,3,6,2,4,None,None,1], 3]
    ]

    for i, (tree, k) in enumerate(testCases):
        root = build_tree_from_list(tree)

        print(f"Testcase {i}:")
        print(f"Input: k={k}, root: \n")
        display_tree(root)
        ans = kthSmallest(root, k)
        print(f"Output: ans={ans}")