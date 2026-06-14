"""
        Given the head of a linked list, determine whether the list contains a loop. If a loop is present, return the number of nodes in the loop, otherwise return 0.

        Note: Internally, pos(1 based index) is used to denote the position of the node that tail's next pointer is connected to. If pos = 0, it means the last node points to null, indicating there is no loop. Note that pos is not passed as a parameter.

        Examples:
            Input: pos = 2,
            Output: 4
            Explanation: There exists a loop in the linked list and the length of the loop is 4.


            Input: pos = 3,
            Output: 3
            Explanation: The loop is from 19 to 10. So length of loop is 19 → 33 → 10 = 3.


            Input: pos = 0    
            Output: 0
            Explanation: There is no loop.

        Constraints:
            1 ≤ number of nodes ≤ 105
            1 ≤ node->data ≤ 104
            0 ≤ pos < number of nodes
"""
from typing import Optional, List
from List_to_Linked_List import list_to_ll, ListNode

def lengthOfLoop(head: Optional[ListNode]) -> int:
        if not head or not head.next: return 0
        
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                break
        
        if not fast or not fast.next: return 0
        size = 1
        fast = fast.next
        while fast != slow:
            size += 1
            fast = fast.next
        
        return size

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
        print(f"TestCase {i}: head={values}, pos={pos} -> {lengthOfLoop(head)}")