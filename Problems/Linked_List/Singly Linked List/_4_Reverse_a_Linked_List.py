# Link: https://leetcode.com/problems/reverse-linked-list/

"""
    @question:
        Given the head of a singly linked list, reverse the list, and return the reversed list.

    ================================================================
    ================================================================

        Example 1:
            Input: head = [1,2,3,4,5]
            Output: [5,4,3,2,1]
    
        ================================================================

        Example 2:
            Input: head = [1,2]
            Output: [2,1]

        ================================================================

        Example 3:
            Input: head = []
            Output: []
        
    ================================================================
    ================================================================

        Constraints:
            The number of nodes in the list is the range [0, 5000].
            -5000 <= Node.val <= 5000
"""
from typing import Optional
from List_to_Linked_List import list_to_ll, print_ll, ListNode

def reverseListIterative(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next: return head

    reverse = head
    head = head.next
    reverse.next = None
    while head:
        temp = head.next
        head.next = reverse
        reverse = head
        head =  temp
    
    return reverse

def reverseListRecursive(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next: return head

    revHead = reverseListRecursive(head.next)
    front = head.next
    front.next = head
    head.next = None

    return revHead

if __name__ == '__main__':
    testCases = [
        [1,2,3,4,5], # [5,4,3,2,1]
        [2,1,3,5,6,4,7], # [7,4,6,5,3,1,2]
        [1, 2], # [2,1]
    ]
    
    for i, head in enumerate(testCases):
        print(f"TestCase {i}:- i/p: head={head}")
        head = list_to_ll(head)
        print_ll(reverseListRecursive(head))