# Link: https://leetcode.com/problems/number-of-islands/

"""
    @question:
        Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

        An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

    -----------------------------------------------------------------------------
    -----------------------------------------------------------------------------

        Example 1:
            Input: grid = [
            ["1","1","1","1","0"],
            ["1","1","0","1","0"],
            ["1","1","0","0","0"],
            ["0","0","0","0","0"]
            ]
            Output: 1

        -----------------------------------------------------------------------------

        Example 2:
            Input: grid = [
            ["1","1","0","0","0"],
            ["1","1","0","0","0"],
            ["0","0","1","0","0"],
            ["0","0","0","1","1"]
            ]
            Output: 3

    -----------------------------------------------------------------------------
    -----------------------------------------------------------------------------

        Constraints:
            m == grid.length
            n == grid[i].length
            1 <= m, n <= 300
            grid[i][j] is '0' or '1'.
"""
from typing import List

def numIslands(grid: List[List[str]]) -> int:
    m, n = len(grid), len(grid[0])
    visited = [[False for _ in range(n)] for _ in range(m)]
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    islands = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j] == '0' or visited[i][j]: continue
            stack = [(i, j)]
            visited[i][j] = True
            while stack:
                x, y = stack.pop()
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] == '1' and not visited[nx][ny]:
                        stack.append((nx, ny))
                        visited[nx][ny] = True
            islands += 1

    return islands

if __name__ == '__main__':
    testCases = [
        [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]],
        [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]
    ]

    for i, grid in enumerate(testCases):
        print(f"TestCase {i}:-\n\ti/p: grid={grid};\n\to/p: {numIslands(grid)}")