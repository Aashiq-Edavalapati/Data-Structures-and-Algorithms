# Link: https://leetcode.com/problems/count-partitions-with-max-min-difference-at-most-k/

"""
    @question:
        You are given an integer array nums and an integer k. Your task is to partition nums into one or more non-empty contiguous segments such that in each segment, the difference between its maximum and minimum elements is at most k.
        Return the total number of ways to partition nums under this condition.
        Since the answer may be too large, return it modulo 109 + 7.

    -------------------------------------------------------------------------------------
    -------------------------------------------------------------------------------------
        
        Example 1:
            Input: nums = [9,4,1,3,7], k = 4
            Output: 6
            Explanation:
                There are 6 valid partitions where the difference between the maximum and minimum elements in each segment is at most k = 4:

                [[9], [4], [1], [3], [7]]
                [[9], [4], [1], [3, 7]]
                [[9], [4], [1, 3], [7]]
                [[9], [4, 1], [3], [7]]
                [[9], [4, 1], [3, 7]]
                [[9], [4, 1, 3], [7]]
        
        -------------------------------------------------------------------------------------
                
        Example 2:
            Input: nums = [3,3,4], k = 0
            Output: 2
            Explanation:
                There are 2 valid partitions that satisfy the given conditions:

                [[3], [3], [4]]
                [[3, 3], [4]]
        
    -------------------------------------------------------------------------------------
    -------------------------------------------------------------------------------------

        Constraints:
            2 <= nums.length <= 5 * 104
            1 <= nums[i] <= 109
            0 <= k <= 109
"""
from typing import List

def countPartitions(nums: List[int], k: int) -> int:
    MOD = 10 ** 9 + 7
    n = len(nums)
    dp = [-1] * n
    def helper(i: int) -> int:
        if i == n: return 1
        if dp[i] != -1: return dp[i]

        maxi, mini = nums[i], nums[i]
        cnt = 0
        for j in range(i, n):
            maxi = max(maxi, nums[j])
            mini = min(mini, nums[j])
            if maxi - mini > k:
                break
            parti = helper(j + 1)
            cnt = (cnt + parti) % MOD

        dp[i] = cnt % MOD
        return dp[i]

    return helper(0)

if __name__ == '__main__':
    testCases = [
        ([9,4,1,3,7], 4), # 6
        ([3,3,4], 0), # 2
    ]

    for i, testCase in enumerate(testCases):
        nums, k = testCase
        print(f"TestCase {i}:- i/p: nums={nums}, k={k}; o/p: {countPartitions(nums, k)}")