# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/

"""
    @question:
        You are given an array prices where prices[i] is the price of a given stock on the ith day.

        Find the maximum profit you can achieve. You may complete as many transactions as you like (i.e., buy one and sell one share of the stock multiple times) with the following restrictions:

        After you sell your stock, you cannot buy stock on the next day (i.e., cooldown one day).
        Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

    ----------------------------------------------------------------------

        Example 1:
            Input: prices = [1,2,3,0,2]
            Output: 3
            Explanation: transactions = [buy, sell, cooldown, buy, sell]
    
        ------------------------------------------------------------
        
        Example 2:
            Input: prices = [1]
            Output: 0
        
    -------------------------------------------

        Constraints:
            1 <= prices.length <= 5000
            0 <= prices[i] <= 1000
"""
from typing import List

def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    dp = [[-1, -1] for _ in range(n)] # Initialize the DP table
    def helper(idx: int, canBuy: int) -> int:
        if idx >= n:
            return 0
        if dp[idx][canBuy] != -1: return dp[idx][canBuy] # If the result was stored in the DP table => Return the result
        
        if canBuy == 1:
            buy = -prices[idx] + helper(idx + 1, 0)
            notBuy = helper(idx + 1, 1)
            profit = max(buy, notBuy)
        else:
            sell = prices[idx] + helper(idx + 2, 1)
            notSell = helper(idx + 1, 0)
            profit = max(sell, notSell)
        
        dp[idx][canBuy] = profit # Store the result in the DP table
        return profit
    
    return helper(0, 1)

if __name__ == '__main__':
    testCases = [
        [1,2,3,0,2],    # 3
        [1],    # 0
        [1, 2], # 1
    ]

    for i, prices in enumerate(testCases):
        print(f"TestCase {i}: i/p: prices={prices}, o/p: {maxProfit(prices)}")