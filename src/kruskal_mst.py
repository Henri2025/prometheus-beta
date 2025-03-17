class DisjointSet:
    """
    A Disjoint Set data structure for tracking connected components 
    and performing union-find operations efficiently.
    """
    def __init__(self, vertices):
        """
        Initialize the Disjoint Set with each vertex in its own set.
        
        :param vertices: Number of vertices in the graph
        """
        self.parent = list(range(vertices))
        self.rank = [0] * vertices

    def find(self, item):
        """
        Find the root/representative of a set with path compression.
        
        :param item: Vertex to find the set for
        :return: Root/representative of the set
        """
        if self.parent[item] != item:
            # Path compression: make every node on the path point directly to the root
            self.parent[item] = self.find(self.parent[item])
        return self.parent[item]

    def union(self, x, y):
        """
        Union two sets by rank to keep the tree balanced.
        
        :param x: First vertex
        :param y: Second vertex
        :return: Whether the union was successful (not already in same set)
        """
        # Find roots of both sets
        root_x = self.find(x)
        root_y = self.find(y)

        # If roots are same, they're already in the same set
        if root_x == root_y:
            return False

        # Union by rank to keep tree balanced
        if self.rank[root_x] < self.rank[root_y]:
            root_x, root_y = root_y, root_x

        self.parent[root_y] = root_x
        
        # Update rank if needed
        if self.rank[root_x] == self.rank[root_y]:
            self.rank[root_x] += 1

        return True

def kruskal_mst(graph):
    """
    Find the Minimum Spanning Tree using Kruskal's Algorithm.
    
    :param graph: List of edges, where each edge is (weight, u, v)
    :return: List of edges in the Minimum Spanning Tree
    :raises ValueError: If graph is empty or invalid
    """
    # Validate input
    if not graph:
        raise ValueError("Graph is empty")

    # Ensure graph contains valid edges
    for edge in graph:
        if len(edge) != 3:
            raise ValueError("Invalid edge format. Expected (weight, u, v)")

    # Sort edges by weight in ascending order
    sorted_edges = sorted(graph, key=lambda x: x[0])

    # Find max vertex to determine number of vertices
    max_vertex = max(max(edge[1], edge[2]) for edge in graph)
    vertices = max_vertex + 1

    # Initialize Disjoint Set
    disjoint_set = DisjointSet(vertices)
    
    # MST will store the selected edges
    mst = []

    # Process each edge
    for weight, u, v in sorted_edges:
        # If adding this edge doesn't create a cycle
        if disjoint_set.union(u, v):
            mst.append((weight, u, v))

    return mst