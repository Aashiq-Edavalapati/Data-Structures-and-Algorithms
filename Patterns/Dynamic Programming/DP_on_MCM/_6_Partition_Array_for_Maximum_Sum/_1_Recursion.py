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


"""
    @intuition:
        We can try partitioning the array at each idx and try extending the size of that partition to a max size of k.
            - So, from this observation, the reccurrence is straight forward
"""
def maxSumAfterPartitioning(arr: List[int], k: int) -> int:
    n = len(arr)
    def helper(idx: int) -> int:
        # Base Case: If idx = n => Whole array has been exhausted, no more paritions left to do
        if idx == n: return 0

        # Vars to keep track of maxSum we can get from the current idx and maxVal to keep track of the sum we get at each partition
        maxSum = 0
        maxVal = arr[idx]
        # Start searching for the best partition starting from idx with a max size of k
        for i in range(idx, min(idx + k, n)):
            maxVal = max(maxVal, arr[i])
            currSum = maxVal * (i - idx + 1) + helper(i + 1) # [x0, x1, ..,xidx + i | {,..., x(n-1)}]
            maxSum = max(maxSum, currSum)
        
        return maxSum

    return helper(0)

if __name__ == '__main__':
    testCases = [
        ([1,15,7,9,2,5,10], 3), # 84
        ([1,4,1,5,7,3,6,1,9,9,3], 4), # 83
        ([1], 1), # 1
    ]

    for i, testCase in enumerate(testCases):
        arr, k = testCase
        print(f"TestCase {i}:- i/p: arr={arr}, k={k}; o/p: {maxSumAfterPartitioning(arr, k)}")