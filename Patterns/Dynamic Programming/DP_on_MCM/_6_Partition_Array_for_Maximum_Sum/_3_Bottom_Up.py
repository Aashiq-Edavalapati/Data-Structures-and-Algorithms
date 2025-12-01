# Link: https://leetcode.com/problems/partition-array-for-maximum-sum/

"""
    @question:
        Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray.

        Return the largest sum of the given array after partitioning. Test cases are generated so that the answer fits in a 32-bit integer.

    -----------------------------------------------------------------------------------------
    -----------------------------------------------------------------------------------------

        Example 1:
            Input: arr = [1,15,7,9,2,5,10], k = 3
            Output: 84
            Explanation: arr becomes [15,15,15,9,10,10,10]

        -----------------------------------------------------------------------------------------

        Example 2:
            Input: arr = [1,4,1,5,7,3,6,1,9,9,3], k = 4
            Output: 83
        
        -----------------------------------------------------------------------------------------
            
        Example 3:
            Input: arr = [1], k = 1
            Output: 1

    -----------------------------------------------------------------------------------------
    -----------------------------------------------------------------------------------------

        Constraints:
            1 <= arr.length <= 500
            0 <= arr[i] <= 109
            1 <= k <= arr.length
"""
from typing import List

def maxSumAfterPartitioning(arr: List[int], k: int) -> int:
    n = len(arr)
    dp = [0 for _ in range(n + 1)]
    for idx in range(n - 1, -1, -1):
        maxSum = 0
        maxVal = arr[idx]
        for i in range(idx, min(idx + k, n)):
            maxVal = max(maxVal, arr[i])
            currSum = maxVal * (i - idx + 1) + dp[i + 1]
            maxSum = max(maxSum, currSum)
        
        dp[idx] = maxSum

    return dp[0]

if __name__ == '__main__':
    testCases = [
        ([1,15,7,9,2,5,10], 3), # 84
        ([1,4,1,5,7,3,6,1,9,9,3], 4), # 83
        ([1], 1), # 1
    ]

    for i, testCase in enumerate(testCases):
        arr, k = testCase
        print(f"TestCase {i}:- i/p: arr={arr}, k={k}; o/p: {maxSumAfterPartitioning(arr, k)}")