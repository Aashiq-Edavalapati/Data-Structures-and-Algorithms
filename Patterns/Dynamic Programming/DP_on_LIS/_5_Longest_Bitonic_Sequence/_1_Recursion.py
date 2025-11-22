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
    n = len(nums)
    def helper(idx: int, prev: int, isIncreasing: bool) -> int:
        if idx == n: return 0
        pick = 0
        if prev == -1:
            pick = 1 + helper(idx + 1, idx, True)
        elif isIncreasing:
            if nums[idx] >= nums[prev]:
                pick = 1 + helper(idx + 1, idx, True)
            else:
                pick = 1 + helper(idx + 1, idx, False)
        elif nums[idx] <= nums[prev]:
            pick = 1 + helper(idx + 1, idx, False)

        notPick = helper(idx + 1, prev, isIncreasing)

        return max(pick, notPick)

    return helper(0, -1, True)

if __name__ == '__main__':
    testCases = [
        [5, 1, 4, 2, 3, 6, 8, 7], # 6
        [10, 20, 30, 40, 50, 40, 30, 20], # 8
        [12, 11, 10, 15, 18, 17, 16, 14], # 6
        [1, 11, 2, 10, 4, 5, 2, 1], # 6
    ]

    for i, nums in enumerate(testCases):
        print(f"TestCase {i}:- i/p: nums={nums}; o/p: {longestBitonicSequence(nums)}")