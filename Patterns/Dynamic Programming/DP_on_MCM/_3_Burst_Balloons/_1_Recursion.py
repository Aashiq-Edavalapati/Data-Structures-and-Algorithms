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

"""
    @intuition:
        - Each time we pick a balloon and burst it out => Similar to MCM, where we replace a matrix with resultant of multiplication of two matrices

        - Now, if we try to solve this problem in a similar way to MCM:
            - Let the balloons be [b1, b2, b3, b4, b5, b6, b7].
            - Let's say we choose b3 first => The next subproblems would be [b1, b2] and [b4, b5, b6, b7]
            - But if we notice carefully, both subproblems cannot be solved independently, because b2's coins incluldes b4 as well and vice-versa.
            - So, obviously this approach doesn't work
        
        - Then, why don't we think in the opposite direction? => Starting from last ballon that's been popped and moving upwards:
            - Let the balloons be [b1, b2, b3, b4, b5, b6, b7].
            - Let's say we choose b3 first(i.e., last balloon to be burst) => cost would be 1 * b3 * 1
            - Then the resulting next subproblems would be [b1, b2] and [b4, b5, b6, b7]:
                At this state if we choose b5 (W.k.t, the next balloon that will be burst after b5 is b3) and 
                from observation we know that b5 is the 2nd last balloon => Only b3, b5 are left at this point actually => cost = b3 * b5 * 1
            - So, by observing this carefully => cost = nums[i - 1] * nums[k] * nums[j + 1], where i = start of curr subproblem, j = end of curr subproblem, k is the index of the balloon that we choose in curr function call.
"""
def maxCoins(nums: List[int]) -> int:
    n = len(nums)
    # Add 1 at the start and end to avoid index out of bound handling
    nums.insert(0, 1)
    nums.append(1)
    def helper(i: int, j: int) -> int:
        if i > j: return 0

        maxi = 0
        # Try by choosing all the indices in curr subproblem and find max of all the choices
        for k in range(i, j + 1):
            cost = nums[k] * nums[i - 1] * nums[j + 1] + helper(i, k - 1) + helper(k + 1, j)
            maxi = max(maxi, cost)

        return maxi
    
    return helper(1, n)

if __name__ == '__main__':
    testCases = [
        [3,1,5,8], # 167
        [1,5], # 10
    ]

    for i, nums in enumerate(testCases):
        print(f"TestCase {i}:- i/p: nums={nums}; o/p: {maxCoins(nums)}")