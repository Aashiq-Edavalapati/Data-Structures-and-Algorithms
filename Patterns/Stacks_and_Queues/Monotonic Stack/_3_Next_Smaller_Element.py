"""
    @question:
        Given an array of integers arr, your task is to find the Next Smaller Element (NSE) for every element in the array.

        The Next Smaller Element for an element x is defined as the first element to the right of x that is smaller than x.

        If there is no smaller element to the right, then the NSE is -1.

    --------------------------------------------------------------------------------
    --------------------------------------------------------------------------------
        
        Examples:
            Input: arr = [4, 8, 5, 2, 25]
            Output: [2, 5, 2, -1, -1]
            Explanation:
                - For 4, the next smaller element is 2.
                - For 8, the next smaller element is 5.
                - For 5, the next smaller element is 2.
                - For 2, there is no smaller element to its right → -1.
                - For 25, no smaller element exists → -1.

            --------------------------------------------------------------------------------

            Input: arr = [10, 9, 8, 7]
            Output: [9, 8, 7, -1]
            Explanation: Each element’s next right neighbor is smaller.
    --------------------------------------------------------------------------------
    --------------------------------------------------------------------------------

        Constraints:
            1 <= arr.length <= 105
            -109 <= arr[i] <= 109
"""
from typing import List

def nextSmallerEL(nums: List[int]) -> List[int]:
    n = len(nums)
    stk = []
    nse = [-1] * n
    for i in range(n - 1, -1, -1):
        while stk and stk[-1] >= nums[i]:
            stk.pop()
        if stk:
            nse[i] = stk[-1]
        stk.append(nums[i])

    return nse

if __name__ == '__main__':
    testCases = [
         [4, 8, 5, 2, 25], # [2, 5, 2, -1, -1]
         [10, 9, 8, 7], # [9, 8, 7, -1]
    ]

    for i, nums in enumerate(testCases):
        print(f"TestCase {i}:- i/p: nums={nums}; o/p: {nextSmallerEL(nums)}")