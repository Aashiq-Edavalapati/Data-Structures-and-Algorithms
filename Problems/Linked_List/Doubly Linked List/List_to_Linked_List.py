from typing import List, Optional, Iterable

# ---------------------------
# Doubly Linked List Node
# ---------------------------
class DLLNode:
    def __init__(
        self,
        val: int = 0,
        next: Optional["DLLNode"] = None,
        prev: Optional["DLLNode"] = None,
    ):
        self.val = val
        self.next = next
        self.prev = prev

    def __repr__(self):
        return f"DLLNode({self.val})"


# ==================================================
# List → Linked List
# ==================================================
def list_to_dll(values: Iterable[int]) -> Optional[DLLNode]:
    """Convert Python list to Doubly Linked List"""
    values = list(values)
    if not values:
        return None

    head = curr = DLLNode(values[0])
    for val in values[1:]:
        node = DLLNode(val, prev=curr)
        curr.next = node
        curr = node

    return head


# ==================================================
# Linked List → List
# ==================================================
def dll_to_list(head: Optional[DLLNode]) -> List[int]:
    """Convert Doubly Linked List to Python list"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# ==================================================
# Debug Print Helpers
# ==================================================
def print_dll(head: Optional[DLLNode]) -> None:
    print(" <-> ".join(map(str, dll_to_list(head))))