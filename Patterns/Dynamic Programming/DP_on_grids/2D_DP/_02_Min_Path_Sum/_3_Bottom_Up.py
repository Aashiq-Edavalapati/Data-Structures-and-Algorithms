from typing import List

def minPathSum(grid: List[List[int]]):
    m, n = len(grid), len(grid[0])
    dp = [[-1 for _ in range(n)] for _ in range(m)]
    dp[0][0] = grid[0][0]
    for row in range(m):
        for col in range(n):
            if row == 0 and col == 0: continue

            up, left = float('inf'), float('inf')
            if row > 0: up = dp[row - 1][col] + grid[row][col]
            if col > 0: left = dp[row][col - 1] + grid[row][col]

            dp[row][col] = min(up, left)
    
    return dp[m - 1][n - 1]

if __name__ == '__main__':
    testCases = [
        [[1,3,1],[1,5,1],[4,2,1]],  # 7
        [[1,2,3],[4,5,6]],          # 12
    ]

    for i, grid in enumerate(testCases):
        print(f'TestCase {i}: i/p: grid = {grid} o/p: {minPathSum(grid)}')