# Link: https://www.geeksforgeeks.org/problems/find-pairs-with-given-sum-in-doubly-linked-list/1

"""
    @question:
        Given a sorted doubly linked list of positive distinct elements, the task is to find pairs in a doubly-linked list whose sum is equal to given value target.

        

        Example 1:
            Input:  
            1 <-> 2 <-> 4 <-> 5 <-> 6 <-> 8 <-> 9
            target = 7
            Output: (1, 6), (2,5)
            Explanation: We can see that there are two pairs 
            (1, 6) and (2,5) with sum 7.
        

        Example 2:
            Input: 
            1 <-> 5 <-> 6
            target = 6
            Output: (1,5)
            Explanation: We can see that there is one pairs  (1, 5) with sum 6.

        

        Your Task:
        You don't need to read input or print anything. Your task is to complete the function findPairsWithGivenSum() which takes head node of the doubly linked list and an integer target as input parameter and returns an array of pairs. If there is no such pair return empty array.

        Expected Time Complexity: O(N)
        Expected Auxiliary Space: O(1)
        Constraints:
            1 <= N <= 105
            1 <= target <= 105
"""
from typing import Optional, List
from List_to_Linked_List import *

def findPairsWithGivenSum(target : int, head : Optional[DLLNode]) -> List[List[int]]:
        left, right = head, head
        while right and right.next:
            right = right.next
        
        pairs = []
        while left.val < right.val:
            if left.val + right.val == target:
                pairs.append([left.val, right.val])
                left = left.next
                right = right.prev
            elif left.val + right.val > target:
                right = right.prev
            else:
                left = left.next
        
        return pairs

if __name__ == '__main__':
    testCases = [
        (5, [1, 2, 3, 4])
    ]

    for i, testCase in enumerate(testCases):
        target, head = testCase
        print(f"TestCase {i}:- i/p: head={head}, target={target}; o/p: {findPairsWithGivenSum(target, list_to_dll(head))}")