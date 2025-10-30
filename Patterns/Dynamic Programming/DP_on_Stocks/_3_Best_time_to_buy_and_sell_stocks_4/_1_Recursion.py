# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iv/

"""
    @question:
        You are given an integer array prices where prices[i] is the price of a given stock on the ith day, and an integer k.

        Find the maximum profit you can achieve. You may complete at most k transactions: i.e. you may buy at most k times and sell at most k times.

        Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

    ------------------------------------------------------------------------------------------------

        Example 1:
            Input: k = 2, prices = [2,4,1]
            Output: 2
            Explanation: Buy on day 1 (price = 2) and sell on day 2 (price = 4), profit = 4-2 = 2.
    
        ---------------------------------------------------------------------------------------
            
        Example 2:
            Input: k = 2, prices = [3,2,6,5,0,3]
            Output: 7
            Explanation: Buy on day 2 (price = 2) and sell on day 3 (price = 6), profit = 6-2 = 4. Then buy on day 5 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.

    -------------------------------------------------------------------------------------------   

        Constraints:
            1 <= k <= 100
            1 <= prices.length <= 1000
            0 <= prices[i] <= 1000
"""
from typing import List

def maxProfit(prices: List[int], k: int) -> int:
    n = len(prices)
    k += k # Because, we can perform k buys and k sells => k + k transactions
    def helper(idx: int, transactions: int) -> int:
        # Base Cases: Either we exhausted all the prices or completed k buys and sells => Return 0
        if idx == n or transactions == k:
            return 0
        
        # If transaction count is even => We have 0 stocks => Buy stock
        if transactions % 2 == 0:
            # Choice 1: Buy the current stock
            buy = -prices[idx] + helper(idx + 1, transactions + 1)
            # Choice 2: Buy some other stock
            notBuy = helper(idx + 1, transactions)
            profit = max(buy, notBuy) # Max profit of both the choices
        # Otherwise we have 1 stock => Sell stock
        else:
            # Choice 1: Sell for current price
            sell = prices[idx] + helper(idx + 1, transactions + 1)
            # Choice 2: Sell at some other price
            notSell = helper(idx + 1, transactions)
            profit = max(sell, notSell) # Max profit out of both the choices
        
        return profit

    return helper(0, 0)

if __name__ == '__main__':
    testCases = [
        ([2,4,1], 2),   # 2
        ([3,2,6,5,0,3], 2), # 7
    ]

    for i, testCase in enumerate(testCases):
        prices, k = testCase
        print(f"TestCase {i}: i/p: prices={prices}, k={k}; o/p: {maxProfit(prices, k)}")