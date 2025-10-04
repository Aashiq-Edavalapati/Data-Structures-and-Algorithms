"""
    @question:
        Given two integer arrays, val and wt, each of size N, representing the values and weights of N items respectively, and an integer W, representing the maximum capacity of a knapsack, determine the maximum value achievable by selecting a subset of the items such that the total weight of the selected items does not exceed the knapsack capacity W. The goal is to maximize the sum of the values of the selected items while keeping the total weight within the knapsack's capacity.

        An infinite supply of each item can be assumed.

        Examples:
            Input: val = [5, 11, 13], wt = [2, 4, 6], W = 10
            Output: 27
            Explanation: Select 2 items with weights 4 and 1 item with weight 2 for a total value of 11+11+5 = 27.
        ---------------------------------------------------------------------------------------------------------
            
            Input: val = [10, 40, 50, 70], wt = [1, 3, 4, 5], W = 8
            Output: 110
            Explanation: Select items with weights 3 and 5 for a total value of 40 + 70 = 110.

    ----------------------------
        Constraints:
            1 ≤ N ≤ 500
            1 ≤ W ≤ 1000
            1 ≤ wt[i] ≤ 500
            1 ≤ val[i] ≤ 500
"""
from typing import List

"""Read the comments with respect to the code from _1_Recursion.py(Brute Force)!"""
def unboundedKnapsack(wt, val, n, W):
    dp = [[-1 for _ in range(W + 1)] for _ in range(n)] # Initialize the DP table
    def helper(idx: int, W: int) -> int:
        # 1. Base Case
        if idx < 0: return 0 # If idx < 0 => The current path completed!
        if dp[idx][W] != -1: return dp[idx][W] # If the answer is stored in the DP table, return it

        # Choice 1: Pick the current element
        pick = 0
        if wt[idx] <= W: # Pick only if weight of current element <= Weight of the bag
            pick = val[idx] + helper(idx, W - wt[idx]) # Increase profit by val[idx] and stay at the same because each element can be taken any number of times. Update remaining capacity of the bag!

        # Choice 2: Don't pick the current element
        notPick = helper(idx - 1, W) # Move to the next element

        dp[idx][W] = max(pick, notPick)  # Store the result in the DP table
        return dp[idx][W]

    return helper(n - 1, W)


if __name__ == '__main__':
    testCases = [
        ([5, 11, 13], [2, 4, 6], 3 ,10),  # 27
        ([10, 40, 50, 70], [1, 3, 4, 5], 4, 8)  # 110
    ]

    for i, inp in enumerate(testCases):
        val, wt, n, W = inp
        print(f'TestCase {i}: i/p: wt={wt}, val={val}, n={n}, W={W}; o/p: {unboundedKnapsack(wt, val, n, W)}')