# Link: https://leetcode.com/problems/next-greater-element-ii/
"""
    @question:
        Given a circular integer array nums (i.e., the next element of nums[nums.length - 1] is nums[0]), return the next greater number for every element in nums.

        The next greater number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, return -1 for this number.

    ---------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------

        Example 1:
            Input: nums = [1,2,1]
            Output: [2,-1,2]
            Explanation: The first 1's next greater number is 2; 
                The number 2 can't find next greater number. 
                The second 1's next greater number needs to search circularly, which is also 2.
    
        ---------------------------------------------------------------------------------
                
        Example 2:
            Input: nums = [1,2,3,4,3]
            Output: [2,3,4,-1,4]
    
    ---------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------

        Constraints:
            1 <= nums.length <= 104
            -109 <= nums[i] <= 109
"""
from typing import List

def nge2(nums: List[int]) -> List[int]:
    n = len(nums)
    nge = [-1] * n
    stk = []
    for i in range(n - 1, -1, -1):
        while stk and stk[-1] <= nums[i]:
            stk.pop()
        stk.append(nums[i])
    
    for i in range(n - 1, -1, -1):
        while stk and stk[-1] <= nums[i]:
            stk.pop()
        if stk:
            nge[i] = stk[-1]
        stk.append(nums[i])

    return nge

if __name__ == '__main__':
    testCases = [
        [1,2,1], # [2,-1,2]
        [1,2,3,4,3], # [2,3,4,-1,4]
        [1,2,3,4,3,5], # [2,3,4,5,5,-1]
        [5,4,3,2,1], # [-1,5,5,5,5]
    ]

    for i, nums in enumerate(testCases):
        print(f"TestCase {i}:- i/p: nums={nums}; o/p: {nge2(nums)}")