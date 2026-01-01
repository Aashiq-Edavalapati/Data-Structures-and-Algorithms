# Link: https://www.geeksforgeeks.org/problems/delete-all-occurrences-of-a-given-key-in-a-doubly-linked-list/1

"""
    You are given the head_ref of a doubly Linked List and a Key. Your task is to delete all occurrences of the given key if it is present and return the new DLL.

        Example1:
            Input: 
            2<->2<->10<->8<->4<->2<->5<->2
            2
            Output: 
            10<->8<->4<->5
            Explanation: 
            All Occurences of 2 have been deleted.

        Example2:
            Input: 
            9<->1<->3<->4<->5<->1<->8<->4
            9
            Output: 
            1<->3<->4<->5<->1<->8<->4
            Explanation: 
            All Occurences of 9 have been deleted.

        Your Task:

        Complete the function void deleteAllOccurOfX(struct Node** head_ref, int key), which takes the reference of the head pointer and an integer value key. Delete all occurrences of the key from the given DLL.

        Expected Time Complexity: O(N).

        Expected Auxiliary Space: O(1).

        Constraints:

        1<=Number of Nodes<=105

        0<=Node Value <=109
"""
from typing import Optional
from List_to_Linked_List import DLLNode, list_to_dll, print_dll

def deleteAllOccurOfX(head: Optional[DLLNode], x: int):
        while head and head.val == x:
            head = head.next
        
        temp = head
        while temp and temp.next:
            while temp and temp.next and temp.next.val == x:
                t = temp.next
                temp.next = temp.next.next
                if temp.next: temp.next.prev = temp
                t.next = None
                t.prev = None
            temp = temp.next
        
        return head

if __name__ == '__main__':
    testCases = [
        ([2, 5, 2, 4, 8, 10, 2, 2], 2),
        ([9, 1, 3, 4, 5, 1, 8, 4], 9),
    ]

    for i, testCase in enumerate(testCases):
        head, x = testCase
        print(f"TestCase {i}:- i/p: {head}; o/p: ", end='')
        head = list_to_dll(head)
        print_dll(deleteAllOccurOfX(head, x))