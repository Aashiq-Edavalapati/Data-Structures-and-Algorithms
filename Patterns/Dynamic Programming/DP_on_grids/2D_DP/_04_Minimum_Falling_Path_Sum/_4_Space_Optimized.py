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
    prevRow = matrix[0]
    for row in range(1, m):
        temp = prevRow[:]
        for idx in range(n):
            if idx < 0 or idx >= n: continue
            
            left, up, right = maxVal, maxVal, maxVal
            if idx > 0:
                left = prevRow[idx - 1] + matrix[row][idx]
            up = prevRow[idx] + matrix[row][idx]
            if idx < n - 1:
                right = prevRow[idx + 1] + matrix[row][idx]

            temp[idx] = min(left, up, right)
        prevRow = temp
    
    return min(prevRow)

if __name__ == '__main__':
    testCases = [
        [[2,1,3],[6,5,4],[7,8,9]],      # 13
        [[-19,57],[-40,-5]],            # -59
    ]

    for i, matrix in enumerate(testCases):
        print(f'TestCase {i}: i/p: matrix = {matrix}; o/p: {minFallingPathSum(matrix)}')