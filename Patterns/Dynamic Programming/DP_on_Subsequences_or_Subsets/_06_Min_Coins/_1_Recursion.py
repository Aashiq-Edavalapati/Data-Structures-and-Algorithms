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

"""
    @intuition:
        Since there is minimization included, we obviously think of DP! Since we are trying all the possible combinations of coins, we try pick/notPick. But since, we can take a coin any number of times, we won't move to next coing in pick, we move only in notPick.
"""
def minCoins(coins: List[int], target: int):
    def helper(ind: int, rem: int):
        # Base Cases
        if rem < 0: return float('inf') # If remaining coins < 0 => Current sum exceeded the target => Invalid path
        if rem == 0: return 0 # If remaining coins = 0 => Target achieved => Return 0(Not 1, since we are updating the coin count in pick)
        # if ind == 0, there are no more coins to explore further!
        if ind == 0: return rem // coins[0] if rem % coins[0] == 0 else float('inf')

        # Case 1: Pick the current coin => Don't move to next coing, but update remaining remaining value and coin count
        pick = 1 + helper(ind, rem - coins[ind]) 
        # Case 2: Don't pick the current coin => Move to next coin
        notPick = helper(ind - 1, rem)

        # Return minimum of both the paths
        return min(pick, notPick)
    
    n = len(coins)
    ans = helper(n - 1, target)
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