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

def LIS(nums: List[int]) -> List[int]:
    n = len(nums)
    lis = []

    def helper(idx: int, prev_idx: int, path: List[int]) -> int:
        nonlocal lis

        if idx == n:
            return 0
        if len(path) >= len(lis):
            lis = path[:]

        take = 0
        notTake = helper(idx + 1, prev_idx, path)
        if prev_idx == -1 or nums[idx] > nums[prev_idx]:
            path.append(nums[idx])
            take = 1 + helper(idx + 1, idx, path)
            path.pop()

        return max(take, notTake)
    
    path = []
    lisLen = helper(0, -1, path)
    return lis

if __name__ == '__main__':
    testCases = [
        [10, 22, 9, 33, 21, 50, 41, 60, 80],  # [10, 22, 33, 50, 60, 80]
        [1, 3, 2, 4, 6, 5],  # [1, 3, 4, 6]
        [7,7,7,7,7,7,7],    # [7]
    ]

    for i, nums in enumerate(testCases):
        print(f"TestCase {i}: i/p: nums={nums}; o/p: {LIS(nums)}")