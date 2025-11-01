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
    def helper(idx: int, canBuy: bool) -> int:
        # Base Case: If index out of bounds => Return 0
        if idx >= n:
            return 0
        
        # If canBuy == True => We have 0 stocks => Buy
        if canBuy:
            # Choice 1: Buy the curr stock
            buy = -prices[idx] + helper(idx + 1, False)
            # Choice 2: Skip the curr stock and buy some other stock
            notBuy = helper(idx + 1, True)
            profit = max(buy, notBuy) # Find max profit of both the paths
        # Otherwise, We have 1 stock => Sell
        else:
            # Choice 1: Sell the curr stock => Cooldown for next stock => Move to idx + 2 instead of idx + 1
            sell = prices[idx] + helper(idx + 2, True)
            # Choice 2: Skip the curr stock and sell at some other price
            notSell = helper(idx + 1, False)
            profit = max(sell, notSell) # Find max profit of both the cases
        
        return profit
    
    return helper(0, True)

if __name__ == '__main__':
    testCases = [
        [1,2,3,0,2],    # 3
        [1],    # 0
        [1, 2], # 1
    ]

    for i, prices in enumerate(testCases):
        print(f"TestCase {i}: i/p: prices={prices}, o/p: {maxProfit(prices)}")