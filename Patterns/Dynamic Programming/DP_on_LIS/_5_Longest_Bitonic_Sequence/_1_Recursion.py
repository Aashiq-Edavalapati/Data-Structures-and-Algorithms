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
        # Base Case: If idx = n => We've reached the end
        if idx == n: return 0

        # Choice 1: Pick the current element
        pick = 0
        # If prev == -1 => We've not chosen any element yet! So, we can pick the curr element without checking
        if prev == -1:
            pick = 1 + helper(idx + 1, idx, True)
        # prev != -1 => We've chosen some elements => We have to compare and check curr element with prev element before picking the curr element
        # If isIncreasing is True => We are in 1st half of the solution => curr element may extend the 1st half or may be start of the 2nd half
        elif isIncreasing:
            # If curr element >= prev element => Still in 1st half(i.e., increasing)
            if nums[idx] >= nums[prev]:
                pick = 1 + helper(idx + 1, idx, True)
            # Otherwise, if we pick curr element => From here on the sequence should be decreasing
            else:
                pick = 1 + helper(idx + 1, idx, False)
        # If isIncreasing is False => We are in decreasing part => Curr element should satisfy decreasing property if we want to pick it
        elif nums[idx] <= nums[prev]:
            pick = 1 + helper(idx + 1, idx, False)

        # Choice 2: Don't pick the current element => Just move to next idx and there will be no change in prev and isIncreasing
        notPick = helper(idx + 1, prev, isIncreasing)

        # Return max of both the choices
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