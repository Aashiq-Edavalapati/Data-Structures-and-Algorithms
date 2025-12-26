# Link: https://leetcode.com/problems/linked-list-cycle-ii/

"""
    @question:
        Given the head of a linked list, return the node where the cycle begins. If there is no cycle, return null.

        There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to (0-indexed). It is -1 if there is no cycle. Note that pos is not passed as a parameter.

        Do not modify the linked list.

    ==========================================================================
    ==========================================================================

        Example 1:
            Input: head = [3,2,0,-4], pos = 1
            Output: tail connects to node index 1
            Explanation: There is a cycle in the linked list, where tail connects to the second node.

        ==========================================================================

        Example 2:
            Input: head = [1,2], pos = 0
            Output: tail connects to node index 0
            Explanation: There is a cycle in the linked list, where tail connects to the first node.

        ==========================================================================

        Example 3:
            Input: head = [1], pos = -1
            Output: no cycle
            Explanation: There is no cycle in the linked list.

        ==========================================================================
        ==========================================================================        

        Constraints:
            The number of the nodes in the list is in the range [0, 104].
            -105 <= Node.val <= 105
            pos is -1 or a valid index in the linked-list.
"""
from typing import Optional, List
from List_to_Linked_List import ListNode, list_to_ll, print_ll

def findStartingPoint(head: Optional[ListNode]) -> Optional[ListNode]:
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast: break

    if not fast or not fast.next: return
    fast = head
    while fast != slow:
        fast = fast.next
        slow = slow.next
    
    return fast

if __name__ == '__main__':
    testCases = [
        ([3, 2, 0, -4], 1),  # 3
        ([1, 2], 0),        # 2
        ([1], -1),          # 0
        ([1, 2, 3, 4], -1), # 0
    ]

    def list_to_ll_pos(values: List[int], pos: int) -> ListNode:
        if pos == -1: return list_to_ll(values)
        head = list_to_ll(values)
        cyclicNode = None
        temp = head
        while temp and temp.next:
            if pos == 0:
                cyclicNode = temp
            temp = temp.next
            pos -= 1
        
        temp.next = cyclicNode
        return head

    for i, (values, pos) in enumerate(testCases):
        head = list_to_ll_pos(values, pos)
        print(f"TestCase {i}: head={values}, pos={pos} -> {findStartingPoint(head)}")