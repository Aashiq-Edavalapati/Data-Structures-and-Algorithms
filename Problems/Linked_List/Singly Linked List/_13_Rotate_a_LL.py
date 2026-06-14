# Link: https://leetcode.com/problems/rotate-list/

"""
    @question:
        Given the head of a linked list, rotate the list to the right by k places.

    ============================================================
    ============================================================  

        Example 1:
            Input: head = [1,2,3,4,5], k = 2
            Output: [4,5,1,2,3]

        ============================================================

        Example 2:
            Input: head = [0,1,2], k = 4
            Output: [2,0,1]
        
    ============================================================
    ============================================================

        Constraints:
            The number of nodes in the list is in the range [0, 500].
            -100 <= Node.val <= 100
            0 <= k <= 2 * 109
"""
from typing import Optional
from List_to_Linked_List import ListNode, list_to_ll, print_ll

def rotateRight(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    if not head or not head.next or k == 0:
        return head
    
    tail = head
    size = 1
    while(tail.next):
        size += 1
        tail = tail.next

    k = k%size
    if k == 0:
        return head
    
    currentNode = head
    for _ in range(1,size - k):
        currentNode = currentNode.next
    
    newHead = currentNode.next
    currentNode.next = None
    tail.next = head
    
    return newHead

if __name__ == '__main__':
    testCases = [
        ([1,2,3,4,5], 2), # [4,5,1,2,3]
        ([1,2,3,4,5], 3), # [3,4,5,1,2]
        ([0,1,2], 4), # [2,0,1]
    ]

    for i, testCase in enumerate(testCases):
        head, k = testCase
        print(f"TestCase {i}:- i/p: head={head}, k={k}; o/p: ", end='')
        head = list_to_ll(head)
        print_ll(rotateRight(head, k))