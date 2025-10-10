# Link: https://leetcode.com/problems/coin-change/

"""
    @question:
        You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

        Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.

        You may assume that you have an infinite number of each kind of coin.  

        Example 1:
            Input: coins = [1,2,5], amount = 11
            Output: 3
            Explanation: 11 = 5 + 5 + 1
    --------------------------------------------------
        Example 2:
            Input: coins = [2], amount = 3
            Output: -1
    --------------------------------------------------
        Example 3:
            Input: coins = [1], amount = 0
            Output: 0
    --------------------------------------------------
        Constraints:
            1 <= coins.length <= 12
            1 <= coins[i] <= 231 - 1
            0 <= amount <= 104
"""
from typing import List

def minCoins(coins: List[int], amount: int):
    n = len(coins)
    dp = [[-1 for _ in range(amount + 1)] for _ in range(n)] # Initialize DP table of same size as in Top-Down approach
    # Base Cases
    # Case 1: target = 0 => return 0
    for row in dp:
        row[0] = 0
    # Case 2: idx = 0 => return rem // coins[0] if rem % coins[0] == 0 else float('inf')
    for rem in range(1, amount + 1): 
        dp[0][rem] = rem // coins[0] if rem % coins[0] == 0 else float('inf')

    # Start iterating
    for ind in range(1, n): # Since idx = 0 is base case, start from 1
        for rem in range(1, amount + 1): # Since rem = 0 is a base case, start from 1
            pick = float('inf')
            if rem - coins[ind] >= 0:
                pick = 1 + dp[ind][rem - coins[ind]]
            notPick = dp[ind - 1][rem]

            dp[ind][rem] = min(pick, notPick)
    
    ans = dp[n - 1][amount]
    return ans if ans != float('inf') else -1


if __name__ == '__main__':
    testCases = [
        ([1, 2, 5], 11),     # 3
        ([2], 3),            # -1
        ([1], 0),            # 0
        ([2, 5], 3),         # -1
    ]

    for i, inp in enumerate(testCases):
        coins, target = inp
        print(f'TestCase {i}: i/p: coins={coins}, target={target}; o/p: {minCoins(coins, target)}')