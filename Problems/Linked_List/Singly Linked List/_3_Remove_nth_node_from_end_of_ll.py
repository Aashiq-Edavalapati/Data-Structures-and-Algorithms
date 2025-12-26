# Link: https://leetcode.com/problems/remove-nth-node-from-end-of-list/

"""
    @question(LC 19):
        Given the head of a linked list, remove the nth node from the end of the list and return its head.

    =================================================================
    =================================================================

        Example 1:
            Input: head = [1,2,3,4,5], n = 2
            Output: [1,2,3,5]

        =================================================================

        Example 2:
            Input: head = [1], n = 1
            Output: []

        =================================================================

        Example 3:
            Input: head = [1,2], n = 1
            Output: [1]
        
    =================================================================
    =================================================================

        Constraints:
            The number of nodes in the list is sz.
            1 <= sz <= 30
            0 <= Node.val <= 100
            1 <= n <= sz
"""
from typing import Optional
from List_to_Linked_List import list_to_ll, print_ll, ListNode

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    fast = head
    while n > 0:
        fast = fast.next
        n -= 1
    if not fast: return head.next
    slow = head
    while fast.next:
        fast = fast.next
        slow = slow.next

    slow.next = slow.next.next
    return head

if __name__ == '__main__':
    testCases = [
        ([1,2,3,4,5], 2), # [1,2,3,5]
        ([1], 1), # []
        ([1, 2], 1), # [1]
    ]
    
    for i, testCase in enumerate(testCases):
        head, n = testCase
        print(f"TestCase {i}:- i/p: head={head}, n={n}")
        head = list_to_ll(head)
        print_ll(removeNthFromEnd(head, n))