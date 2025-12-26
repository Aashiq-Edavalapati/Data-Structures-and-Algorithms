from typing import List, Optional, Iterable


# ---------------------------
# Singly Linked List Node
# ---------------------------
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next

    def __repr__(self):
        return f"ListNode({self.val})"


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

def list_to_ll(values: Iterable[int]) -> Optional[ListNode]:
    """Convert Python list to Singly Linked List"""
    values = list(values)
    if not values:
        return None

    head = curr = ListNode(values[0])
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next

    return head


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
# Linked List → List (VERY useful for testing)
# ==================================================

def ll_to_list(head: Optional[ListNode]) -> List[int]:
    """Convert Singly Linked List to Python list"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


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

def print_ll(head: Optional[ListNode]) -> None:
    print(" -> ".join(map(str, ll_to_list(head))))


def print_dll(head: Optional[DLLNode]) -> None:
    print(" <-> ".join(map(str, dll_to_list(head))))
