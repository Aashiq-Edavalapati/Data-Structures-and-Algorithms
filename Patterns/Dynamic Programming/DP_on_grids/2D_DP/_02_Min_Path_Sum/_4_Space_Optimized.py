from typing import List

def minPathSum(grid: List[List[int]]):
    m, n = len(grid), len(grid[0])
    prevCol = grid[0][0]
    prevRow = [float('inf')] * n
    prevRow[0] = grid[0][0]
    for row in range(m):
        for col in range(n):
            if row == 0 and col == 0: continue

            up, left = float('inf'), float('inf')
            if row > 0: up = prevRow[col] + grid[row][col]
            if col > 0: left = prevCol + grid[row][col]

            prevCol = min(up, left)
            prevRow[col] = prevCol
    
    return prevCol

if __name__ == '__main__':
    testCases = [
        [[1,3,1],[1,5,1],[4,2,1]],  # 7
        [[1,2,3],[4,5,6]],          # 12
    ]

    for i, grid in enumerate(testCases):
        print(f'TestCase {i}: i/p: grid = {grid} o/p: {minPathSum(grid)}')