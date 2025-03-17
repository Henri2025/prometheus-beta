import pytest
from src.kruskal_mst import kruskal_mst, DisjointSet

def test_disjoint_set_initialization():
    """Test DisjointSet initialization."""
    ds = DisjointSet(5)
    assert ds.parent == [0, 1, 2, 3, 4]
    assert ds.rank == [0, 0, 0, 0, 0]

def test_disjoint_set_find():
    """Test find operation in DisjointSet."""
    ds = DisjointSet(5)
    ds.parent[1] = 2
    ds.parent[2] = 3
    ds.parent[3] = 4
    
    assert ds.find(1) == 4
    # Path compression should have updated parent
    assert ds.parent[1] == 4
    assert ds.parent[2] == 4

def test_disjoint_set_union():
    """Test union operation in DisjointSet."""
    ds = DisjointSet(5)
    
    # First union should succeed
    assert ds.union(0, 1) == True
    assert ds.find(0) == ds.find(1)
    
    # Union of same set should fail
    assert ds.union(0, 1) == False

def test_kruskal_mst_simple_graph():
    """Test Kruskal's algorithm on a simple graph."""
    # Graph with 4 vertices and 5 edges
    graph = [
        (1, 0, 1),   # weight 1, between vertex 0 and 1
        (4, 0, 2),   # weight 4, between vertex 0 and 2
        (2, 1, 2),   # weight 2, between vertex 1 and 2
        (3, 1, 3),   # weight 3, between vertex 1 and 3
        (5, 2, 3)    # weight 5, between vertex 2 and 3
    ]
    
    mst = kruskal_mst(graph)
    
    # Expected MST edges (sorted by weight)
    expected_mst = [
        (1, 0, 1),   # First edge
        (2, 1, 2),   # Second edge
        (3, 1, 3)    # Third edge
    ]
    
    # Compare MST, ignoring order
    assert sorted(mst) == sorted(expected_mst)
    assert len(mst) == 3  # Number of edges in MST should be (vertices - 1)

def test_kruskal_mst_empty_graph():
    """Test Kruskal's algorithm with an empty graph."""
    with pytest.raises(ValueError, match="Graph is empty"):
        kruskal_mst([])

def test_kruskal_mst_invalid_edge():
    """Test Kruskal's algorithm with invalid edge format."""
    invalid_graph = [
        (1, 0),      # Invalid edge (missing third element)
        (4, 0, 2)    # Valid edge
    ]
    
    with pytest.raises(ValueError, match="Invalid edge format"):
        kruskal_mst(invalid_graph)

def test_kruskal_mst_disconnected_graph():
    """Test Kruskal's algorithm on a disconnected graph."""
    graph = [
        (1, 0, 1),   # Component 1
        (2, 2, 3),   # Component 2
        (5, 4, 5)    # Another component
    ]
    
    mst = kruskal_mst(graph)
    
    # Each component will have its minimal edges
    assert len(mst) == len(graph) - 1

def test_kruskal_mst_large_graph():
    """Test Kruskal's algorithm on a larger, more complex graph."""
    graph = [
        (2, 0, 1),   # lowest
        (3, 1, 2),
        (1, 0, 2),   # another low weight edge
        (4, 1, 3),
        (5, 2, 3),
        (6, 0, 3)    # highest weight
    ]
    
    mst = kruskal_mst(graph)
    
    # Expected result focuses on minimum weight edges
    expected_weights = {2, 1, 4}  # Total minimum weight
    mst_weights = {edge[0] for edge in mst}
    
    assert mst_weights == expected_weights
    assert len(mst) == 3  # Number of edges in MST