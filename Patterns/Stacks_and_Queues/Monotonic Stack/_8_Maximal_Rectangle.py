# Link: https://leetcode.com/problems/maximal-rectangle/

"""
    @question(LC 85):
        Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

    ---------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------        

        Example 1:
            Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
            Output: 6
            Explanation: The maximal rectangle is shown in the above picture.

        ---------------------------------------------------------------------------------

        Example 2:
            Input: matrix = [["0"]]
            Output: 0

        ---------------------------------------------------------------------------------

        Example 3:
            Input: matrix = [["1"]]
            Output: 1
        
        ---------------------------------------------------------------------------------
        ---------------------------------------------------------------------------------

        Constraints:
            rows == matrix.length
            cols == matrix[i].length
            1 <= rows, cols <= 200
            matrix[i][j] is '0' or '1'.
"""
from typing import List

def maximalRectangle(matrix: List[List[int]]) -> int:
    n, m = len(matrix), len(matrix[0])
    for i in range(n):
        for j in range(m):
            matrix[i][j] = int(matrix[i][j])
    heightMat = [[0 for _ in range(m)] for _ in range(n)]
    for j in range(m):
        heightMat[0][j] = matrix[0][j]
        for i in range(1, n):
            if matrix[i][j] == 0:
                continue
            heightMat[i][j] = heightMat[i - 1][j] + matrix[i][j]

    ans = 0
    for i in range(n):
        stk = []
        heights = heightMat[i]
        maxArea = 0
        for i, height in enumerate(heights):
            while stk and heights[stk[-1]] > height:
                idx = stk.pop()
                w = i - (stk[-1] if stk else -1) - 1
                maxArea = max(maxArea, w * heights[idx])
            stk.append(i)
        
        while stk:
            idx = stk.pop()
            w = m - (stk[-1] if stk else -1) - 1
            maxArea = max(maxArea, w * heights[idx])
        ans = max(ans, maxArea)
    
    return ans


if __name__ == '__main__':
    testCases = [
        [["1","0","1","0","0"],
         ["1","0","1","1","1"],
         ["1","1","1","1","1"],
         ["1","0","0","1","0"]], # 6
        
        [["0"]], # 0,

        [["1"]], # 1

        [["0","1"],["1","0"]], # 1
    ]

    for i, matrix in enumerate(testCases):
        print(f"TestCase {i}:- i/p: matrix={matrix}; o/p: {maximalRectangle(matrix)}")