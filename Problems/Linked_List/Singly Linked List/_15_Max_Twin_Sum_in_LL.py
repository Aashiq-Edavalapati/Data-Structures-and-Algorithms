# Link: https://leetcode.com/problems/maximum-twin-sum-of-a-linked-list/

"""
    @question:
                                                                Maximum Twin Sum of a Linked List


        In a linked list of size n, where n is even, the ith node (0-indexed) of the linked list is known as the twin of the (n-1-i)th node, if 0 <= i <= (n / 2) - 1.

            For example, if n = 4, then node 0 is the twin of node 3, and node 1 is the twin of node 2. These are the only nodes with twins for n = 4.

        The twin sum is defined as the sum of a node and its twin.

        Given the head of a linked list with even length, return the maximum twin sum of the linked list.

    -------------------------------------------------------------------------------
    -------------------------------------------------------------------------------


        Example 1:
            Input: head = [5,4,2,1]
            Output: 6
            Explanation:
                Nodes 0 and 1 are the twins of nodes 3 and 2, respectively. All have twin sum = 6.
                There are no other nodes with twins in the linked list.
                Thus, the maximum twin sum of the linked list is 6. 

        -------------------------------------------------------------------------------
                
        Example 2:
            Input: head = [4,2,2,3]
            Output: 7
            Explanation:
                The nodes with twins present in this linked list are:
                - Node 0 is the twin of node 3 having a twin sum of 4 + 3 = 7.
                - Node 1 is the twin of node 2 having a twin sum of 2 + 2 = 4.
                Thus, the maximum twin sum of the linked list is max(7, 4) = 7. 

        Example 3:
            Input: head = [1,100000]
            Output: 100001
            Explanation:
                There is only one node with a twin in the linked list having twin sum of 1 + 100000 = 100001.

    -------------------------------------------------------------------------------
    -------------------------------------------------------------------------------

        Constraints:
            The number of nodes in the list is an even integer in the range [2, 105].
            1 <= Node.val <= 105
"""

from typing import Optional
from List_to_Linked_List import list_to_ll, print_ll, ListNode
from _4_Reverse_a_Linked_List import reverseListIterative
from _5_Find_Middle_Node import findMiddleNode

def pairSum(head: Optional[ListNode]) -> int:
    """
        @intuition:
            @Brute-Force:
                - Most naive way to solve this question would be converting the linked list into an array and then using two pointer on this array.
                - Time Complexity: O(n), Space Complexity: O(n)
            @Optimal:
                @Observations:
                    - In every twin, one node will be from the 1st half of the linked list and the other will be from the second half of the linked list.
                    - Twin of ith node will be ith node from last.
                - So, for finding twin for ith node, we have to find ith node from last, but we will go only till middle node, because all the nodes after the middle node were already paired up in the previous iterations
                - How do we traverse from the last node till middle node in a singly linked list? => Reverse ll from middle node.
                - Now since we've reversed the 2nd half of the array, we can place two pointers one at the beginning and one at the head of reversed linked list from mid and move both the pointers simultaneously.
                @Note:
                    - In the question it is given that the number of node will be even => middle element using the slow, fast pointers will always return the 2nd mid, so we can reverse from mid.
                    - If odd length is also possible => reverse from mid + 1 for odd and mid for even.
    """
    mid = findMiddleNode(head)
    revHead = reverseListIterative(mid)

    mid.next = None
    first, second = head, revHead
    maxSum = 0
    while first and second:
        maxSum = max(maxSum, first.val + second.val)
        first = first.next
        second = second.next
    
    return maxSum

if __name__ == '__main__':
    testCases = [
        [1,2,2,1], 
        [1,2,4,5], 
        [2,1,3,5,6,7],
        [1, 2],
        [5,4,2,1],
        [4,2,2,3],
        [1,100000]
    ]
    
    for i, head in enumerate(testCases):
        head = list_to_ll(head)
        print(f"TestCase {i}:- i/p: head={print_ll(head)}; o/p: {pairSum(head)}")