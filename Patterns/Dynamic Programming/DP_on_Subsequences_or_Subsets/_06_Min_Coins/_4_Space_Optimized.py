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
    # Initialize prev and curr arrays
    prev = [-1 for _ in range(amount + 1)]
    curr = [-1 for _ in range(amount + 1)]

    # Base Cases
    # Case 1: rem = 0 => return 0
    prev[0] = 0
    curr[0] = 0
    # Case 2: idx = 0 => return rem // coins[0] if rem % coins[0] == 0 else float('inf')
    for rem in range(1, amount + 1):
        prev[rem] = rem // coins[0] if rem % coins[0] == 0 else float('inf')

    for ind in range(1, n):
        for rem in range(1, amount + 1):
            pick = float('inf')
            if rem - coins[ind] >= 0: # Index bound check (Base Case 3: rem < 0 => float('inf'))
                pick = 1 + curr[rem - coins[ind]] # f(idx, rem - coins[idx]) => curr[rem - coins[idx]]
            notPick = prev[rem] # f(idx - 1, rem) => prev[rem]

            curr[rem] = min(pick, notPick) # f(idx, rem) => curr[rem]
        prev = curr[:] # Update current row as prev row
    
    ans = prev[amount]
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