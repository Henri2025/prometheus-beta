import pytest
from src.depth_first_search import depth_first_search

def test_basic_dfs():
    """Test basic DFS traversal on a simple graph."""
    graph = {
        'A': ['B', 'C'],
        'B': ['D', 'E'],
        'C': ['F'],
        'D': [],
        'E': ['F'],
        'F': []
    }
    
    result = depth_first_search(graph, 'A')
    assert result == ['A', 'B', 'D', 'E', 'F', 'C']

def test_dfs_with_visit_func():
    """Test DFS with a visit function."""
    visited_nodes = []
    
    def visit_func(node):
        visited_nodes.append(node)
    
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['E'],
        'D': [],
        'E': []
    }
    
    depth_first_search(graph, 'A', visit_func=visit_func)
    assert visited_nodes == ['A', 'B', 'D', 'C', 'E']

def test_dfs_single_node_graph():
    """Test DFS on a graph with a single node."""
    graph = {'A': []}
    
    result = depth_first_search(graph, 'A')
    assert result == ['A']

def test_dfs_raises_error_for_missing_start_node():
    """Test that an error is raised if start node is not in graph."""
    graph = {'A': ['B'], 'B': []}
    
    with pytest.raises(ValueError, match="Start node X not found in graph"):
        depth_first_search(graph, 'X')

def test_dfs_raises_error_for_invalid_graph():
    """Test that an error is raised for invalid graph type."""
    with pytest.raises(TypeError, match="Graph must be a dictionary"):
        depth_first_search([], 'A')

def test_dfs_disconnected_components():
    """Test DFS on a graph with disconnected components."""
    graph = {
        'A': ['B'],
        'B': ['A'],
        'C': ['D'],
        'D': ['C'],
        'E': []
    }
    
    result = depth_first_search(graph, 'A')
    assert result == ['A', 'B']

def test_dfs_cyclic_graph():
    """Test DFS on a graph with cycles."""
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A'],
        'D': ['B']
    }
    
    result = depth_first_search(graph, 'A')
    assert result == ['A', 'B', 'D', 'C']