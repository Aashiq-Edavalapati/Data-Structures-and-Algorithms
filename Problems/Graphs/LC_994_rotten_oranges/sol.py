# Link: https://leetcode.com/problems/rotting-oranges/

"""
    @question:
        You are given an m x n grid where each cell can have one of three values:

            0 representing an empty cell,
            1 representing a fresh orange, or
            2 representing a rotten orange.

        Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

        Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

    ---------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------

        Example 1:
            Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
            Output: 4
        ---------------------------------------------------------------------------------
        Example 2:
            Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
            Output: -1
            Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
        ---------------------------------------------------------------------------------
        Example 3:
            Input: grid = [[0,2]]
            Output: 0
            Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

    ---------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------

        Constraints:
            m == grid.length
            n == grid[i].length
            1 <= m, n <= 10
            grid[i][j] is 0, 1, or 2.
"""
from typing import List

def orangesRotting(grid: List[List[int]]) -> int:
    m, n = len(grid), len(grid[0])
    fresh = 0
    minutes = 0
    q = []
    for i in range(m):
        for j in range(n):
            if grid[i][j] == 1: fresh += 1
            elif grid[i][j] == 2: q.append((i, j))
    
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

    while q:
        sz = len(q)
        isRot = False
        for i in range(sz):
            x, y = q.pop(0)
            for j in range(4):
                dx, dy = x + dxs[j], y + dys[j]
                if 0 <= dx < m and 0 <= dy < n and grid[dx][dy] == 1:
                    isRot = True
                    grid[dx][dy] = 2
                    fresh -= 1
                    q.append((dx, dy))
        if isRot: minutes += 1

    return minutes if fresh == 0 else -1

if __name__ == '__main__':
    testCases = [
        [[2,1,1],[1,1,0],[0,1,1]],
        [[2,1,1],[0,1,1],[1,0,1]],
        [[0,2]]
    ]

    for i, testCase in enumerate(testCases):
        print(f"TestCase {i}: i/p: grid={testCase}; o/p: {orangesRotting(testCase)}")