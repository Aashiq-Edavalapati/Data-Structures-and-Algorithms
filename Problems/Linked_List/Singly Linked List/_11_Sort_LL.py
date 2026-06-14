# Link: https://leetcode.com/problems/sort-list/

"""
    @question:
        Given the head of a linked list, return the list after sorting it in ascending order.
"""
from typing import Optional
from List_to_Linked_List import ListNode, list_to_ll, print_ll

def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next: return head

    slow, fast = head, head
    fast = fast.next.next
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    
    fast = slow.next
    slow.next = None
    left = sortList(head)
    right = sortList(fast)

    return merge(left, right)

def merge(headA: Optional[ListNode], headB: Optional[ListNode]):
    if not headA:
        return headB
    if not headB:
        return headA
    
    head = ListNode(0)
    temp = head
    temp1, temp2 = headA, headB
    while temp1 and temp2:
        if temp1.val > temp2.val:
            temp.next = ListNode(temp2.val)
            temp2 = temp2.next
        else:
            temp.next = ListNode(temp1.val)
            temp1 = temp1.next
        temp = temp.next

    if temp1: temp.next = temp1
    elif temp2: temp.next = temp2

    return head.next

if __name__ == '__main__':
    testCases = [
        [1,2,5,4,5], # [1,2,4,4,5]
        [2,1,3,5,6,4,7], # [1,2,3,4,5,6,7]
        [1, 2], # [1, 2]
    ]
    
    for i, head in enumerate(testCases):
        print(f"TestCase {i}:- i/p: head={head}")
        head = list_to_ll(head)
        print_ll(sortList(head))