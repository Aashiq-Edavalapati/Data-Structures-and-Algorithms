# Link: https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/

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


def distanceK(root: 'TreeNode', target: 'TreeNode', k: int) -> List[int]:
    """
        @intuition:
            - Point to parents for each node and now radially move in all the 3 directions from the target until we reach the requred distance(k).
    """
    parent = {}
    q =  [root]

    while q:
        sz = len(q)
        for _ in range(sz):
            node = q.pop(0)
            if node.left:
                parent[node.left.val] = node
                q.append(node.left)
            if node.right:
                parent[node.right.val] = node
                q.append(node.right)
    
    visited = set()
    visited.add(target.val)
    q = [target]
    dist = 0
    while q:
        if dist == k: return [el.val for el in q]
        sz = len(q)
        for _ in range(sz):
            node = q.pop(0)
            if (node.val in parent) and (parent[node.val].val not in visited):
                q.append(parent[node.val])
                visited.add(parent[node.val].val)
            if node.left and (node.left.val not in visited):
                q.append(node.left)
                visited.add(node.left.val)
            if node.right and (node.right.val not in visited):
                q.append(node.right)
                visited.add(node.right.val)
        
        dist += 1

    return [el.val for el in q]
    

if __name__ == '__main__':
    testCases = [
        [[3,5,1,6,2,0,8,None,None,7,4], 5, 2],
        [[1], 1, 3]
    ]

    def find_node(root: 'TreeNode', target: int) -> Optional['TreeNode']:
        if not root:
            return None
        if root.val == target:
            return root

        left = find_node(root.left, target)
        if left:
            return left
        return find_node(root.right, target)

    for i, (values, target_val, k) in enumerate(testCases):
        root = build_tree_from_list(values)
        target = find_node(root, target_val)
        result = distanceK(root, target, k)

        print(f"Testcase {i}:")
        print(f"Input: values={values}, target={target_val}, k={k}")
        print(f"Output: {result}")