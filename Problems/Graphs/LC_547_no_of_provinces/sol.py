# Link: https://leetcode.com/problems/number-of-provinces/

"""
    @question:
        There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.

        A province is a group of directly or indirectly connected cities and no other cities outside of the group.

        You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.

        Return the total number of provinces.

    ---------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------
        Example 1:
            Input: isConnected = [[1,1,0],[1,1,0],[0,0,1]]
            Output: 2
        ---------------------------------------------------------------------------------
        Example 2:
            Input: isConnected = [[1,0,0],[0,1,0],[0,0,1]]
            Output: 3

    ---------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------
        Constraints:
            1 <= n <= 200
            n == isConnected.length
            n == isConnected[i].length
            isConnected[i][j] is 1 or 0.
            isConnected[i][i] == 1
            isConnected[i][j] == isConnected[j][i]

"""
from typing import List

def findCircleNum(isConnected: List[List[int]]) -> int:
    n = len(isConnected)
    visited = set()
    provinces = 0
    for i in range(n):
        if i not in visited:
            stack = [i]
            while stack:
                node = stack.pop()
                visited.add(node)
                for j in range(n):
                    if isConnected[node][j] == 1 and j not in visited:
                        stack.append(j)
                        visited.add(j)
            
            provinces += 1
    
    return provinces

if __name__ == '__main__':
    testCases = [
        [[1,1,0],[1,1,0],[0,0,1]],
        [[1,0,0],[0,1,0],[0,0,1]]
    ]

    for i, testCase in enumerate(testCases):
        op = findCircleNum(testCase)
        print(f"Testcase {i}: i/p: isConnected={testCase}; o/p: Provinces={op}")