import pytest
from src.second_largest import find_second_largest

def test_basic_array():
    """Test finding second largest in a basic array."""
    assert find_second_largest([1, 2, 3, 4, 5]) == 4

def test_array_with_duplicates():
    """Test finding second largest in an array with duplicates."""
    assert find_second_largest([5, 5, 3, 3, 2, 1]) == 3

def test_negative_numbers():
    """Test finding second largest with negative numbers."""
    assert find_second_largest([-1, -2, -3, -4, -5]) == -2

def test_mixed_numbers():
    """Test finding second largest with mixed positive and negative numbers."""
    assert find_second_largest([-10, 5, 0, 3, 5]) == 3

def test_two_element_array():
    """Test finding second largest in a two-element array."""
    assert find_second_largest([1, 2]) == 1

def test_error_single_element():
    """Test that an error is raised for a single-element array."""
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([1])

def test_error_empty_array():
    """Test that an error is raised for an empty array."""
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([])

def test_error_all_same_elements():
    """Test that an error is raised when all elements are the same."""
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([2, 2, 2, 2])