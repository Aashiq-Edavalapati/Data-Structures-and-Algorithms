# Link: https://leetcode.com/problems/surrounded-regions/

"""
    @question:
        You are given an m x n matrix board containing letters 'X' and 'O', capture regions that are surrounded:

            Connect: A cell is connected to adjacent cells horizontally or vertically.
            Region: To form a region connect every 'O' cell.
            Surround: A region is surrounded if none of the 'O' cells in that region are on the edge of the board. Such regions are completely enclosed by 'X' cells.

        To capture a surrounded region, replace all 'O's with 'X's in-place within the original board. You do not need to return anything.

    ---------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------

        Example 1:
            Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
            Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
            Explanation:
                In the above diagram, the bottom region is not captured because it is on the edge of the board and cannot be surrounded.

        ---------------------------------------------------------------------------------
                
        Example 2:
            Input: board = [["X"]]
            Output: [["X"]]

    ---------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------

        Constraints:
            m == board.length
            n == board[i].length
            1 <= m, n <= 200
            board[i][j] is 'X' or 'O'.
"""
from typing import List

class Solution:
    def __init__(self):
        self.directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    def dfs(self, startX: int, startY: int, board: List[List[str]], visited: List[List[bool]], m: int, n: int) -> None:
        visited[startX][startY] = True
        stack = [(startX, startY)]
        while stack:
            x, y = stack.pop()
            for dx, dy in self.directions:
                nx, ny = x + dx, y + dy
                if 0 <= nx < m and 0 <= ny < n and board[nx][ny] == 'O' and not visited[nx][ny]:
                    stack.append((nx, ny))
                    visited[nx][ny] = True

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        visited = [[False for _ in range(n)] for _ in range(m)]
        for i in range(m):
            # first col
            if board[i][0] == 'O' and not visited[i][0]:
                self.dfs(i, 0, board, visited, m, n)

            # last col
            if board[i][-1] == 'O' and not visited[i][-1]:
                self.dfs(i, n - 1, board, visited, m, n)
        
        for i in range(n):
            # first row
            if board[0][i] =='O' and not visited[0][i]:
                self.dfs(0, i, board, visited, m, n)
            
            # last row
            if board[-1][i] == 'O' and not visited[-1][i]:
                self.dfs(m - 1, i, board, visited, m, n)
        
        for i in range(1, m - 1):
            for j in range(1, n - 1):
                if board[i][j] == 'O' and not visited[i][j]:
                    board[i][j] = 'X'

if __name__ == '__main__':
    testCases = [
        [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]],
        [["X"]],
        [["O","O","X","X"],["O","X","X","X"],["X","X","O","X"],["X","O","X","X"]],
        [["O","O","O","O"],["O","X","X","X"],["X","X","O","X"],["X","O","O","X"]],
        [["X","O"],["O","X"]]
    ]

    sol = Solution()

    for i, board in enumerate(testCases):
        print(f"TestCase {i}:\n\ti/p: board={board}")
        sol.solve(board)
        print(f"\to/p: board={board}")