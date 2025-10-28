# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

"""
    @question:
        You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

        On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the stock at any time. However, you can sell and buy the stock multiple times on the same day, ensuring you never hold more than one share of the stock.

        Find and return the maximum profit you can achieve.

        
    ---------------------------------------------------------------------------------------------------------------
        Example 1:
            Input: prices = [7,1,5,3,6,4]
            Output: 7
            Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
                        Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
                        Total profit is 4 + 3 = 7.
        ---------------------------------------------------------
        Example 2:
            Input: prices = [1,2,3,4,5]
            Output: 4
            Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
                        Total profit is 4.
        -----------------------------------------------------------
        Example 3:
            Input: prices = [7,6,4,3,1]
            Output: 0
            Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
        
    --------------------------------------------------------------------------------------------------------------------

        Constraints:
            1 <= prices.length <= 3 * 104
            0 <= prices[i] <= 104
"""

from typing import List

def maxProfit(profits: List[int]) -> int:
    n = len(profits)
    def helper(idx: int, canBuy: bool) -> int:
        # Base Case
        # If we exhausted all the days, then return 0, because there's nothing left for us to do
        if idx == n:
            return 0

        # 1. If we can buy => Either choose to buy the current stock or move forward to buy another stock in future
        if canBuy:
            # 1.1 Buy the current stock => We should sell the stock before buying next stock => canBuy = False
            buy = -profits[idx] + helper(idx + 1, False)
            # 1.2 Don't buy the current stock => We should buy a stock before trying to sell => canBuy = True
            notBuy = helper(idx + 1, True)
            profit = max(buy, notBuy) # Profit is max of both since we are trying to maximize the profit
        # 2. If we cannot buy => Should sell before buying
        else:
            # 2.1 Sell the current stock => We should buy a stock before selling next time => canBuy = True
            sell = profits[idx] + helper(idx + 1, True)
            # 2.2 Don't sell the current stock => Move forward but canBuy = False because we have to buy the current holding before selling one
            notSell = helper(idx + 1, False)
            profit = max(sell, notSell) # Max of both paths
        
        return profit
    return helper(0, True)

if __name__ == '__main__':
    testCases = [
        [7,1,5,3,6,4], # 7
        [1,2,3,4,5],   # 4
        [7,6,4,3,1],   # 0
    ]

    for i, profits in enumerate(testCases):
        print(f"TestCase {i}: i/p: profits={profits}; o/p: {maxProfit(profits)}")