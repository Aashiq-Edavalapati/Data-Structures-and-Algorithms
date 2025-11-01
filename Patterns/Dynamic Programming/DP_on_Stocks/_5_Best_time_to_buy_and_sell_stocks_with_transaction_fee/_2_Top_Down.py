# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-transaction-fee/

"""
    @question:
        You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

        Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

        Note:

        You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
        The transaction fee is only charged once for each stock purchase and sale.
        
    ---------------------------------------------------------------------------------------

        Example 1:
            Input: prices = [1,3,2,8,4,9], fee = 2
            Output: 8
            Explanation: The maximum profit can be achieved by:
                - Buying at prices[0] = 1
                - Selling at prices[3] = 8
                - Buying at prices[4] = 4
                - Selling at prices[5] = 9
                The total profit is ((8 - 1) - 2) + ((9 - 4) - 2) = 8.
        
        ---------------------------------------------------------------

        Example 2:
            Input: prices = [1,3,7,5,10,3], fee = 3
            Output: 6
    
    ----------------------------------------------------------------------------------

        Constraints:
            1 <= prices.length <= 5 * 104
            1 <= prices[i] < 5 * 104
            0 <= fee < 5 * 104
"""
from typing import List

def maxProfit(prices: List[int], fee) -> int:
    n = len(prices)
    dp = [[-1, -1] for _ in range(n)] # Initialize the DP table
    def helper(idx: int, canBuy: int) -> int:
        if idx == n:
            return 0
        if dp[idx][canBuy] != -1: return dp[idx][canBuy] # If the result was stored in the DP table, return it
        
        if canBuy:
            buy = -prices[idx] + helper(idx + 1, 0)
            notBuy = helper(idx + 1, 1)
            profit = max(buy, notBuy)
        else:
            sell = prices[idx] - fee + helper(idx + 1, 1)
            notSell = helper(idx + 1, 0)
            profit = max(sell, notSell)
        
        dp[idx][canBuy] = profit # Store the result in the DP table
        return profit
    
    return helper(0, 1)

if __name__ == '__main__':
    testCases = [
        ([1,3,2,8,4,9], 2),    # 8
        ([1,3,7,5,10,3], 3),    # 6
    ]

    for i, testCase in enumerate(testCases):
        prices, fee = testCase
        print(f"TestCase {i}: i/p: prices={prices}, fee={fee}, o/p: {maxProfit(prices, fee)}")