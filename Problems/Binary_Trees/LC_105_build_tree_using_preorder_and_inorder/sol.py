# Link: https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/

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


def buildTree(preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
    if not preorder: return
    inMap = {}
    for i, val in enumerate(inorder):
        inMap[val] = i
    n = len(inorder)

    return helper(preorder, inorder, inMap, 0, n - 1, 0, n - 1)

def helper(preorder: List[int], inorder: List[int], inMap, inStart: int, inEnd: int, preStart: int, preEnd: int) -> Optional[TreeNode]:
    if not preorder: return
    node = TreeNode(preorder[preStart])
    ind = inMap[node.val]
    node.left = (preorder, inorder, inMap, 0, ind - 1, preStart + 1, ind)
    node.right = (preorder, inorder, inMap, ind + 1, inEnd, ind + 1, preEnd)

    return node

if __name__ == '__main__':
    testCases = [
        [[3,9,20,15,7], [9,3,15,20,7]],
        [[-1], [-1]],
        [[3,9,10,11,20,15,7], [10,11,9,3,15,20,7]]
    ]

    for i, (preorder, inorder) in enumerate(testCases):
        result = buildTree(preorder, inorder)

        print(f"Testcase {i}:")
        print(f"Input: preorder={preorder}, inorder={inorder}")
        print(f"Output root: {result.val if result else None}")