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
    prev = [0 for _ in range(n + 1)] # Initialize prev row
    for curr in range(n, 0, -1):
        cur = [0 for _ in range(n + 1)]
        for rem in range(curr, n + 1):
            pick = price[curr - 1] + cur[rem - curr] # dp[curr][rem - curr] => cur[rem - curr]
            notPick = 0
            if curr < n:
                notPick = prev[rem] # dp[curr + 1][rem] => prev[rem]

            # Store the result in cur row
            cur[rem] = max(pick, notPick)
        prev = cur # Update cur row as prev row
        
    return prev[n]

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