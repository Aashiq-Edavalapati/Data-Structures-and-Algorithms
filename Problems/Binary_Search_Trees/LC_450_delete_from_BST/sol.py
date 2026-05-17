# Link: https://leetcode.com/problems/delete-node-in-a-bst/

"""
    @question:
        Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.
        Basically, the deletion can be divided into two stages:
            Search for a node to remove.
            If the node is found, delete the node.

    --------------------------------------------------------------------------------------
    --------------------------------------------------------------------------------------

        Example 1:
            Input: root = [5,3,6,2,4,null,7], key = 3
            Output: [5,4,6,2,null,null,7]
            Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
            One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
            Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

        --------------------------------------------------------------------------------------
            
        Example 2:
            Input: root = [5,3,6,2,4,null,7], key = 0
            Output: [5,3,6,2,4,null,7]
            Explanation: The tree does not contain a node with value = 0.

        --------------------------------------------------------------------------------------
            
        Example 3:
            Input: root = [], key = 0
            Output: []
        
    --------------------------------------------------------------------------------------
    --------------------------------------------------------------------------------------

        Constraints:
            The number of nodes in the tree is in the range [0, 104].
            -105 <= Node.val <= 105
            Each node has a unique value.
            root is a valid binary search tree.
            -105 <= key <= 105
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

def deleteNode(root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
    if not root: return
    if root.val == key:
        node = root.right
        if not node: return root.left
        n = root.left
        if not n: return node
        t = n
        while n and n.right:
            n = n.right
        n.right = node

        return t
    
    if root.val < key:
        root.right = deleteNode(root.right, key)
    else:
        root.left = deleteNode(root.left, key)
    
    return root

if __name__ == '__main__':
    testCases = [
        [[5,3,6,2,4,None,7], 3],
        [[5,3,6,2,4,None,7], 0],
        [[], 0]
    ]

    for i, (tree, val) in enumerate(testCases):
        root = build_tree_from_list(tree)

        print(f"Testcase {i}:")
        print(f"Input: val={val}, root: \n")
        display_tree(root)
        newRoot = deleteNode(root, val)
        print(f"Output: \n")
        display_tree(newRoot)