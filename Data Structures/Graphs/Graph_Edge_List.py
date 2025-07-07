from Dependencies.heap import BinaryMinHeap

class Vertex:
    def __init__(self, element):
        """Initialize a vertex with its element."""
        self._element = element
        self._position = None  # Position in the list V (if needed for removal)

    def element(self):
        """Return the element stored in this vertex."""
        return self._element

    def __lt__(self,other):
        return self._element < other._element

class Edge:
    def __init__(self, vertex_u, vertex_v, weight, isDirected):
        """Initialize an edge between vertex_u and vertex_v with element."""
        self._endpoints = (vertex_u, vertex_v)  # Tuple of endpoint vertices
        self._position = None  # Position in the list E (if needed for removal)
        self._weight = weight
        self._isDirected = isDirected

    def element(self):
        """Return the element stored in this edge."""
        return self._element

    def endpoints(self):
        """Return the endpoints (u, v) of this edge."""
        return self._endpoints

    def opposite(self, vertex):
        """Return the vertex opposite to the given vertex."""
        if vertex == self._endpoints[0]:
            return self._endpoints[1]
        elif vertex == self._endpoints[1]:
            return self._endpoints[0]
        else:
            raise ValueError("Vertex not incident to edge")

    def __lt__(self,other):
        return self._weight < other._weight

class Graph_Edge_List:
    def __init__(self):
        """Initialize an empty graph."""
        self._vertices: list[Vertex] = []  # List of vertex objects
        self._edges: list[Edge] = []     # List of edge objects

    def insertVertex(self, element):
        """Insert and return a new vertex storing element."""
        v = Vertex(element)
        v._position = len(self._vertices)  # Position in the vertex list
        self._vertices.append(v)
        return v

    def insertEdge(self, u, v, weight = 1, isDirected = False):
        """Insert and return a new edge from u to v storing element."""
        e = Edge(u, v,weight,isDirected)
        e._position = len(self._edges)  # Position in the edge list
        self._edges.append(e)
        return e

    def vertices(self):
        """Return a list of all vertices."""
        return self._vertices

    def edges(self):
        """Return a list of all edges."""
        return self._edges

    def remove_vertex(self, vertex):
        """Remove a vertex and all its incident edges."""
        self._vertices.remove(vertex)
        self._edges = [e for e in self._edges if vertex not in e.endpoints()]

    def remove_edge(self, edge):
        """Remove an edge."""
        self._edges.remove(edge)

    def DFS(self, start_vertex: Vertex) -> None:
        """
        Perform Depth First Search (DFS) starting from the given vertex.

        Args:
            start_vertex (Vertex): The starting vertex for the DFS.
        """
        visited = set()  # Set to track visited vertices

        def dfs(v):
            """
            Helper function to perform recursive DFS.
            """
            if v not in visited:
                # Mark the vertex as visited and print its element
                print(v.element())
                visited.add(v)

                # Find all unvisited adjacent vertices
                adjacent = []
                for edge in self._edges:
                    # Check if the current vertex is an endpoint of the edge
                    if v in edge.endpoints():
                        # Get the opposite vertex
                        adj = edge.opposite(v)
                        if adj not in visited:
                            adjacent.append(adj)

                # Recursively visit all adjacent vertices
                for vertex in adjacent:
                    dfs(vertex)

        # Start the DFS from the given start vertex
        dfs(start_vertex)

    def DFS_SpanningTree(self, start_vertex: Vertex) -> dict:
        """
        Perform Depth First Search (DFS) to compute a spanning tree starting from the given vertex.

        Args:
            start_vertex (Vertex): The starting vertex for the DFS.

        Returns:
            dict: A dictionary mapping each visited vertex (other than the start vertex)
                to the edge used to discover it.
        """
        discovered = {start_vertex: None}  # Dictionary to store the spanning tree

        def helper(v):
            """
            Recursive helper function to explore the graph.
            """
            for edge in self._edges:
                # Check if the current vertex is an endpoint of the edge
                if v in edge.endpoints():
                    adj = edge.opposite(v)
                    # If the adjacent vertex is not discovered, add it to the tree
                    if adj not in discovered:
                        discovered[adj] = edge  # Mark edge as the discovery edge
                        helper(adj)  # Recursively visit the adjacent vertex

        # Start DFS from the starting vertex
        helper(start_vertex)
        return discovered

    def is_cyclic(self):
        """
            Checks if there is a cycle present in the graph.
        """
        visited = set()

        def helper(v: Vertex, parent: Vertex):
            visited.add(v)
            
            for edge in self._edges:
                if v in edge.endpoints():
                    adjacent = edge.opposite(v)

                    # If the adjacent vertex is not visited, do DFS on it
                    if adjacent not in visited:
                        if helper(adjacent, v):
                            return True
                    # If visited and not parent, there is a cycle
                    elif adjacent != parent:
                        return True
            
        # Check for cycles in every connected component
        for vertex in self._vertices:
            if vertex not in visited:
                if helper(vertex, None):
                    return True

        return False

    def MST_Prims(self):
        d = {}
        tree = []
        visited = set()
        pq = BinaryMinHeap()

        for v in self._vertices:
            if not d:
                d[v] = 0
            else:
                d[v] = float('inf')
        
        pq.insert((0,self._vertices[0],None))

        while pq.sz > 0:
            dist, u, edge = pq.delMin()

            if u in visited:
                continue
                
            visited.add(u)

            if edge is not None:
                tree.append(edge)

            for edge in self._edges:
                if u in edge.endpoints():
                    adj = edge.opposite(u)

                    if adj not in visited:
                        wgt = edge._weight
                        if wgt < d[adj]:
                            d[adj] = wgt
                            pq.insert((d[adj], adj, edge))
            
        return tree

    def MST_Kruskals(self):
        tree = []
        pq = BinaryMinHeap()
        components = [{v} for v in self._vertices]
        
        seen_edges = set()
        for edge in self._edges:
            u, v = edge.endpoints()
            if (u, v) not in seen_edges and (v, u) not in seen_edges:
                pq.insert((edge._weight, edge))
                seen_edges.add((u, v))

        while len(tree) < len(self._vertices) - 1 and pq.sz > 0:
            weight, edge = pq.delMin()
            u, v = edge.endpoints()

            u_component = None
            v_component = None
            for component in components:
                if u in component:
                    u_component = component
                if v in component:
                    v_component = component
                if u_component and v_component:
                    break
            
            if u_component != v_component:
                tree.append(edge)
                new_component = u_component.union(v_component)
                components.remove(u_component)
                components.remove(v_component)
                components.append(new_component)
                        
        return tree
    
    def MST_Boruvkas(self):
        if not self._vertices:
            return []
        
        components = [{v} for v in self._vertices]
        mst_edges = []

        while len(components) > 1:
            cheapest = []

            for i, component in enumerate(components):
                min_edge = None
                min_weight = float('inf')

                for vertex in component:
                    for edge in self._edges:
                        if vertex in edge.endpoints():
                            other = edge.opposite(vertex)

                            if other in component:
                                continue

                            if edge._weight < min_weight:
                                min_weight = edge._weight
                                min_edge = edge
                    
                if min_edge:
                    cheapest.append((i, min_edge))
                
            used = set()
            new_components = []

            for comp_idx, edge in cheapest:
                if comp_idx in used:
                    continue
                
                other_comp_idx = None
                for i, comp in enumerate(components):
                    if(i != comp_idx and (edge.endpoints()[0] in comp or edge.endpoints()[1] in comp)):
                        other_comp_idx = i
                        break
                
                if other_comp_idx is not None and other_comp_idx not in used and comp_idx not in used:
                    new_component = components[comp_idx].union(components[other_comp_idx])
                    new_components.append(new_component)
                    used.add(comp_idx)
                    used.add(other_comp_idx)
                    mst_edges.append(edge)
            for i, comp in enumerate(components):
                if i not in used:
                    new_components.append(comp)

            components = new_components
        return mst_edges

