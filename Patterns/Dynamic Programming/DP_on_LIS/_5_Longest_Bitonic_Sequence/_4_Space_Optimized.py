"""
    @question:
        Given an array arr of n integers, the task is to find the length of the longest bitonic sequence. A sequence is considered bitonic if it first increases, then decreases. The sequence does not have to be contiguous.


        Examples:
            Input: arr = [5, 1, 4, 2, 3, 6, 8, 7]
            Output: 6
            Explanation: The longest bitonic sequence is [1, 2, 3, 6, 8, 7] with length 6.
    -----------------------------------
            Input: arr = [10, 20, 30, 40, 50, 40, 30, 20]
            Output: 8
            Explanation: The entire array is bitonic, increasing up to 50 and then decreasing.
----------------------------------------------------------------------------------------
        Constraints:
            1 <= arr.length <= 103
            -106<= arr[i] <= 106
"""
from typing import List

def longestBitonicSequence(nums: List[int]) -> int:
    """
        In the bottom-up solution make the following replacements:    
            - dp[idx + 1] => prevRow
            - dp[idx] => curr
    """
    n = len(nums)
    prevRow = [[0 for _ in range(2)] for _ in range(n + 1)]
    for idx in range(n - 1, -1, -1):
        curr = [[0 for _ in range(2)] for _ in range(n + 1)]
        for prev in range(idx - 1, -2, -1):
            for isIncreasing in range(2):
                pick = 0
                if prev == -1:
                    pick = 1 + prevRow[idx + 1][1]
                elif isIncreasing == 1:
                    if nums[idx] >= nums[prev]:
                        pick = 1 + prevRow[idx + 1][1]
                    else:
                        pick = 1 + prevRow[idx + 1][0]
                elif nums[idx] <= nums[prev]:
                    pick = 1 + prevRow[idx + 1][0]

                notPick = prevRow[prev + 1][isIncreasing]

                curr[prev + 1][isIncreasing] =  max(pick, notPick)
        prevRow = curr

    return prevRow[0][1]

if __name__ == '__main__':
    testCases = [
        [5, 1, 4, 2, 3, 6, 8, 7], # 6
        [10, 20, 30, 40, 50, 40, 30, 20], # 8
        [12, 11, 10, 15, 18, 17, 16, 14], # 6
        [1, 11, 2, 10, 4, 5, 2, 1], # 6
    ]

    for i, nums in enumerate(testCases):
        print(f"TestCase {i}:- i/p: nums={nums}; o/p: {longestBitonicSequence(nums)}")