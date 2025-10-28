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
    prev = [0, 0] # n + 1 th row (i.e., idx == n)
    for idx in range(n - 1, -1, -1):
        curr = [0, 0] # dp[idx]
        for canBuy in range(1, -1, -1):
            if canBuy == 1:
                buy = -profits[idx] + prev[0] # dp[idx + 1] => prev
                notBuy =prev[1] # dp[idx + 1] = prev
                profit = max(buy, notBuy)
            else:
                sell = profits[idx] +prev[1] # dp[idx + 1] => prev
                notSell =prev[0] # dp[idx + 1] => prev
                profit = max(sell, notSell)
            
            curr[canBuy] = profit   # dp[idx] => curr
        prev = curr # Update the current row as prev row for next row
 
    return prev[1]

if __name__ == '__main__':
    testCases = [
        [7,1,5,3,6,4], # 7
        [1,2,3,4,5],   # 4
        [7,6,4,3,1],   # 0
    ]

    for i, profits in enumerate(testCases):
        print(f"TestCase {i}: i/p: profits={profits}; o/p: {maxProfit(profits)}")