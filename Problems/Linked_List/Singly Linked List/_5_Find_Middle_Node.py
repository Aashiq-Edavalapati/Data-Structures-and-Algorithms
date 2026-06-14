from typing import Optional
from List_to_Linked_List import list_to_ll, print_ll, ListNode

def findMiddleNode(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next: return head

    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    return slow

