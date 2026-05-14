# Link: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/

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


def flatten(root: Optional[TreeNode]) -> None:
    if not root:
        return
    
    flatten(root.left)
    flatten(root.right)

    if root.left:
        temp = root.right
        root.right = root.left
        root.left = None

        curr = root
        while curr.right:
            curr = curr.right
        
        curr.right = temp
    

if __name__ == '__main__':
    testCases = [
        [1, 2, 3],
        [1, 2, 2, 3, 4, 4, 3],
        [1, 2, None, 3, 4, 5, 6, 7, 8],
        [1, 2, 4, 5, None, None, 6, 7, 8, 9]
    ]

    for i, testCase in enumerate(testCases):
        root = build_tree_from_list(testCase)

        print(f"\nTestcase {i}: i/p: {testCase}")

        flatten(root)

        # Extract flattened list
        vals = []
        curr = root
        while curr:
            vals.append(curr.val)
            curr = curr.right

        # Build RIGHT-SKEWED BinaryTree manually
        bt = BinaryTree()

        if vals:
            bt.root.element = vals[0]
            curr = bt.root

            for v in vals[1:]:
                new_node = bt.Node()
                new_node.element = v

                curr.rightchild = new_node
                new_node.parent = curr

                curr = new_node

        print("Output:")
        bt.displayTree()