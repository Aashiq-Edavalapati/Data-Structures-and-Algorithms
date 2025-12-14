# Link: https://leetcode.com/problems/max-consecutive-ones-iii

"""
    @question(LC 1004):
        Given a binary array nums and an integer k, return the maximum number of consecutive 1's in the array if you can flip at most k 0's.

    -------------------------------------------------------------------
    -------------------------------------------------------------------

        Example 1:
            Input: nums = [1,1,1,0,0,0,1,1,1,1,0], k = 2
            Output: 6
            Explanation: [1,1,1,0,0,1,1,1,1,1,1]
            Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.

        -------------------------------------------------------------------

        Example 2:
            Input: nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3
            Output: 10
            Explanation: [0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
            Bolded numbers were flipped from 0 to 1. The longest subarray is underlined.
        
    -------------------------------------------------------------------
    -------------------------------------------------------------------

        Constraints:
            1 <= nums.length <= 105
            nums[i] is either 0 or 1.
            0 <= k <= nums.length
"""
from typing import List

def maxConsecOnes(nums: List[int], k: int) -> int:
    n = len(nums)
    l, r, flips, ones = 0, 0, 0, 0
    maxConsecOnes = 0
    while r < n:
        if nums[r] == 1:
            ones += 1
            maxConsecOnes = max(maxConsecOnes, ones + flips)
            r += 1
        elif nums[r] == 0 and flips < k:
            flips += 1
            r += 1
            maxConsecOnes = max(maxConsecOnes, ones + flips)
        else:
            while nums[l] == 1:
                l += 1
                ones -= 1
            l += 1
            flips -= 1
    
    return maxConsecOnes

if __name__ == '__main__':
    testCases = [
        ([1,1,1,0,0,0,1,1,1,1,0], 2), # 6
        ([0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], 3), # 10
    ]

    for i, testCase in enumerate(testCases):
        nums, k = testCase
        print(f"TestCase {i}:- i/p: nums={nums}; o/p: {maxConsecOnes(nums, k)}")