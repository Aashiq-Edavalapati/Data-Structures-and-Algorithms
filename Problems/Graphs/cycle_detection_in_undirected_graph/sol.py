# Link: https://www.geeksforgeeks.org/problems/detect-cycle-in-an-undirected-graph/1

"""
    @question:
        Given an undirected graph with V vertices and E edges, represented as a 2D vector edges[][], where each entry edges[i] = [u, v] denotes an edge between vertices u and v, determine whether the graph contains a cycle or not.

        Note: The graph can have multiple component.

    ---------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------
        
        Examples:
            Input: V = 4, E = 4, edges[][] = [[0, 1], [0, 2], [1, 2], [2, 3]]
            Output: true
            Explanation: 
                1 -> 2 -> 0 -> 1 is a cycle.

            ---------------------------------------------------------------------------------
                
            Input: V = 4, E = 3, edges[][] = [[0, 1], [1, 2], [2, 3]]
            Output: false
            Explanation: 
                No cycle in the graph.

    ---------------------------------------------------------------------------------
    ---------------------------------------------------------------------------------
                
        Constraints:
            1 ≤ V, E ≤ 105
            0 ≤ edges[i][0], edges[i][1] < V
"""
from typing import List

def isCycle(V: int, edges: List[List[int]]) -> bool:
    adj_list = [[] for _ in range(V)]
    
    for a, b in edges:
        adj_list[a].append(b)
        adj_list[b].append(a)
        
    visited = set()
    for i in range(V):
        if i in visited: continue
        
        stack = [(i, -1)] # (vertex, parent)
        visited.add(i)
        while stack:
            vertex, parent = stack.pop()
            for neighbor in adj_list[vertex]:
                if neighbor not in visited:
                    stack.append((neighbor, vertex))
                    visited.add(neighbor)
                elif neighbor != parent: return True
            
        if len(visited) == V: return False
    
    return False

if __name__ == '__main__':
    testCases = [
        [4, [[0, 1], [0, 2], [1, 2], [2, 3]]],
        [4, [[0, 1], [1, 2], [2, 3]]]
    ]

    for i, (V, edges) in enumerate(testCases):
        print(f"TestCase {i}: i/p: V={V}, edges={edges}; \n\to/p: {"Cycle exists" if isCycle(V, edges) else "Cycle doesn't exist"}")