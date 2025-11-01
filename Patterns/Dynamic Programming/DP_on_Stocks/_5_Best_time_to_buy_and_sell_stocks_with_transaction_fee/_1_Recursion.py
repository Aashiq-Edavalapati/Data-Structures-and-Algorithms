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
    def helper(idx: int, canBuy: bool) -> int:
        # Base Case: If index out of bounds => Return 0
        if idx == n:
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
            # Choice 1: Sell the curr stock => 1 transaction finish => deduct transaction fee from the profit
            sell = prices[idx] - fee + helper(idx + 1, True)
            # Choice 2: Skip the curr stock and sell at some other price
            notSell = helper(idx + 1, False)
            profit = max(sell, notSell) # Find max profit of both the cases
        
        return profit
    
    return helper(0, True)

if __name__ == '__main__':
    testCases = [
        ([1,3,2,8,4,9], 2),    # 8
        ([1,3,7,5,10,3], 3),    # 6
    ]

    for i, testCase in enumerate(testCases):
        prices, fee = testCase
        print(f"TestCase {i}: i/p: prices={prices}, fee={fee}, o/p: {maxProfit(prices, fee)}")