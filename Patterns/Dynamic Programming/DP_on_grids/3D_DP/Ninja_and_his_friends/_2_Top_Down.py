from typing import List
"""
    @question:
        Ninja has a grid of size R x C, where each cell contains some chocolates. He has two friends: Alice and Bob, and wants to collect as many chocolates as possible using their help.

        Alice starts at the top-left cell (0, 0)
        Bob starts at the top-right cell (0, C - 1)
        Both can only move to the next row, and from position (i, j), they can move to:
        (i + 1, j)
        (i + 1, j - 1)
        (i + 1, j + 1)

        Both must remain within the grid bounds.
        Each collects all chocolates in their current cell.
        If both land on the same cell, the chocolates are only counted once.

        Return the maximum number of chocolates Ninja can collect using his two friends.
------------------------------------------------------------------------------------------------------
        Examples:
            Input: grid = [[2, 3, 1, 2],[3, 4, 2, 2],[5, 6, 3, 5]]
            Output: 21
            Explanation: 
                Alice: (0,0) → (1,1) → (2,1) → chocolates = 2 + 4 + 6 = 12
                Bob:  (0,3) → (1,3) → (2,3) → chocolates = 2 + 2 + 5 = 9
                Total = 12 + 9 = 21
        -----------------------------------------------------------------------------------------------

            Input: grid = [[1, 2],[3, 4]]
            Output: 10
            Explanation:

                Alice: (0,0) → (1,0) → 1 + 3 = 4
                Bob:  (0,1) → (1,1) → 2 + 4 = 6
                But both can't pick at same time (if they land same cell), so:
                Best is (0,0)+(1,0)+(0,1)+(1,1) - overlap = 1+3+2+4 = 10

"""

def maxCandies(grid: List[List[int]]) -> int:
    n, m = len(grid), len(grid[0])
    minVal = -(10 ** 9 + 7)
    dp = [[[minVal for _ in range(m)] for _ in range(m)] for _ in range(n)]
    def helper(i: int, j1: int, j2: int) -> int:
        if j1 < 0 or j1 >= m or j2 < 0 or j2 >= m:
            return minVal
        if i == n - 1:
            if j1 != j2:
                dp[i][j1][j2] = grid[i][j1] + grid[i][j2]
            else:
                dp[i][j1][j2] = grid[i][j1]
            return dp[i][j1][j2]

        if dp[i][j1][j2] > minVal: return dp[i][j1][j2]

        maxRes = 0
        for d1 in range(-1, 2):
            for d2 in range(-1, 2):
                if j1 == j2:
                    rec = grid[i][j1] + helper(i + 1, j1 + d1, j2 + d2)
                else:
                    rec = grid[i][j1] + grid[i][j2] + helper(i + 1, j1 + d1, j2 + d2)
                maxRes = max(maxRes, rec)
        
        dp[i][j1][j2] = maxRes
        return maxRes
    
    return helper(0, 0, m - 1)
    
if __name__ == '__main__':
    testCases = [
        [[2, 3, 1, 2],[3, 4, 2, 2],[5, 6, 3, 5]],        # 21
        [[1, 2],[3, 4]],                                 # 10
    ]

    for i, grid in enumerate(testCases):
        print(f'Testcase {i}: i/p: grid={grid};  o/p: {maxCandies(grid)}')