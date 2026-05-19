# Link: https://leetcode.com/problems/01-matrix/

"""
    @question:
        Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.

        The distance between two cells sharing a common edge is 1.

    ---------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------

        Example 1:
            Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
            Output: [[0,0,0],[0,1,0],[0,0,0]]

        ---------------------------------------------------------------------------------
            
        Example 2:
            Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
            Output: [[0,0,0],[0,1,0],[1,2,1]]

        ---------------------------------------------------------------------------------

        Example 3:
            Input: mat = 
                [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]
            Output: 
                [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,2,1,1,0,1],[2,1,1,1,1,2,1,0,1,0],[3,2,2,1,0,1,0,0,1,1]]
        
    ---------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------

        Constraints:
            m == mat.length
            n == mat[i].length
            1 <= m, n <= 104
            1 <= m * n <= 104
            mat[i][j] is either 0 or 1.
            There is at least one 0 in mat.
"""
from typing import List
from collections import deque

def updateMatrix(mat: List[List[int]]) -> List[List[int]]:
    """
        @topic: multi-source BFS
        @intuition:
            
    """
    m, n = len(mat), len(mat[0])
    q = deque()
    for i in range(m):
        for j in range(n):
            if mat[i][j] == 0: q.append((i, j))
            else: mat[i][j] = float('inf')
    
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    while q:
        x, y = q.popleft()

        for dx, dy in directions:
            neighborX, neighborY = x + dx, y + dy
            if 0 <= neighborX < m and 0 <= neighborY < n and mat[neighborX][neighborY] > mat[x][y] + 1:
                mat[neighborX][neighborY] = mat[x][y] + 1
                q.append((neighborX, neighborY))

    return mat

if __name__ == '__main__':
    testCases = [
        [[0,0,0],[0,1,0],[0,0,0]],
        [[0,0,0],[0,1,0],[1,1,1]],
        [[1,0,1,1,0,0,1,0,0,1],[0,1,1,0,1,0,1,0,1,1],[0,0,1,0,1,0,0,1,0,0],[1,0,1,0,1,1,1,1,1,1],[0,1,0,1,1,0,0,0,0,1],[0,0,1,0,1,1,1,0,1,0],[0,1,0,1,0,1,0,0,1,1],[1,0,0,0,1,1,1,1,0,1],[1,1,1,1,1,1,1,0,1,0],[1,1,1,1,0,1,0,0,1,1]]
    ]

    for i, mat in enumerate(testCases):
        print(f"TestCase {i}: \n\ti/p: mat={mat};\n\to/p: {updateMatrix(mat)}")