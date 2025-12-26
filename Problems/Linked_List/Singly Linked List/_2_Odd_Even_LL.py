# Link: https://leetcode.com/problems/odd-even-linked-list/

"""
    @question(LC 328):
        Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

        The first node is considered odd, and the second node is even, and so on.

        Note that the relative order inside both the even and odd groups should remain as it was in the input.

        You must solve the problem in O(1) extra space complexity and O(n) time complexity.

    ==========================================================================
    ==========================================================================

        Example 1:
            Input: head = [1,2,3,4,5]
            Output: [1,3,5,2,4]

        ==========================================================================

        Example 2:
            Input: head = [2,1,3,5,6,4,7]
            Output: [2,3,6,7,1,5,4]
        
    ==========================================================================
    ==========================================================================

        Constraints:
            The number of nodes in the linked list is in the range [0, 104].
            -106 <= Node.val <= 106
"""
from typing import Optional
from List_to_Linked_List import ListNode, list_to_ll, print_ll

def oddEvenList(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next or not head.next.next: return head
    odd, even = head, head.next;
    while (even and even.next):
        temp = odd.next
        odd.next = even.next
        even.next = odd.next.next
        odd.next.next = temp
        odd = odd.next
        even = even.next
    
    return head

def oddEvenList2(head: Optional[ListNode]) -> Optional[ListNode]:
    if not head or not head.next: return head
    odd, even = head, head.next
    evenHead = even
    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next

        odd = odd.next
        even = even.next
    
    odd.next = evenHead
    return head

if __name__ == '__main__':
    testCases = [
        [1,2,3,4,5], # [1,3,5,2,4]
        [2,1,3,5,6,4,7], # [2,3,6,7,1,5,4]
        [1, 2], # [1, 2]
    ]
    
    for i, head in enumerate(testCases):
        print(f"TestCase {i}:- i/p: head={head}")
        head = list_to_ll(head)
        print_ll(oddEvenList2(head))