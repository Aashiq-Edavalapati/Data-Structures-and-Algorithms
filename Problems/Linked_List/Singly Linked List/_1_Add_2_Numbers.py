# Link: https://leetcode.com/problems/add-two-numbers/

"""
    @question(LC 2):
        You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

        You may assume the two numbers do not contain any leading zero, except the number 0 itself.

    ==========================================================
    ==========================================================

        Example 1:
            Input: l1 = [2,4,3], l2 = [5,6,4]
            Output: [7,0,8]
            Explanation: 342 + 465 = 807.

        ==========================================================

        Example 2:
            Input: l1 = [0], l2 = [0]
            Output: [0]

        ==========================================================

        Example 3:
            Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
            Output: [8,9,9,9,0,0,0,1]
        
    ==========================================================
    ==========================================================

        Constraints:
            The number of nodes in each linked list is in the range [1, 100].
            0 <= Node.val <= 9
            It is guaranteed that the list represents a number that does not have leading zeros.
"""
from typing import Optional
from List_to_Linked_List import ListNode, list_to_ll, print_ll

def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
    dummy = ListNode(0)
    curr = dummy
    carry = 0

    while l1 and l2:
        val = l1.val + l2.val + carry
        carry = val // 10
        curr.next = ListNode(val % 10)
        curr = curr.next
        l1 = l1.next
        l2 = l2.next

    while l1:
        val = l1.val + carry
        carry = val // 10
        curr.next = ListNode(val % 10)
        curr = curr.next
        l1 = l1.next
    
    while l2:
        val = l2.val + carry
        carry = val // 10
        curr.next = ListNode(val % 10)
        curr = curr.next
        l2 = l2.next
    
    if carry:
        curr.next = ListNode(1)
    
    return dummy.next

if __name__ == '__main__':
    testCases = [
        ([2,4,3], [5,6,4]), # [7, 0, 8]
        ([0], [0]), # 0
        ([9,9,9,9,9,9,9], [9,9,9,9]), # [8,9,9,9,0,0,0,1]
    ]
    
    for i, testCase in enumerate(testCases):
        l1, l2 = testCase
        print(f"TestCase {i}:- i/p: l1={l1}, l2={l2}")
        l1, l2 = list_to_ll(l1), list_to_ll(l2)
        print_ll(addTwoNumbers(l1, l2))