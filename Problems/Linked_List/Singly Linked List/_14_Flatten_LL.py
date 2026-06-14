# Link: https://www.geeksforgeeks.org/problems/flattening-a-linked-list/1

from typing import Optional

class ListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.bottom = None

def flatten(root):
    if not root or not root.next: return root
    def helper(a, b):
        if not b: return a
        
        a.next = helper(b, b.next)
        return merge(a, a.next)

    return helper(root, root.next)
    
def merge(a, b):
    t1, t2 = a, b
    head = ListNode(0)
    t = head
    while t1 and t2:
        if t1.data <= t2.data:
            t.bottom = t1
            t1 = t1.bottom
        else:
            t.bottom = t2
            t2 = t2.bottom
        t = t.bottom
    
    if t1: t.bottom = t1
    else: t.bottom = t2
    
    return head.bottom

if __name__ == '__main__':
    testCases = [
        [[5, 7, 8, 30], [10, 20], [19, 22, 50], [28, 35, 40, 45]],
        [[1, 3, 5], [2, 4, 6]],
        [[1], [2], [3]]
    ]

    def build_linked_list(arr):
        """
        Builds a bottom-linked list from a sorted array
        """
        head = ListNode(arr[0])
        curr = head
        for val in arr[1:]:
            curr.bottom = ListNode(val)
            curr = curr.bottom
        return head


    def build_multilevel_list(lists):
        """
        lists: List of lists
        Each inner list becomes a bottom-linked list
        All heads are connected using next pointers
        """
        head = build_linked_list(lists[0])
        curr = head

        for lst in lists[1:]:
            curr.next = build_linked_list(lst)
            curr = curr.next

        return head


    def print_flattened_list(head):
        """
        Prints flattened linked list using bottom pointers
        """
        curr = head
        while curr:
            print(curr.data, end=" ")
            curr = curr.bottom
        print()

    for i, lists in enumerate(testCases):
        print(f"TestCase {i}:- i/p: list={lists}; o/p: ", end='')
        root = build_multilevel_list(lists)
        flat_head = flatten(root)
        print_flattened_list(flat_head)