# Link: https://leetcode.com/problems/intersection-of-two-linked-lists/

"""
    @question:
        Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

        For example, the following two linked lists begin to intersect at node c1:

        The test cases are generated such that there are no cycles anywhere in the entire linked structure.

        Note that the linked lists must retain their original structure after the function returns.

        Custom Judge:

            The inputs to the judge are given as follows (your program is not given these inputs):

            intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
            listA - The first linked list.
            listB - The second linked list.
            skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
            skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
            The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.


        Example 1:
            Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
            Output: Intersected at '8'
            Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
                From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
                - Note that the intersected node's value is not 1 because the nodes with value 1 in A and B (2nd node in A and 3rd node in B) are different node references. In other words, they point to two different locations in memory, while the nodes with value 8 in A and B (3rd node in A and 4th node in B) point to the same location in memory.


        Example 2:
            Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
            Output: Intersected at '2'
            Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
                From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.

        Example 3:
            Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
            Output: No intersection
            Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
            Explanation: The two lists do not intersect, so return null.
        

        Constraints:
            The number of nodes of listA is in the m.
            The number of nodes of listB is in the n.
            1 <= m, n <= 3 * 104
            1 <= Node.val <= 105
            0 <= skipA <= m
            0 <= skipB <= n
            intersectVal is 0 if listA and listB do not intersect.
            intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.
"""
from List_to_Linked_List import ListNode, print_ll, list_to_ll
from typing import Optional

def getIntersectionNode(headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
    n, m = 0, 0

    # Find lengths of both lists
    t1, t2 = headA, headB
    while t1:
        m += 1
        t1 = t1.next
    while t2:
        n += 1
        t2 = t2.next
    
    # Move both pointer to same level: i.e., to a position where both have same number of nodes after that!
    t1, t2 = headA, headB
    while n > m:
        n -= 1
        t2 = t2.next
    while m > n:
        m -= 1
        t1 = t1.next
    
    # Keep comparing two pointers and move forward
    while t1 and t2:
        if t1 == t2: return t1
        t1 = t1.next
        t2 = t2.next
    
    return None

def getIntersectionNodeOptimal(headA: Optional[ListNode], headB: Optional[ListNode]) -> Optional[ListNode]:
    if not headA or not headB: return None

    temp1, temp2 = headA, headB
    while temp1 != temp2:
        temp1 = temp1.next
        temp2 = temp2.next

        if temp1 == temp2: return temp1
        if not temp1: temp1 = headB
        if not temp2: temp2 = headA
    
    return temp1

if __name__ == '__main__':
    testCases = [
        ([4,1,8,4,5], [5,6,1,8,4,5], 2, 3), # [8, 4, 5]
        ([1,9,1,2,4], [3,2,4], 3, 1), # [2, 4]
        ([2,6,4], [1, 5], 3, 2), # None
    ]
    
    

    def build_lists(listA, listB, skipA, skipB):
        """
            helper function to build the Y - Linked list
        """
        dummyA = ListNode(0)
        currA = dummyA
        nodesA = []
        for val in listA:
            currA.next = ListNode(val)
            currA = currA.next
            nodesA.append(currA)

        dummyB = ListNode(0)
        currB = dummyB
        nodesB = []
        for val in listB:
            currB.next = ListNode(val)
            currB = currB.next
            nodesB.append(currB)

        if skipA < len(nodesA) and skipB < len(nodesB):
            nodesB[skipB].next = nodesA[skipA]

        return dummyA.next, dummyB.next

    for i, testCase in enumerate(testCases):
        l1, l2, skipA, skipB = testCase
        print(f"TestCase {i}:- i/p: l1={l1}, l2={l2}")
        l1, l2 = build_lists(l1, l2, skipA, skipB)
        print("\to/p: ", end=' ')
        # print_ll(getIntersectionNode(l1, l2))
        print_ll(getIntersectionNodeOptimal(l1, l2))