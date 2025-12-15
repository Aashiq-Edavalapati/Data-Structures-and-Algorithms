# Link: https://leetcode.com/problems/count-number-of-nice-subarrays/

"""
    @QUESTION(LC 1248):
        Given an array of integers nums and an integer k. A continuous subarray is called nice if there are k odd numbers on it.

        Return the number of nice sub-arrays.

    -----------------------------------------------------------------------
    -----------------------------------------------------------------------

        Example 1:
            Input: nums = [1,1,2,1,1], k = 3
            Output: 2
            Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].

        -----------------------------------------------------------------------

        Example 2:
            Input: nums = [2,4,6], k = 1
            Output: 0
            Explanation: There are no odd numbers in the array.

        -----------------------------------------------------------------------

        Example 3:
            Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
            Output: 16
        
    -----------------------------------------------------------------------
    -----------------------------------------------------------------------

        Constraints:
            1 <= nums.length <= 50000
            1 <= nums[i] <= 10^5
            1 <= k <= nums.length
"""
from  typing import List

def noOfSubarrays(nums: List[int], k: int) -> int:
    return helper(nums, k) - helper(nums, k - 1)

def helper(nums: List[int], k: int) -> int:
    n = len(nums)
    odd = 0
    l, r = 0, 0
    cnt = 0
    while r < n:
        if nums[r] % 2 != 0:
            odd += 1
        while odd > k:
            if nums[l] % 2 != 0: odd -= 1
            l += 1
        cnt += r - l + 1
        
        r += 1
    
    return cnt

if __name__ == '__main__':
    testCases = [
        ([1,1,2,1,1], 3), # 2
        ([2,4,6], 1), # 0
        ([2,2,2,1,2,2,1,2,2,2], 2), # 16
    ]
    
    for i, testCase in enumerate(testCases):
        nums, k = testCase
        print(f"TestCase {i}:- i/p: nums={nums}, k={k}; o/p: {noOfSubarrays(nums, k)}")