# Example Usage:
if __name__ == "__main__":
    graph = Graph_Edge_List()
    
    # Insert vertices
    vertices = {}
    for i in range(1,8):
        vertices[i] = graph.insertVertex(i)
    
    # Insert edges
    # Each edge is inserted only once since the graph is undirected
    '''For prim's algorithm'''
    # edges = [
    #     (1,2,1,False),(1,4,3,False),
    #     (2,4,2,False),(2,5,6,False),(2,6,5,False),(2,3,3,False),
    #     (3,5,4,False),(3,6,4,False),
    #     (4,5,3,False),
    #     (5,6,2,False)
    # ]           
    '''For Boruvka's algorithm'''
    edges = [
        (1,2,7,False),(1,4,4,False),
        (2,4,9,False),(2,3,11,False),(2,5,10,False),
        (3,5,5,False),
        (4,5,15,False),(4,6,6,False),
        (5,6,12,False),(5,7,8,False),
        (6,7,13,False)
    ]
    '''Dijkstra's algorithm'''
    # edges = [
    #     (1,6,14),(1,2,7),(1,3,9),
    #     (2,3,10),(2,4,15),
    #     (3,4,11),(3,6,2),
    #     (4,5,6),
    #     (5,6,9)
    # ]
    '''For DFS'''
    # edges = [
    #     (0,1,1),(0,3,1),
    #     (1,2,1),
    #     (2,4,1),(2,5,1),
    #     (4,5,1),(4,6,1),(4,7,1),
    #     (6,10,1),
    #     (7,8,1),(7,10,1),
    #     (8,10,1),
    #     (9,10,1)
    # ]
    '''For BFS'''
    # edges = [
    #     (1,2,1),(1,5,1),(1,6,1),
    #     (2,6,1),(2,3,1),
    #     (3,7,1),(3,4,1),
    #     (4,7,1),(4,8,1),
    #     (5,6,1),(5,9,1),
    #     (6,7,1),(6,9,1),
    #     (7,10,1),(7,11,1),(7,12,1),
    #     (8,12,1),
    #     (9,10,1),(9,13,1),(9,14,1),
    #     (10,11,1),
    #     (11,14,1),(11,15,1),
    #     (12,16,1),
    #     (13,14,1)
    # ]
    '''For topological sort'''
    # edges = [
    #     (1,4,1,True),(1,2,1,True),(1,3,1,True),
    #     (2,4,1,True),(2,5,1,True),
    #     (4,5,1,True),(4,3,1,True)
    # ]
    
    # Add all edges to the graph
    for v1, v2, w, d in edges:
        graph.insertEdge(vertices[v1], vertices[v2], w, d)
    '''-----------------------------------------------------------------------------------------------------------'''
    '''Prim's Algorithm'''
    # mst: list[Edge] = graph.MST_Prims()
    # for edge in mst:
    #     print(edge.endpoints()[0]._element,'->',edge.endpoints()[1]._element)

    '''Kruskal's Algorithm'''
    # mst = graph.MST_Kruskals()
    # for edge in mst:
    #     print(edge.endpoints()[0]._element,'->',edge.endpoints()[1]._element)

    '''Boruvka's Algorithm'''
    mst = graph.MST_Boruvkas()
    for edge in mst:
        print(edge.endpoints()[0]._element,'->',edge.endpoints()[1]._element)