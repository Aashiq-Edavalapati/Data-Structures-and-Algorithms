# @Link: https://leetcode.com/problems/partition-equal-subset-sum/
from typing import List

"""
    @question:
        Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
    ---------------------------------------
        Example 1:
            Input: nums = [1,5,11,5]
            Output: true
            Explanation: The array can be partitioned as [1, 5, 5] and [11].
    ----------------------------------------
        Example 2:
            Input: nums = [1,2,3,5]
            Output: false
            Explanation: The array cannot be partitioned into equal sum subsets.
    -----------------------------------------
        Constraints:
            1 <= nums.length <= 200
            1 <= nums[i] <= 100
"""

def canBePartitioned(arr: List[int]) -> bool:
    def subsetSumEqualsTarget(idx: int, target: int) -> int:
        if target == 0: return True
        if idx == 0: return arr[0] == target
        if target < 0: return False

        pick = subsetSumEqualsTarget(idx - 1, target - arr[idx])
        notPick = subsetSumEqualsTarget(idx - 1, target)

        return pick or notPick

    n = len(arr)
    totSum = sum(arr)
    if totSum % 2 == 1: return False
    target = totSum // 2
    return subsetSumEqualsTarget(n - 1, target)


if __name__ == '__main__':
    testCases = [
        [1,5,11,5],     # true
        [1,2,3,5],      # false
    ]

    for i, arr in enumerate(testCases):
        print(f'TestCase {i}: i/p: arr={arr}; o/p: {canBePartitioned(arr)}')