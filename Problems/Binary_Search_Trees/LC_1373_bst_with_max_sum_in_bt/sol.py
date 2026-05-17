# Link: https://leetcode.com/problems/maximum-sum-bst-in-binary-tree/

"""
    @question:
        Given a binary tree root, return the maximum sum of all keys of any sub-tree which is also a Binary Search Tree (BST).

        Assume a BST is defined as follows:

            The left subtree of a node contains only nodes with keys less than the node's key.
            The right subtree of a node contains only nodes with keys greater than the node's key.
            Both the left and right subtrees must also be binary search trees.

    --------------------------------------------------------------------------------------
    --------------------------------------------------------------------------------------

        Example 1:
            Input: root = [1,4,3,2,4,2,5,null,null,null,null,null,null,4,6]
            Output: 20
            Explanation: Maximum sum in a valid Binary search tree is obtained in root node with key equal to 3.

        --------------------------------------------------------------------------------------
            
        Example 2:
            Input: root = [4,3,null,1,2]
            Output: 2
            Explanation: Maximum sum in a valid Binary search tree is obtained in a single root node with key equal to 2.

        --------------------------------------------------------------------------------------
        
        Example 3:
            Input: root = [-4,-2,-5]
            Output: 0
            Explanation: All values are negatives. Return an empty BST.

    --------------------------------------------------------------------------------------
    --------------------------------------------------------------------------------------

        Constraints:
            The number of nodes in the tree is in the range [1, 4 * 10^4].
            -4 * 10^4 <= Node.val <= 4 * 10^4
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

def maxSumBST(root: Optional[TreeNode]) -> int:
    maxSum = 0
    def findMaxSumBST(node):
        nonlocal maxSum
        if not node: return (True, float('inf'), float('-inf'), 0)

        l_isBST, l_min, l_max, l_sum = findMaxSumBST(node.left)
        r_isBST, r_min, r_max, r_sum = findMaxSumBST(node.right)

        if l_isBST and r_isBST and l_max < node.val < r_min:
            currSum = l_sum + r_sum + node.val
            maxSum = max(maxSum, currSum)

            return (True, min(l_min, node.val), max(r_max, node.val), currSum)
        
        return (False, 0, 0, 0)

    findMaxSumBST(root)
    return maxSum

if __name__ == '__main__':
    testCases = [
        [1,4,3,2,4,2,5,None,None,None,None,None,None,4,6],
        [4,3,None,1,2],
        [-4,-2,-5]
    ]

    for i, tree in enumerate(testCases):
        root = build_tree_from_list(tree)

        print(f"Testcase {i}:")
        print(f"Input: root: \n")
        display_tree(root)
        ans = maxSumBST(root)
        print(f"Output: maxSum={ans}")