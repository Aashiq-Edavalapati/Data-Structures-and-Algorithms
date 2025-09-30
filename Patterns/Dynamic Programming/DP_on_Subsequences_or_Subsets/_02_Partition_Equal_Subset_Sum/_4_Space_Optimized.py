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

def canPartition(nums: List[int]) -> bool:
        """
            Equal Sum partition => Sum of each subset = sum(nums) / 2 and sum(nums) should be even
            => Check if there is a subset that sum to sum(nums) / 2
        """

        totSum = sum(nums)
        if totSum % 2 == 1:
            return False
        reqSum = totSum // 2
        n = len(nums)
        prevRow = [False for _ in range(reqSum + 1)]
        prevRow[0] = True
        if nums[0] <= reqSum: prevRow[nums[0]] = 0

        for i in range(1, n):
            temp = [False for _ in range(reqSum + 1)]
            temp[0] = True
            for target in range(1, reqSum + 1):
                pick = False
                if target >= nums[i]:
                    pick = prevRow[target - nums[i]]
                notPick = prevRow[target]
                
                temp[target] = pick or notPick
            prevRow = temp
        
        return prevRow[reqSum]