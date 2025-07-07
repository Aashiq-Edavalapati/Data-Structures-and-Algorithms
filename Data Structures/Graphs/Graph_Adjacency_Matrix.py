from collections import defaultdict, deque

class Graph:
    def __init__(self, num_vertices, edges=None):
        self.num_vertices = num_vertices

        # Initialize adjacency matrix
        self.adj_matrix = [[0] * num_vertices for i in range(num_vertices)]
        if edges:
            for u, v in edges:
                self.adj_matrix[u][v] = 1

    def bfs_matrix(self, start):
        visited = [False] * self.num_vertices
        queue = [start]
        traversal = []

        while queue:
            node = queue.pop(0)
            if not visited[node]:
                visited[node] = True
                traversal.append(node)
                for neighbor in range(self.num_vertices):
                    if self.adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
                        queue.append(neighbor)
        return traversal

    def dfs_matrix(self, start):
        visited = [False] * self.num_vertices
        stack = [start]
        traversal = []

        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                traversal.append(node)
                for neighbor in range(self.num_vertices - 1, -1, -1):
                    if self.adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
                        stack.append(neighbor)
        return traversal

    def topological_sort_matrix(self):
        visited = [False] * self.num_vertices
        stack = []

        def dfs(node):
            visited[node] = True
            for neighbor in range(self.num_vertices):
                if self.adj_matrix[node][neighbor] == 1 and not visited[neighbor]:
                    dfs(neighbor)
            stack.append(node)

        for node in range(self.num_vertices):
            if not visited[node]:
                dfs(node)
        return stack[::-1]


# Example Usage
if __name__ == "__main__":
    edges = [(0, 1), (0, 2), (1, 3), (2, 3), (2, 4)]

    # Adjacency Matrix
    print("Adjacency Matrix Representation:")
    graph_matrix = Graph(5, edges)
    print("BFS:", graph_matrix.bfs_matrix(0))
    print("DFS:", graph_matrix.dfs_matrix(0))
    print("Topological Sort:", graph_matrix.topological_sort_matrix())