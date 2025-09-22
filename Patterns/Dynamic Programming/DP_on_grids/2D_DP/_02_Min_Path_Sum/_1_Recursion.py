from typing import List

def minPathSum(grid: List[List[int]]):
    m, n = len(grid), len(grid[0])
    def minPathSumFinder(row: int, col: int):
        if row < 0 or col < 0: return -1
        if row == 0 and col == 0: return grid[0][0]
        
        leftRec = minPathSumFinder(row, col - 1)
        left = float('inf')
        if leftRec != -1: left = grid[row][col] + leftRec
        upRec = minPathSumFinder(row - 1, col)
        up = float('inf')
        if upRec != -1: up = grid[row][col] + upRec

        return min(left, up)
    
    return minPathSumFinder(m - 1, n - 1)

if __name__ == '__main__':
    testCases = [
        [[1,3,1],[1,5,1],[4,2,1]],  # 7
        [[1,2,3],[4,5,6]],          # 12
    ]

    for i, grid in enumerate(testCases):
        print(f'TestCase {i}: i/p: grid = {grid} o/p: {minPathSum(grid)}')