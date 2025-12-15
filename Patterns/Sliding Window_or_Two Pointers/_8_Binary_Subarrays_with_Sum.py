# Link: https://leetcode.com/problems/binary-subarrays-with-sum/

"""
    @QUESTION(LC 930):
        Given a binary array nums and an integer goal, return the number of non-empty subarrays with a sum goal.

        A subarray is a contiguous part of the array.

    --------------------------------------------------------------
    --------------------------------------------------------------    

        Example 1:
            Input: nums = [1,0,1,0,1], goal = 2
            Output: 4
            Explanation: The 4 subarrays are bolded and underlined below:
                [1,0,1,0,1]
                [1,0,1,0,1]
                [1,0,1,0,1]
                [1,0,1,0,1]

        --------------------------------------------------------------

        Example 2:
            Input: nums = [0,0,0,0,0], goal = 0
            Output: 15
        
    --------------------------------------------------------------
    --------------------------------------------------------------

        Constraints:
            1 <= nums.length <= 3 * 104
            nums[i] is either 0 or 1.
            0 <= goal <= nums.length
"""
from typing import List

def numSubarraysWithSum(nums: List[int], goal: int) -> int:
    return cntSubarrayWithSumLTEK(nums, goal) - cntSubarrayWithSumLTEK(nums, goal - 1)

def cntSubarrayWithSumLTEK(nums: List[int], k: int) -> int:
    if k < 0: return 0
    l, r = 0, 0
    currSum = 0
    cnt = 0
    n = len(nums)
    while r < n:
        currSum += nums[r]
        while currSum > k:
            currSum -= nums[l]
            l += 1
        cnt += r - l + 1

        r += 1
    
    return cnt

if __name__ == '__main__':
    testCases = [
        ([1,0,1,0,1], 2), # 4
        ([0,0,0,0,0], 0), # 15
        ([1,0,0,0,1,0,1], 2), # 6
        ([0,0,0,0,0,0,1,0,0,0], 0), # 27
    ]
    
    for i, testCase in enumerate(testCases):
        nums, goal = testCase
        print(f"TestCase {i}:- i/p: nums={nums}, goal={goal}; o/p: {numSubarraysWithSum(nums, goal)}")