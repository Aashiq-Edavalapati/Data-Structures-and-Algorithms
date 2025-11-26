# Link: https://leetcode.com/problems/burst-balloons/

"""
    @question:
        You are given n balloons, indexed from 0 to n - 1. Each balloon is painted with a number on it represented by an array nums. You are asked to burst all the balloons.
        If you burst the ith balloon, you will get nums[i - 1] * nums[i] * nums[i + 1] coins. If i - 1 or i + 1 goes out of bounds of the array, then treat it as if there is a balloon with a 1 painted on it.
        Return the maximum coins you can collect by bursting the balloons wisely.

    -------------------------------------------------------------------------------------
    -------------------------------------------------------------------------------------

        Example 1:
            Input: nums = [3,1,5,8]
            Output: 167
            Explanation:
            nums = [3,1,5,8] --> [3,5,8] --> [3,8] --> [8] --> []
            coins =  3*1*5    +   3*5*8   +  1*3*8  + 1*8*1 = 167
        
        -------------------------------------------------------------------------------------

        Example 2:
            Input: nums = [1,5]
            Output: 10
    
    -------------------------------------------------------------------------------------
    -------------------------------------------------------------------------------------

        Constraints:
            n == nums.length
            1 <= n <= 300
            0 <= nums[i] <= 10
"""
from typing import List

def maxCoins(nums: List[int]) -> int:
    n = len(nums)
    nums.insert(0, 1)
    nums.append(1)
    dp = [[0 for _ in range(n + 2)] for _ in range(n + 2)] # Initialize the DP table(Base case already handled)
    # Start iterating over changing params in reverse order to that of top-down(recursion)
    for i in range(n, 0, -1):
        for j in range(i, n + 1):
            maxi = 0
            for k in range(i, j + 1):
                cost = nums[k] * nums[i - 1] * nums[j + 1] + dp[i][k - 1] + dp[k + 1][j] # f(i, j) => dp[i][j]
                maxi = max(maxi, cost)

            dp[i][j] = maxi
    
    return dp[1][n]

if __name__ == '__main__':
    testCases = [
        [3,1,5,8], # 167
        [1,5], # 10
    ]

    for i, nums in enumerate(testCases):
        print(f"TestCase {i}:- i/p: nums={nums}; o/p: {maxCoins(nums)}")