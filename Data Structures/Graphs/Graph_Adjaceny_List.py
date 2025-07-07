                            # Adjacency list based implementation of graph
from Dependencies.heap import BinaryMinHeap

class Graph_incident_edges:
    class Vertex:
        def __init__(self,e):
           self.incident_edges = [] # List to store all incident edges
           self.value = e # Value to be stored
        
        def __lt__(self, other):
            return self.value < other.value
           
    class Edge:
        def __init__(self,v1: 'Graph_incident_edges.Vertex',v2: 'Graph_incident_edges.Vertex',e: int = 1,directed: bool = False):
            self.v1 = v1 # 1st vertex which the edge is incident on.
            self.v2 = v2 # 2nd vertex which the edge is incident on.
            self.weight = e # Weight of the edge.
            self.isDirected = directed

        def opposite(self, vertex):
            if self.v1 == vertex:
                return self.v2
            return self.v1

        def __lt__(self, other):
            return self.weight < other.weight

    def __init__(self):
        # Adjacency List
        self.Vertices = [] # List to store all the Vertexs in the graph.

    def insertVertex(self, val: int) -> Vertex:
        """
            Inserts a new vertex in graph with value: val.
        """
        v = self.Vertex(val)
        self.Vertices.append(v)
        return v

    
    def insertEdge(self,v1: Vertex,v2: Vertex,w: int = 1, directed: bool = False) -> None:
        """
            Inserts a new edge between vertices v1, v2 with weigth w.
        """
        e = self.Edge(v1,v2,w, directed) # Create a new edge e.
        v1.incident_edges.append(e) # Add e to edge list of v1.
        v2.incident_edges.append(e) # Add e to edge list of v2.
        return e
	
    def removeVertex(self, v: Vertex):
        """
            Removes the specified vertex
        """
        for edge in v.incident_edges:
            adj = edge.opposite(v)
            adj.incident_edges.remove(edge)
        self.Vertices.remove(v)

    def removeEdge(self, edge: Edge):
        """
            Removes the specified edge
        """
        edge.v1.incident_edges.remove(edge)
        edge.v2.incident_edges.remove(edge)

    def degree(self, vertex: Vertex, weighted_degree: bool= False) -> int:
        degree = 0
        if not weighted_degree:
            for edge in vertex.incident_edges:
                if edge.isDirected:
                    if edge.v2 == vertex:
                        degree += 1
                else:
                    degree += 1
        else:
            for edge in vertex.incident_edges:
                if edge.isDirected:
                    if edge.v2 == vertex:
                        degree += edge.weight
                else:
                    degree += edge.weight
        return degree

    def DFS(self,v: Vertex) -> None:
        """
            Performs depth first search on the graph starting at vertex v.
        """
        visited = set() # Set to keep track of all the visited vertices.
        def dfs(v):
            """
                Helper function to perform DFS.
            """
            # If current vertex is unvisited till now print it and add it to the visited set.
            if v not in visited:
                print(v.value)
                visited.add(v)
            
            # Find and add all the unvisited adjacent vertices of the current vertex into adjacent list.
            for edge in v.incident_edges:
                adj = edge.opposite(v)
                if adj not in visited:
                    dfs(adj)

            return
        
        dfs(v)
    
    def dfs_iterative(self, start):
        visited = set()
        stack = [start]

        while stack:
            vertex = stack.pop()
            if vertex not in visited:
                print(vertex.value)
                visited.add(vertex)
                for edge in vertex.incident_edges:
                    adj = edge.opposite(vertex)
                    if adj not in visited:
                        stack.append(adj)

        return visited

    def DFS_SpanningTree(self, vertex: Vertex):
        """
            Perform DFS of the undiscovered portion of Graph g starting at Vertex u.
            
            Discovered is a dictionary mapping each vertex to the edge that was used to
            discover it during the DFS. (u should be ”discovered” prior to the call.)
            Newly discovered vertices will be added to the dictionary as a result.
        """
        discovered = {vertex: None} # A new dictionary, with vertex trivially discovered
        def DFS_helper(vertex):
            if not vertex:
                return
            # Iterate through all outgoing edges from vertex
            for e in vertex.incident_edges:
                v = e.opposite(vertex)
                # If v is an unvisited vertex
                if v not in discovered:
                    discovered[v] = e # e is the tree edge that discovered vertex
                    DFS_helper(v) # Recursively explore from v
        DFS_helper(vertex)
        return discovered
    
    def is_cyclic(self):
        """
            Checks if there is a cycle present in the graph.
        """
        visited = set()

        def helper(v: self.Vertex, parent: self.Vertex):
            visited.add(v)
            
            for edge in v.incident_edges:
                adjacent = edge.opposite(v)

                # If the adjacent vertex is not visited, do DFS on it
                if adjacent not in visited:
                    if helper(adjacent, v):
                        return True
                # If visited and not parent, there is a cycle
                elif adjacent != parent:
                    return True
            
        # Check for cycles in every connected component
        for vertex in self.Vertices:
            if vertex not in visited:
                if helper(vertex, None):
                    return True

        return False

    def BFS(self, v: Vertex) -> None:
        """
            Performs Breadth-First Search (BFS) on the given graph starting from the specified start vertex.

            Args:
                v: Vertex at which BFS starts.
        """

        visited = set() # Set to keep track of visited vertices
        queue = [v] # Queue to store vertices for exploration.

        while queue:
            v = queue.pop(0)

            # If current vertex is unvisited print it, add it to the visited set and add all unvisited adjacent vertices to queue.
            if v not in visited:
                print(v.value)
                visited.add(v)

                # Add all the unvisited adjacent vertices of the current vertex to the queue.
                for edge in v.incident_edges:
                    adj = edge.opposite(v)
                    if adj not in visited:
                        queue.append(adj)
    
    def BFS_(self, s, discovered):
        """
            Perform BFS of the undiscovered portion of Graph g starting at Vertex s.

            discovered is a dictionary mapping each vertex to the edge that was used to
            discover it during the BFS (s should be mapped to None prior to the call).
            Newly discovered vertices will be added to the dictionary as a result.
        """
        levels = [[s]]
        level = [s] # first level includes only s
        discovered[s] = None
        while len(level) > 0:
            next_level = [] # prepare to gather newly found vertices
            for u in level:
                for e in u.incident_edges: # for every outgoing edge from u
                    v = e.opposite(u)
                    if v not in discovered: # v is an unvisited vertex
                        discovered[v] = e # e is the tree edge that discovered v
                        next_level.append(v) # v will be further considered in next pass
            levels.append(next_level)
            level = next_level # relabel ’next’ level to become current

        return levels

    def DFS_directed(self, start: Vertex):
        visited=set()
        result=[]
        
        def recur(v: self.Vertex):
            visited.add(v)
            result.append(v)
            for edge in v.incidence_container:
                if edge.isDirected:
                    if edge.vertex1 == v:
                        opposite = edge.vertex2
                    else:
                        opposite=None
                else: 
                    opposite = edge.opposite(v)
                if opposite != None and opposite not in visited:
                    recur(opposite)
                    
        if start != None and start in self.Vertices:
            recur(start)
        else:
            return "error"
        
        for i in self.Vertices:
            if i not in visited:
                recur(i)
        
        return result
         
    def BFS_directed(self,start):
        if start == None or start not in self.Vertices:
            return "error"
        visited=set()
        visited.add(start)
        result=[]
        q=[start]
        
        while len(q)!=0:
            a = q.pop(0)
            result.append(a)
            for edge in a.incidence_edges:
                if edge.isDirected:
                    if edge.vertex1 == a :
                        opposite = i.vertex2
                    else:
                        opposite = None
                else:      
                    opposite = edge.opposite(a)
                if opposite not in visited and opposite!=None:
                    q.append(opposite)
                    visited.add(opposite)
                    
        return result

    def MST_Prims(self) -> list[Edge]:
        """
            Compute a minimum spanning tree of weighted graph g.

            Return a list of edges that comprise the MST (in arbitrary order).
        """
        d = {}  # d[v] is bound on distance to tree
        tree = []  # list of edges in spanning tree
        visited = set()  # to track visited vertices
        heap = BinaryMinHeap()  # Custom BinaryMinHeap for efficient edge selection

        # Initialize distances and choose an arbitrary starting vertex (root)
        for v in self.Vertices:
            if not d:
                d[v] = 0  # make the first vertex the root (distance 0)
            else:
                d[v] = float('inf')  # all other vertices are at "infinite" distance

        # Initialize the heap with the starting vertex (root)
        heap.insert((0, self.Vertices[0], None))  # (distance, vertex, edge)

        while heap.sz > 0:
            # Extract the minimum edge from the heap
            dist, u, edge = heap.delMin()

            # Skip if vertex has already been processed
            if u in visited:
                continue

            visited.add(u)

            if edge is not None:
                tree.append(edge)  # add edge to tree if it exists

            # Update distances for neighbors of the newly added vertex
            for edge in u.incident_edges:  # for each incident edge (u, v)
                v = edge.opposite(u)
                if v not in visited:  # if v is not yet in the tree
                    wgt = edge.weight  # weight of edge (u, v)
                    if wgt < d[v]:  # a better edge to v?
                        d[v] = wgt  # update distance
                        heap.insert((d[v], v, edge))  # update heap with new distance and edge

        return tree

    def MST_Kruskal(self) -> list[Edge]:
        """
        Compute a minimum spanning tree of a graph using Kruskal's algorithm.
        Uses sets to track components instead of UnionFind.
        
        Returns:
            list: A list of edges that comprise the MST.
        """
        tree = []  # List to store MST edges
        edge_pq = BinaryMinHeap()  # List to store all edges
        # Initialize each vertex as its own component
        components = [{v} for v in self.Vertices]
        
        # Collect all edges into a priority queue
        seen_edges = set()  # To avoid duplicate edges in undirected graph
        for vertex in self.Vertices:
            for edge in vertex.incident_edges:
                # Only add each undirected edge once
                if (edge.v1, edge.v2) not in seen_edges and (edge.v2, edge.v1) not in seen_edges:
                    edge_pq.insert((edge.weight, edge))
                    seen_edges.add((edge.v1, edge.v2))

        # Process edges in order of increasing weight
        while len(tree) < len(self.Vertices) - 1 and edge_pq.sz > 0:
            weight, edge = edge_pq.delMin()
            u, v = edge.v1, edge.v2
            
            # Find components containing u and v
            u_component = None
            v_component = None
            for component in components:
                if u in component:
                    u_component = component
                if v in component:
                    v_component = component
                if u_component and v_component:
                    break
            
            # If vertices are in different components, add edge to MST
            if u_component != v_component:
                tree.append(edge)
                # Merge components
                new_component = u_component.union(v_component)
                components.remove(u_component)
                components.remove(v_component)
                components.append(new_component)
        
        return tree

    def MST_Boruvkas(self):
        """
            Compute a minimum spanning tree using a simplified version of Boruvka's algorithm.
            Returns:
                list: A list of edges that comprise the MST.
        """
        if not self.Vertices:
            return []

        # Initialize: each vertex in its own component
        components = [{v} for v in self.Vertices]
        mst_edges = []
        
        while len(components) > 1:
            # Find cheapest outgoing edge for each component
            cheapest = []  # List of (component_index, edge) tuples
            
            for i, component in enumerate(components):
                min_edge = None
                min_weight = float('inf')
                
                # Check all edges from this component
                for vertex in component:
                    for edge in vertex.incident_edges:
                        other = edge.opposite(vertex)
                        # Skip if edge stays within component
                        if other in component:
                            continue
                            
                        if edge.weight < min_weight:
                            min_weight = edge.weight
                            min_edge = edge
                
                if min_edge:
                    cheapest.append((i, min_edge))
            
            if not cheapest:
                break
                
            # Merge components connected by cheapest edges
            used = set()  # Track which components have been merged
            new_components = []
            
            for comp_idx, edge in cheapest:
                # Skip if this component was already merged
                if comp_idx in used:
                    continue
                    
                # Find the other component this edge connects to
                other_comp_idx = None
                for i, comp in enumerate(components):
                    if (i != comp_idx and (edge.v1 in comp or edge.v2 in comp)):
                        other_comp_idx = i
                        break
                
                # If we found both components and neither is used
                if (other_comp_idx is not None and other_comp_idx not in used):
                    # Merge components
                    new_comp = components[comp_idx].union(components[other_comp_idx])
                    new_components.append(new_comp)
                    used.add(comp_idx)
                    used.add(other_comp_idx)
                    mst_edges.append(edge)
            
            # Keep unmerged components
            for i, comp in enumerate(components):
                if i not in used:
                    new_components.append(comp)
            
            # Update for next iteration
            components = new_components

        return mst_edges


    def dijkstrasAlgo(self, src: Vertex):
        """
            Compute shortest-path distances from src to reachable vertices of the graph.
            
            Graph can be undirected or directed, but must be weighted.
            Returns dictionary mapping each reachable vertex to its distance from src.
        """
        dist = {}              
        prev = {}
        pq = BinaryMinHeap()   # vertex v will have key dist[v]

        # For each vertex v of the graph, add an entry to the priority queue
        # with the source having distance 0 and all others having infinite distance
        for v in self.Vertices:
            if v == src:
                dist[v] = 0
                pq.insert((dist[v], v))
            else:
                dist[v] = float('inf')
            prev[v] = None            

        while pq.sz > 0:
            # Remove vertex with minimum distance
            key, u = pq.delMin()

            # For each edge from u to v
            for e in u.incident_edges:
                v = e.opposite(u)
                wgt = e.weight
                if dist[u] + wgt < dist[v]:    # better path to v?
                    dist[v] = dist[u] + wgt    # update the distance
                    prev[v] = u
                    # Add new entry with updated distance
                    pq.insert((dist[v], v))

        return dist    # only includes reachable vertices

    def construct_path(self, u: Vertex, v: Vertex, discovered: dict):
        if discovered is None:
            discovered = self.DFS_SpanningTree(u)
        path = []
        if v in discovered:
            # we build list from v to u and then reverse it at the end
            path.append(v)
            walk = v
            while walk is not u:
                e = discovered[walk] # find edge leading to walk
                parent = e.opposite(walk)
                path.append(parent)
                walk = parent
            path.reverse() # reorient path from u to v
        return path
    
    def isConnected(self) -> bool:
        return len(self.DFS_SpanningTree(self.Vertices[0])) == len(self.Vertices)


    def find_connected_components(self):
        """
        Finds all connected components in the graph using DFS_SpanningTree.
        
        Returns:
            list: List of dictionaries, where each dictionary contains the vertices in one connected component
        """
        components = []  # List to store all components
        visited = set()  # Set to keep track of visited vertices
        
        for vertex in self.Vertices:
            if vertex not in visited:
                # Get the spanning tree starting from this vertex
                tree = self.DFS_SpanningTree(vertex)
                # Add all vertices in this tree to visited set
                visited.update(tree.keys())
                # Add this component to our list of components
                components.append(tree)
        
        return components

    def topological_sort(self) -> list[Vertex]:
        """
            Return a list of vertices of directed acyclic graph g in topological order.
            If graph g has a cycle, the result will be incomplete.
        """
        topo = []  # a list of vertices placed in topological order
        ready = []  # list of vertices that have no remaining constraints
        incount = {}  # keep track of in-degree for each vertex

        # Calculate in-degree for each vertex
        for u in self.Vertices:
            incount[u] = 0  # initialize in-degree count

        for u in self.Vertices:
            for edge in u.incident_edges:
                if edge.isDirected and edge.v1 == u:  # only consider outgoing edges
                    incount[edge.v2] += 1  # increment in-degree of destination vertex

        # Collect all vertices with no incoming edges
        for u in self.Vertices:
            if incount[u] == 0:
                ready.append(u)

        # Process vertices
        while len(ready) > 0:
            u = ready.pop(0)  # u is free of constraints
            topo.append(u)  # add u to the topological order
            for edge in u.incident_edges:
                if edge.isDirected and edge.v1 == u:  # only consider outgoing edges
                    v = edge.v2
                    incount[v] -= 1  # v has one less constraint without u
                    if incount[v] == 0:
                        ready.append(v)

        # Check if a topological sort is possible (i.e., no cycles)
        if len(topo) != len(self.Vertices):
            print("Graph has at least one cycle")

        return topo


    def bellman_ford(self, source: 'Graph_incident_edges.Vertex'):
        """
            Implements the Bellman-Ford algorithm to find shortest paths from a source vertex
            to all other vertices, even in the presence of negative edge weights.
            
            Args:
                source: Starting vertex for pathfinding
                
            Returns:
                tuple: (distances, predecessors) where
                    - distances is a dict mapping each vertex to its shortest distance from source
                    - predecessors is a dict mapping each vertex to its predecessor in shortest path
                    
            Raises:
                ValueError: If the graph contains a negative-weight cycle
        """
        # Step 1: Initialize distances and predecessors
        distances = {}
        predecessors = {}
        for vertex in self.Vertices:
            if vertex == source:
                distances[vertex] = 0
            else:
                distances[vertex] = float('inf')
            predecessors[vertex] = None
            
        # # Step 2: Relax edges |V|-1 times
        # for _ in range(len(self.Vertices) - 1):
        # For each vertex, examine all its incident edges
        for _ in range(len(self.Vertices) - 1):
            for vertex in self.Vertices:
                for edge in vertex.incident_edges:
                    u = vertex  # current vertex
                    v = edge.opposite(u)  # adjacent vertex
                    w = edge.weight  # edge weight
                    
                    # Relaxation step
                    if distances[u] != float('inf') and distances[u] + w < distances[v]:
                        distances[v] = distances[u] + w
                        predecessors[v] = u
                        
        # Step 3: Check for negative-weight cycles
        for vertex in self.Vertices:
            for edge in vertex.incident_edges:
                u = vertex
                v = edge.opposite(u)
                w = edge.weight
                
                if distances[u] != float('inf') and distances[u] + w < distances[v]:
                    print("Graph contains a negative-weight cycle")
                    
        return distances, predecessors

