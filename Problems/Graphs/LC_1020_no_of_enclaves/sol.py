# Link: https://leetcode.com/problems/number-of-enclaves/

"""
    @question:
        You are given an m x n binary matrix grid, where 0 represents a sea cell and 1 represents a land cell.

        A move consists of walking from one land cell to another adjacent (4-directionally) land cell or walking off the boundary of the grid.

        Return the number of land cells in grid for which we cannot walk off the boundary of the grid in any number of moves.

    ---------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------        

        Example 1:
            Input: grid = [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]]
            Output: 3
            Explanation: There are three 1s that are enclosed by 0s, and one 1 that is not enclosed because its on the boundary.

        ---------------------------------------------------------------------------------
            
        Example 2:
            Input: grid = [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
            Output: 0
            Explanation: All 1s are either on the boundary or can reach the boundary.

    ---------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------

        Constraints:
            m == grid.length
            n == grid[i].length
            1 <= m, n <= 500
            grid[i][j] is either 0 or 1.
"""
from typing import List

class Solution:
    def __init__(self):
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def isValidEnclave(self, startX: int, startY: int, grid: List[List[int]], visited: List[List[int]], m: int, n: int) -> bool:
        stack = [(startX, startY)]
        visited[startX][startY] = True
        isValid = True
        cnt = 1
        while stack:
            x, y = stack.pop()
            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == 1 and not visited[nx][ny]:
                    if nx == 0 or nx == m - 1 or ny == 0 or ny == n - 1: isValid = False
                    stack.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1
        
        return cnt if isValid else -1

    def numEnclaves(self, grid: List[List[int]]) -> int:
        enclaves = 0
        m, n = len(grid), len(grid[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if grid[i][j] == 1 and not visited[i][j]:
                    cnt = self.isValidEnclave(i, j, grid, visited, m, n)
                    if cnt != -1: enclaves += cnt

        return enclaves
    
if __name__ == '__main__':
    testCases = [
        [[0,0,0,0],[1,0,1,0],[0,1,1,0],[0,0,0,0]],
        [[0,1,1,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]]
    ]

    sol = Solution()

    for i, grid in enumerate(testCases):
        print(f"TestCase {i}:\n\ti/p: grid={grid}\n\to/p: {sol.numEnclaves(grid)}")