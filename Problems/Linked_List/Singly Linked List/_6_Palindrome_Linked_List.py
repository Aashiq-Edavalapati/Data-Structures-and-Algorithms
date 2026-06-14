# Link: https://leetcode.com/problems/palindrome-linked-list/

"""
    @question:
        Given the head of a singly linked list, return true if it is a palindrome or false otherwise.

    ====================================================================
    ====================================================================

        Example 1:
            Input: head = [1,2,2,1]
            Output: true

        ====================================================================

        Example 2:
            Input: head = [1,2]
            Output: false
        
    ====================================================================
    ====================================================================

        Constraints:
            The number of nodes in the list is in the range [1, 105].
            0 <= Node.val <= 9
"""
from typing import Optional
from List_to_Linked_List import list_to_ll, print_ll, ListNode
from _4_Reverse_a_Linked_List import reverseListIterative

def isPalindrome(head: Optional[ListNode]) -> bool:
    if not head or not head.next: return True

    slow, fast = head, head
    while fast and fast.next and fast.next.next:
        slow = slow.next
        fast = fast.next.next

    second = reverseListIterative(slow.next)
    first = head
    while second:
        if first.val != second.val: return False
        first = first.next
        second = second.next
    
    reverseListIterative(slow.next)
    return True

if __name__ == '__main__':
    testCases = [
        [1,2,2,1], # True
        [1,2,3,4,5], # False
        [2,1,3,5,6,4,7], # False
        [1, 2], # False
        [1, 2, 1], # True
    ]
    
    for i, head in enumerate(testCases):
        head = list_to_ll(head)
        print(f"TestCase {i}:- i/p: head={print_ll(head)}; o/p: {isPalindrome(head)}")