# Link: https://www.geeksforgeeks.org/problems/connected-components-in-an-undirected-graph/1

"""
    @question:
        Given an undirected graph with V vertices numbered from 0 to V-1 and E edges, represented as a 2D array edges[][], where each entry edges[i] = [u, v] denotes an edge between vertices u and v.

        Your task is to return a list of all connected components. Each connected component should be represented as a list of its vertices, with all components returned in a collection where each component is listed separately.

        Note: You can return the components in any order, driver code will print the components in sorted order.
    ---------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------
        Examples :
            Input: V = 5, edges[][] = [[0, 1], [2, 1], [3, 4]]
            Output: [[0, 1, 2], [3, 4]]
        ---------------------------------------------------------------------------------
            Input: V = 7, edges[][] = [[0, 1], [6, 0], [2, 4], [2, 3], [3, 4]]
            Output: [[0, 1, 6], [2, 3, 4], [5]]
    ---------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------
        Constraints:
            1 ≤ V, E ≤ 105
            0 ≤ edges[i][0], edges[i][1] < V
"""
from typing import List

def getComponents(V: int, edges: List[List[int]]):
    components = []
    adj_list = [[] for _ in range(V)]
    for a, b in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)
    
    visited = set()
    for i in range(V):
        if i not in visited:
            stack = [i]
            visited.add(i)
            comp = []
            while stack:
                node = stack.pop()
                comp.append(node)
                for j in adj_list[node]:
                    if j not in visited:
                        stack.append(j)
                        visited.add(j)
            components.append(comp)
    
    return components

if __name__ == '__main__':
    testCases = [
        [5, [[0, 1], [2, 1], [3, 4]]],
        [7, [[0, 1], [6, 0], [2, 4], [2, 3], [3, 4]]]
    ]

    for i, (V, edges) in enumerate(testCases):
        print(f"TestCase {i}: i/p: V={V}, edges={edges}; o/p: components={getComponents(V, edges)}")