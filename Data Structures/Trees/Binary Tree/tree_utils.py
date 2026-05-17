from importlib.util import module_from_spec, spec_from_file_location
from pathlib import Path
from typing import Optional


_BINARY_TREE_PATH = (
	Path(__file__).resolve().parent / "BinaryTree.py"
)

_spec = spec_from_file_location("binary_tree", _BINARY_TREE_PATH)
if _spec is None or _spec.loader is None:
	raise ImportError(f"Cannot load BinaryTree from {_BINARY_TREE_PATH}")

_binary_tree_module = module_from_spec(_spec)
_spec.loader.exec_module(_binary_tree_module)

BinaryTree = _binary_tree_module.BinaryTree


def display_tree(node: Optional[object]) -> None:
	"""
	Pretty-print a tree rooted at the given node.

	Supports both LeetCode-style nodes with `val`, `left`, `right` and
	BinaryTree nodes with `element`, `leftchild`, `rightchild`.
	"""
	def convert(current, parent=None):
		if not current:
			return None

		converted = BinaryTree.Node()
		converted.element = getattr(current, "val", getattr(current, "element", None))
		converted.parent = parent
		converted.leftchild = convert(
			getattr(current, "left", getattr(current, "leftchild", None)),
			converted,
		)
		converted.rightchild = convert(
			getattr(current, "right", getattr(current, "rightchild", None)),
			converted,
		)
		return converted

	tree = BinaryTree()
	tree.root = convert(node)
	tree.displayTree()