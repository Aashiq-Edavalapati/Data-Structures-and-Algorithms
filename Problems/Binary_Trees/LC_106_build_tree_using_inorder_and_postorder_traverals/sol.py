# Link: https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/

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


def buildTree(inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
    n = len(inorder)
    inMap = {val: idx for idx, val in enumerate(inorder)}

    return helper(inorder, postorder, inMap, 0, n - 1, 0, n - 1)

def helper(inorder: List[int], postorder: List[int], inMap, inStart: int, inEnd: int, postStart: int, postEnd: int) -> Optional[TreeNode]:
    if inStart > inEnd or postStart > postEnd: return

    node = TreeNode(postorder[postEnd])
    idx = inMap[node.val]
    numsLeft = idx - inStart

    node.left = helper(inorder, postorder, inMap, inStart, idx - 1, postStart, postStart + numsLeft -1 )
    node.right = helper(inorder, postorder, inMap, idx + 1, inEnd, postStart + numsLeft, postEnd - 1)

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