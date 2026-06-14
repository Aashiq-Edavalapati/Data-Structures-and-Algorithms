# Link: https://leetcode.com/problems/reverse-nodes-in-k-group/

"""
    @question:
        Given the head of a linked list, reverse the nodes of the list k at a time, and return the modified list.

        k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

        You may not alter the values in the list's nodes, only nodes themselves may be changed.

    ========================================================================
    ========================================================================

        Example 1:
            Input: head = [1,2,3,4,5], k = 2
            Output: [2,1,4,3,5]

        ========================================================================

        Example 2:
            Input: head = [1,2,3,4,5], k = 3
            Output: [3,2,1,4,5]
        
    ========================================================================
    ========================================================================

        Constraints:
            The number of nodes in the list is n.
            1 <= k <= n <= 5000
            0 <= Node.val <= 1000
"""
from typing import Optional
from List_to_Linked_List import ListNode, list_to_ll, print_ll  

def reverseKGroupRecursive(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or not head.next: return head

    left, right = head, head
    cnt = 1
    while right:
        if cnt == k:
            temp = right.next
            right.next = None
            right = left
            left = reverse(left)
            right.next = reverseKGroupRecursive(temp, k)
            break
        right = right.next
        cnt += 1

    return left

def reverseKGroupIterative(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or not head.next: return head

    left, right = head, head
    cnt = 1
    nextNode, prevNode = None, None
    while right:
        if cnt == k:
            nextNode = right.next
            right.next = None
            left = reverse(left)
            prevNode = head
            head = left
            left = nextNode
            right = nextNode
            break

        right = right.next
        cnt += 1
    
    cnt = 1
    while right:
        if cnt == k:
            nextNode = right.next
            right.next = None
            prevNode.next = reverse(left)
            prevNode = left
            left = nextNode
            right = nextNode
            cnt = 1

        if right:
            right = right.next
            cnt += 1

    if prevNode: prevNode.next = nextNode
    return head

def reverse(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next: return head

    rev = head
    head = head.next
    rev.next = None
    while head:
        temp = head.next
        head.next = rev
        rev = head
        head = temp
    
    return rev 

if __name__ == '__main__':
    testCases = [
        ([1,2,3,4,5], 2), # [2,1,4,3,5]
        ([1,2,3,4,5], 3), # [3,2,1,4,5]
    ]

    for i, testCase in enumerate(testCases):
        head, k = testCase
        print(f"TestCase {i}:- i/p: head={head}, k={k}; o/p: ", end='')
        head = list_to_ll(head)
        # print_ll(reverseKGroupRecursive(head, k))
        print_ll(reverseKGroupIterative(head, k))