# Link: https://leetcode.com/problems/minimum-falling-path-sum/
from typing import List
"""
    @question:
        Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

        A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).
"""

def minFallingPathSum(matrix: List[List[int]]) -> int:
    m, n = len(matrix), len(matrix[0])
    maxVal = 10 ** 9
    dp = [[float('inf') for _ in range(n)] for _ in range(m)]
    dp[0] = matrix[0]
    for row in range(1, m):
        for idx in range(n):
            if idx < 0 or idx >= n: continue
            
            left, up, right = maxVal, maxVal, maxVal
            if idx > 0:
                left = dp[row - 1][idx - 1] + matrix[row][idx]
            up = dp[row - 1][idx] + matrix[row][idx]
            if idx < n - 1:
                right = dp[row - 1][idx + 1] + matrix[row][idx]

            dp[row][idx] = min(left, up, right)
    
    return min(dp[-1])

if __name__ == '__main__':
    testCases = [
        [[2,1,3],[6,5,4],[7,8,9]],      # 13
        [[-19,57],[-40,-5]],            # -59
    ]

    for i, matrix in enumerate(testCases):
        print(f'TestCase {i}: i/p: matrix = {matrix}; o/p: {minFallingPathSum(matrix)}')