"""
    @question:
        Given a rod of length N inches and an array price[] where price[i] denotes the value of a piece of rod of length i inches (1-based indexing). Determine the maximum value obtainable by cutting up the rod and selling the pieces. Make any number of cuts, or none at all, and sell the resulting pieces.

        Examples:
            Input: price = [1, 6, 8, 9, 10, 19, 7, 20], N = 8
            Output: 25
            Explanation: Cut the rod into lengths of 2 and 6 for a total price of 6 + 19= 25.
        ----------------------------------------------------------------------------------------
            Input: price = [1, 5, 8, 9], N = 4
            Output: 10
            Explanation: Cut the rod into lengths of 2 and 2 for a total price of 5 + 5 = 10.
        
        
        Constraints:
            1 ≤ N ≤ 1000
            1 ≤ price[i] ≤ 105
"""

from typing import List

def rodCutting(price: List[int], n: int) -> int:
    dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)] # Initialize DP table
    def solve(curr: int, rem: int):
        if rem == 0 or curr > rem:
            return 0
        if dp[curr][rem] != -1: return dp[curr][rem] # If the result was stored in DP table, return it

        pick = price[curr - 1] + solve(curr, rem - curr)
        notPick = solve(curr + 1, rem)

        # Store the result in DP table
        dp[curr][rem] = max(pick, notPick) 
        dp[rem][curr] = dp[curr][rem] # Since, f(1, 2) is same as f(2, 1). Because, here's an example: consider n = 5 => 2, 2, 1 == 2, 1, 2 == 1, 2, 2

        return dp[curr][rem]
    
    return solve(1, n)

if __name__ == '__main__':
    testCases = [
        ([1, 6, 8, 9, 10, 19, 7, 20], 8),    # 25
        ([1, 5, 8, 9], 4),                   # 10
        ([5, 5, 8, 9, 10, 17, 17, 20], 8) ,  # 40
        ([42, 68, 35, 1, 70], 5),            # 210
        ([25, 79, 59, 63, 65, 6, 46, 82], 8) # 316
    ]

    for i, inp in enumerate(testCases):
        price, n = inp
        print(f'TestCase {i}: i/p: price={price}, n={n}; o/p: {rodCutting(price, n)}')