if __name__ == '__main__':
    graph = Graph_incident_edges()
    
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
    #     (1,6,14,False),(1,2,7,False),(1,3,9,False),
    #     (2,3,10,False),(2,4,15,False),
    #     (3,4,11,False),(3,6,2,False),
    #     (4,5,6,False),
    #     (5,6,9,False)
    # ]
    '''For DFS'''
    # edges = [
    #     (0,1,1,False),(0,3,1,False),
    #     (1,2,1,False),
    #     (2,4,1,False),(2,5,1,False),
    #     (4,5,1,False),(4,6,1,False),(4,7,1,False),
    #     (6,10,1,False),
    #     (7,8,1,False),(7,10,1,False),
    #     (8,10,1,False),
    #     (9,10,1,False)
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
    # edges = [
    #     (1,2,4,True), (1,4,5,True),
    #     (2,4,5,True),
    #     (3,2,-10,True),
    #     (4,3,3,True)
    # ]
    # Add all edges to the graph
    for v1, v2, w, d in edges:
        graph.insertEdge(vertices[v1], vertices[v2], w, d)
    '''----------------------------------------------------------------------------------------------------------------'''
    '''DFS'''
    # graph.DFS(graph.Vertices[0])
    
    '''Iterative DFS'''
    # graph.dfs_iterative(graph.Vertices[0])
    
    '''DFS Spanning Tree'''
    # discovered = graph.DFS_SpanningTree(vertices[0])
    # for v in discovered:
    #     if discovered[v]:
    #         print(f'{discovered[v].v1.value} -> {discovered[v].v2.value}')
    
    '''BFS'''
    # graph.BFS(graph.Vertices[0])

    '''BFS Spanning Tree'''
    # discovered = {}
    # for level in graph.BFS_(graph.Vertices[0], discovered):
    #     for vertex in level:
    #         print(vertex.value, end="-")
    #     print("------------------------")
    # for vertex in discovered:
    #     print(vertex.value, end=" - ")

    '''Topological Sort'''
    # print([v.value for v in graph.topological_sort()])

    '''Prim's algorithm'''
    # mst = graph.MST_Prims()
    # for edge in mst:
    #     print(edge.v1.value,'->',edge.v2.value)

    '''Kruskal's algorithm'''
    # mst = graph.MST_Kruskal()
    # for edge in mst:
    #     print(edge.v1.value,'->',edge.v2.value)

    '''Boruvka's algorithm'''
    mst = graph.MST_Boruvkas()
    for edge in mst:
        print(edge.v1.value,'->',edge.v2.value)

    '''Dijkstra's Algorithm'''
    # distances = graph.dijkstrasAlgo(vertices[1])
    # for v in distances:
    #     print(v.value,':',distances[v])

    '''Bellman-Ford Algorithm'''
    # distances, _ = graph.bellman_ford(vertices[1])
    # for v in distances:
    #     print(v.value,':',distances[v])