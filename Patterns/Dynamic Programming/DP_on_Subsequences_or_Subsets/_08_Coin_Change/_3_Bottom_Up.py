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
    dp = [[0 for _ in range(amount + 1)] for _ in range(n)] # Initialize DP table. -> Parameters(2) [idx(0 to n - 1), target(0 to amount)] => 2D (n x (amount + 1))

    # 1. Base Cases
    for row in dp:
        row[0] = 1 # target == 0
    for target in range(amount + 1):
        dp[0][target] = 1 if target % coins[0] == 0 else 0 # idx == 0
    # Since, index can't be negative => We'll handle in the for loop

    # Start iterating from bottom to up (From base case to the initial function call)
    for idx in range(1, n): # idx == 0 is a base case => Start from 1
        for target in range(1, amount + 1): # target == 0 is a base case => Start from 1
            pick = 0
            if target - coins[idx] >= 0:
                pick = dp[idx][target - coins[idx]]
            notPick = dp[idx - 1][target]

            dp[idx][target] = pick + notPick
    
    return dp[n - 1][amount]

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
    