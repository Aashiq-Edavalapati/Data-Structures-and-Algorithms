"""
    @question:
        Given an array of n integers arr, return the Longest Increasing Subsequence (LIS) that is Index-wise Lexicographically Smallest.

        The Longest Increasing Subsequence (LIS) is the longest subsequence where all elements are in strictly increasing order.

        A subsequence A1 is Index-wise Lexicographically Smaller than another subsequence A2 if, at the first position where A1 and A2 differ, the element in A1 appears earlier in the array arr than corresponding element in S2.

        Your task is to return the LIS that is Index-wise Lexicographically Smallest from the given array.

    ----------------------------------------------------------------------------------------------------------

        Example 1:
            Input: arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
            Output: [10, 22, 33, 50, 60, 80]
            Explanation: The LIS is [10, 22, 33, 50, 60, 80] and it is the lexicographically smallest.

        ---------------------------------------------------------------------------------------------
            
        Example 2:
            Input: arr = [1, 3, 2, 4, 6, 5]
            Output: [1, 3, 4, 6]
            Explanation: Possible LIS sequences are [1, 3, 4, 6] and [1, 2, 4, 6]. Since [1, 3, 4, 6] is Index-wise Lexicographically Smaller, it is the result.
        
    ---------------------------------------------------------------------

    Constraints:
        1 <= arr.length <= 103
        -106 <= arr[i] <= 106
"""
from typing import List

def LIS(nums: List[int]) -> int:
    n = len(nums)
    dp = [1 for _ in range(n)]
    # Step 1: Build Parent + DP
    parent = [i for i in range(n)]
    for idx in range(n):
        for prev_idx in range(idx):
            if nums[prev_idx] < nums[idx]:
                if dp[idx] < 1 + dp[prev_idx]:
                    # Update parent[idx] whenever dp[idx] value is updated
                    parent[idx] = prev_idx
                    dp[idx] = 1 + dp[prev_idx]
    
    # Step 2: Find the index of last element of LIS (i.e, idx with max(dp))
    lastIdx = max(range(n), key=lambda i : dp[i])

    # Build the sequence (Backtracking)
    seq = []
    while parent[lastIdx] != lastIdx:
        seq.append(nums[lastIdx])
        lastIdx = parent[lastIdx]
    seq.append(nums[lastIdx])

    return seq[::-1]

if __name__ == '__main__':
    testCases = [
        [10, 22, 9, 33, 21, 50, 41, 60, 80],  # [10, 22, 33, 50, 60, 80]
        [1, 3, 2, 4, 6, 5],  # [1, 3, 4, 6]
        [7,7,7,7,7,7,7],    # [7]
    ]

    for i, nums in enumerate(testCases):
        print(f"TestCase {i}: i/p: nums={nums}; o/p: {LIS(nums)}")