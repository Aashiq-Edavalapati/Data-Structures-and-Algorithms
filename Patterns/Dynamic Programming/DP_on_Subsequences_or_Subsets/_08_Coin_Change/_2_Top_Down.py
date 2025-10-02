"""
    @question:
        You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

        Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

        You may assume that you have an infinite number of each kind of coin.

        The answer is guaranteed to fit into a signed 32-bit integer.

        
        Example 1:
            Input: amount = 5, coins = [1,2,5]
            Output: 4
            Explanation: there are four ways to make up the amount:
            5=5
            5=2+2+1
            5=2+1+1+1
            5=1+1+1+1+1

        Example 2:
            Input: amount = 3, coins = [2]
            Output: 0
            Explanation: the amount of 3 cannot be made up just with coins of 2.

        Example 3:
            Input: amount = 10, coins = [10]
            Output: 1
        

        Constraints:
            1 <= coins.length <= 300
            1 <= coins[i] <= 5000
            All the values of coins are unique.
            0 <= amount <= 5000
"""
from typing import List


def change(amount: int, coins: List[int]) -> int:
    n = len(coins)
    dp = [[-1 for _ in range(amount + 1)] for _ in range(n)] # Initialize DP table. -> Parameters(2) [idx(0 to n - 1), target(0 to amount)] => 2D (n x (amount + 1))
    def helper(idx: int, target: int) -> int:
        # Base Cases
        if target == 0: return 1 # If target == 0 => An answer found => Increase count by 1 => Return 1
        if idx == 0: return 1 if target % coins[0] == 0 else 0 # idx == 0 => Current path is valid if arr[0] * x = target
        if target < 0: return 0
        if dp[idx][target] != -1: return dp[idx][target] # If answer available in dp table, return it

        # Choice 1: Pick the current element => Update target. Don't move to next element because the same element can be chosen multiple times
        pick = helper(idx, target - coins[idx])

        # Choice 2: Don't pick the current element => Move to next element
        notPick = helper(idx - 1, target)

        dp[idx][target] = pick + notPick # Store answer in DP table
        return dp[idx][target]
    
    return helper(n - 1, amount)

if __name__ == '__main__':
    testCases = [
        (5, [1,2,5]),      # 4
        (3, [2]),          # 0
        (10, [10]),        # 1
        (10, [2, 4,10]),   # 4
        (5,  [1, 2, 3, 5]) # 6
    ]

    for i, inp in enumerate(testCases):
        amount, coins = inp
        print(f'TestCase {i}: i/p: amount={amount}, coins={coins}; o/p: {change(amount, coins)}')
    