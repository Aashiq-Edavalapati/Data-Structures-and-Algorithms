from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from typing import List


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

def floorCeilInBST(root: 'TreeNode', val: int) -> List[int]:
    if not root: return -1
    floor, ceil = -1, -1
    stack = [root]
    curr = root
    while curr or stack:
        if not curr:
            node = stack.pop()
            if node.val < val:
                floor = node.val
            elif node.val > val:
                ceil = node.val
                break
            else:
                floor = node.val
                ceil = node.val
                break
            curr = node.right
            if curr: stack.append(curr)
            continue
        
        curr = curr.left
        if curr: stack.append(curr)

    return [floor, ceil]

if __name__ == '__main__':
    testCases = [
        [[8, 4, 12, 2, 6, 10, 14] , 11],
        [[8, 4, 12, 2, 6, 10, 14] , 15],
        [[8, 4, 12, 2, 6, 10, 14] , 1],
        [[8, 4, 12, 2, 6, 10, 14] , 6]
    ]

    for i, (tree, val) in enumerate(testCases):
        root = build_tree_from_list(tree)

        floor, ceil = floorCeilInBST(root, val)
        print(f"Testcase {i}:")
        print(f"Input: val={val}, root: ")
        display_tree(root)
        print(f"Output: floor={floor}, ceil={ceil}")