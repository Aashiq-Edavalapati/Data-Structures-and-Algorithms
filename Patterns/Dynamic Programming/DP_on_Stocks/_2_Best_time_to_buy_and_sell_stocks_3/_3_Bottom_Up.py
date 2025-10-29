# Link: https://leetcode.com/problems/best-time-to-buy-and-sell-stock-iii/description/

"""
    @question:
        You are given an array prices where prices[i] is the price of a given stock on the ith day.

        Find the maximum profit you can achieve. You may complete at most two transactions.

        Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).
        
    ------------------------------------------------------------------------------------------------------------
        
        Example 1:
            Input: prices = [3,3,5,0,0,3,1,4]
            Output: 6
            Explanation: Buy on day 4 (price = 0) and sell on day 6 (price = 3), profit = 3-0 = 3.
            Then buy on day 7 (price = 1) and sell on day 8 (price = 4), profit = 4-1 = 3.
        
        -------------------------------------------------------------------------------------------
        
        Example 2:
            Input: prices = [1,2,3,4,5]
            Output: 4
            Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
            Note that you cannot buy on day 1, buy on day 2 and sell them later, as you are engaging multiple transactions at the same time. You must sell before buying again.
        
        --------------------------------------------------------------------------------------------------
            
        Example 3:
            Input: prices = [7,6,4,3,1]
            Output: 0
            Explanation: In this case, no transaction is done, i.e. max profit = 0.
    
    -----------------------------------------------------------------------------------

        Constraints:
            1 <= prices.length <= 105
            0 <= prices[i] <= 105
"""

from typing import List


def maxProfit(prices: List[int]) -> int:
    n = len(prices)
    dp = [[[0, 0] for _ in range(3)] for _ in range(n + 1)]

    for idx in range(n - 1, -1, -1):
        for sold in range(1, -1, -1):
            for canBuy in range(1, -1, -1):
                if canBuy:
                    buy = -prices[idx] + dp[idx + 1][sold][0]
                    notBuy = dp[idx + 1][sold][1]
                    profit = max(buy, notBuy)
                else:
                    sell = prices[idx] + dp[idx + 1][sold + 1][1]
                    notSell = dp[idx + 1][sold][0]
                    profit = max(sell, notSell)
                
                # Store the result in DP table
                dp[idx][sold][canBuy] = profit

    return dp[0][0][1]

def maxProfit2(prices: List[int]) -> int:
    """
        Method 2: After each buy or sell, increase the transactions count => 
                        Even count => Buy, Odd Count => Sell
    """
    n = len(prices)
    dp = [[0 for _ in range(5)] for _ in range(n + 1)]
    for idx in range(n - 1, -1, -1):
        for transaction in range(3, -1, -1):
            if transaction % 2 == 0:
                buy = -prices[idx] + dp[idx + 1][transaction + 1]
                notBuy = dp[idx + 1][transaction]
                profit = max(buy, notBuy)
            else:
                sell = prices[idx] + dp[idx + 1][transaction + 1]
                notSell = dp[idx + 1][transaction]
                profit = max(sell, notSell)

            dp[idx][transaction] = profit
    
    return dp[0][0]


if __name__ == '__main__':
    testCases = [
        [3,3,5,0,0,3,1,4],  # 6
        [1,2,3,4,5],    # 4
        [7,6,4,3,1],    # 0
    ]

    for i, prices in enumerate(testCases):
        print(f"TestCase {i}: i/p: prices={prices}; o/p: {maxProfit2(prices)}")