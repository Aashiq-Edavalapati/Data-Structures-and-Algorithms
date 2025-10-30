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
    k *= 2
    prev = [0 for _ in range(k + 1)] # Initialize prev row (nth row)
    for idx in range(n - 1, -1, -1):
        curr = [0 for _ in range(k + 1)]
        for transactions in range(k - 1, -1, -1):
            if transactions % 2 == 0:
                buy = -prices[idx] + prev[transactions + 1] # dp[idx + 1] => prev
                notBuy = prev[transactions]
                profit = max(buy, notBuy)
            else:
                sell = prices[idx] + prev[transactions + 1]
                notSell = prev[transactions]
                profit = max(sell, notSell)
            
            curr[transactions] = profit # dp[idx] => curr
        prev = curr # Update the curr row as prev row for next row

    return prev[0]

if __name__ == '__main__':
    testCases = [
        ([2,4,1], 2),   # 2
        ([3,2,6,5,0,3], 2), # 7
    ]

    for i, testCase in enumerate(testCases):
        prices, k = testCase
        print(f"TestCase {i}: i/p: prices={prices}, k={k}; o/p: {maxProfit(prices, k)}")