# Link: https://leetcode.com/problems/subarrays-with-k-different-integers/

"""
    @question(LC 992):
        Given an integer array nums and an integer k, return the number of good subarrays of nums.

        A good array is an array where the number of different integers in that array is exactly k.

        For example, [1,2,3,1,2] has 3 different integers: 1, 2, and 3.
        A subarray is a contiguous part of an array.

    -------------------------------------------------------------
    -------------------------------------------------------------

        Example 1:
            Input: nums = [1,2,1,2,3], k = 2
            Output: 7
            Explanation: Subarrays formed with exactly 2 different integers: [1,2], [2,1], [1,2], [2,3], [1,2,1], [2,1,2], [1,2,1,2]

        -------------------------------------------------------------

        Example 2:
            Input: nums = [1,2,1,3,4], k = 3
            Output: 3
            Explanation: Subarrays formed with exactly 3 different integers: [1,2,1,3], [2,1,3], [1,3,4].
        
    -------------------------------------------------------------
    -------------------------------------------------------------
            
        Constraints:
            1 <= nums.length <= 2 * 104
            1 <= nums[i], k <= nums.length
"""
from typing import List

"""
    No. of subarrays with k distinct integers = (No. of subarrays with <= k distinct integers) - (No. of subarrays with <= (k - 1) distinct integers)
"""
def subarraysWithKDistInts(nums: List[int], k: int) -> int:
    return helper(nums, k) - helper(nums, k - 1)

"""
    No. of subbarrays with <= k distinct integers
"""
def helper(nums: List[int], k: int) -> int:
    n = len(nums)
    cnt = 0
    l, r = 0, 0
    freq = {}
    while r < n:
        if nums[r] in freq:
            freq[nums[r]] += 1
        else:
            freq[nums[r]] = 1
        while len(freq) > k:
            freq[nums[l]] -= 1
            if freq[nums[l]] == 0: del freq[nums[l]]
            l += 1

        cnt += r - l + 1
        r += 1

    return cnt

if __name__ == '__main__':
    testCases = [
        ([1,2,1,2,3], 2), # 7
        ([1,2,1,3,4], 3), # 3
    ]
    
    for i, testCase in enumerate(testCases):
        nums, k = testCase
        print(f"TestCase {i}:- i/p: nums={nums}, k={k}; o/p: {subarraysWithKDistInts(nums, k)}")