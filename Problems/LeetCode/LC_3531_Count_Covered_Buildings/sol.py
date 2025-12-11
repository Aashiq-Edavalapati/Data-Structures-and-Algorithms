# Link: https://leetcode.com/problems/count-covered-buildings/

"""
    @question:
        You are given a positive integer n, representing an n x n city. You are also given a 2D grid buildings, where buildings[i] = [x, y] denotes a unique building located at coordinates [x, y].

        A building is covered if there is at least one building in all four directions: left, right, above, and below.

        Return the number of covered buildings.

    ------------------------------------------------------------------------------
    ------------------------------------------------------------------------------

        Example 1:
            Input: n = 3, buildings = [[1,2],[2,2],[3,2],[2,1],[2,3]]
            Output: 1
            Explanation:
                Only building [2,2] is covered as it has at least one building:
                above ([1,2])
                below ([3,2])
                left ([2,1])
                right ([2,3])
                Thus, the count of covered buildings is 1.
        
        ------------------------------------------------------------------------------
                
        Example 2:
            Input: n = 3, buildings = [[1,1],[1,2],[2,1],[2,2]]
            Output: 0
            Explanation: No building has at least one building in all four directions.

        ------------------------------------------------------------------------------

        Example 3:
            Input: n = 5, buildings = [[1,3],[3,2],[3,3],[3,5],[5,3]]
            Output: 1
            Explanation:
                Only building [3,3] is covered as it has at least one building:
                above ([1,3])
                below ([5,3])
                left ([3,2])
                right ([3,5])
                Thus, the count of covered buildings is 1.
        
    ------------------------------------------------------------------------------
    ------------------------------------------------------------------------------

        Constraints:
            2 <= n <= 105
            1 <= buildings.length <= 105 
            buildings[i] = [x, y]
            1 <= x, y <= n
            All coordinates of buildings are unique.
"""
from typing import List
from collections import defaultdict

def countCoveredBuildings(n: int, buildings: List[List[int]]) -> int:
    """
        :param n: Size of grid (n x n)
        :type n: int
        :param buildings: Coords where building is present
        :type buildings: List[List[int]]
        :return: count of covered buildings
        :rtype: int
        :TC: O(M*log(M)); where M is no. of buildings
        :SC: O(M)
    """
    # O(M) — build row/column maps
    xs = defaultdict(list)
    ys = defaultdict(list)

    for x, y in buildings:  # O(M)
        xs[y].append(x)
        ys[x].append(y)

    leftExists  = set()
    rightExists = set()
    upExists    = set()
    downExists  = set()

    # Process rows
    for y, xList in xs.items():
        xList.sort()  # O(M log M) total across all row-lists

        for i in range(1, len(xList) - 1):  # O(M) total across all rows
            x = xList[i]
            leftExists.add((x, y))
            rightExists.add((x, y))

    # Process columns
    for x, yList in ys.items():
        yList.sort()  # O(M log M) total across all column-lists

        for i in range(1, len(yList) - 1):  # O(M) total across all columns
            y = yList[i]
            upExists.add((x, y))
            downExists.add((x, y))

    # Count valid buildings
    cnt = 0
    for x, y in buildings:  # O(M)
        if (x, y) in leftExists and (x, y) in rightExists and (x, y) in upExists and (x, y) in downExists:
            cnt += 1

    return cnt  # Overall time complexity: O(M log M)


# The below solution gave MLE
def mle(n: int, buildings: List[List[int]]) -> int:
    # O(M) time, O(M) space — build row/column maps
    xs = defaultdict(list)
    ys = defaultdict(list)

    for x, y in buildings:  # O(M)
        xs[y].append(x)
        ys[x].append(y)

    # O(N^2) space — four (n+1) × (n+1) grids
    up    = [[False for _ in range(n + 1)] for _ in range(n + 1)]    # O(N^2)
    down  = [[False for _ in range(n + 1)] for _ in range(n + 1)]    # O(N^2)
    left  = [[False for _ in range(n + 1)] for _ in range(n + 1)]    # O(N^2)
    right = [[False for _ in range(n + 1)] for _ in range(n + 1)]    # O(N^2)

    # Process rows
    for y, xList in xs.items():
        xList.sort()  # O(M log M) total across all rows

        for i in range(1, len(xList) - 1):  # O(M) total
            left[y][xList[i]] = True

        for i in range(len(xList) - 2, 0, -1):  # O(M) total
            right[y][xList[i]] = True

    # Process columns
    for x, yList in ys.items():
        yList.sort()  # O(M log M) total across all columns

        for i in range(1, len(yList) - 1):  # O(M) total
            up[x][yList[i]] = True

        for i in range(len(yList) - 2, 0, -1):  # O(M) total
            down[x][yList[i]] = True

    # Count valid buildings
    cnt = 0
    for x, y in buildings:  # O(M)
        if up[x][y] and down[x][y] and left[y][x] and right[y][x]:
            cnt += 1

    return cnt  # Overall time: O(N^2 + M log M), space: O(N^2)

if __name__ == '__main__':
    testCases = [
        (3, [[1,2],[2,2],[3,2],[2,1],[2,3]]), # 1
        (3, [[1,1],[1,2],[2,1],[2,2]]), # 0
        (5, [[1,3],[3,2],[3,3],[3,5],[5,3]]), # 1
        (5, [[1,2],[2,2],[3,2],[2,1],[2,3],[3,1],[3,3],[3,4],[4,2],[4,3]]), # 3
    ]

    for i, testCase in enumerate(testCases):
        n, buildings = testCase
        print(f"TestCase {i}:- i/p: n={n}, buildings={buildings}; o/p: {countCoveredBuildings(n, buildings)}")