"""
    @question:
        Given a chain of matrices A1, A2, A3,.....An, you have to figure out the most efficient way to multiply these matrices. In other words, determine where to place parentheses to minimize the number of multiplications.
        
        Given an array nums of size n. Dimension of matrix Ai ( 0 < i < n ) is nums[i - 1] x nums[i].Find a minimum number of multiplications needed to multiply the chain.

    ---------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------

        Examples:
            Input : nums = [10, 15, 20, 25]
            Output : 8000
            Explanation : There are two ways to multiply the chain - A1*(A2*A3) or (A1*A2)*A3.
                        If we multiply in order- A1*(A2*A3), then number of multiplications required are 11250.
                        If we multiply in order- (A1*A2)*A3, then number of multiplications required are 8000.
                        Thus minimum number of multiplications required is 8000.

        -------------------------------------------------------------------------------
                        
        Input : nums = [4, 2, 3]
        Output : 24
        Explanation : There is only one way to multiply the chain - A1*A2.
                      Thus minimum number of multiplications required is 24.

    -------------------------------------------------------------------------------
    -------------------------------------------------------------------------------

    Constraints:
        2 <= n <= 100
        1 <= nums[i] <= 100
"""
from typing import List

def mcm(nums: List[int]) -> int:
    n = len(nums)
    # Initialize the DP table (Size: i -> (1, n - 1), j -> (n - 1, 1))
    dp = [[-1 for _ in range(n)] for _ in range(n)]
    def helper(i: int, j: int) -> int:
        if i == j: return 0
        if dp[i][j] != -1: return dp[i][j] # If result already stored in DP table, return
        minOps = float('inf')
        for k in range(i, j):
            ops = nums[i - 1] * nums[j] * nums[k] + helper(i, k) + helper(k + 1, j)
            minOps = min(minOps, ops)
        
        # Store the result in DP table
        dp[i][j] = minOps
        return minOps

    return helper(1, n - 1)

if __name__ == '__main__':
    testCases = [
        [10, 15, 20, 25], # 8000
        [4, 2, 3], # 24
    ]

    for i, nums in enumerate(testCases):
        print(f"TestCase {i}:- i/p: nums={nums}; o/p: {mcm(nums)}")