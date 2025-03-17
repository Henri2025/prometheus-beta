import pytest
from src.find_second_largest import find_second_largest

def test_find_second_largest_normal_case():
    """Test finding second largest in a typical array."""
    assert find_second_largest([1, 2, 3, 4, 5]) == 4
    assert find_second_largest([5, 3, 1, 4, 2]) == 4

def test_find_second_largest_with_duplicates():
    """Test finding second largest with duplicate values."""
    assert find_second_largest([1, 1, 2, 2, 3, 3, 4, 4, 5]) == 4
    assert find_second_largest([5, 5, 4, 4, 3, 3, 2, 2, 1]) == 4

def test_find_second_largest_negative_numbers():
    """Test finding second largest with negative numbers."""
    assert find_second_largest([-1, -2, -3, -4, -5]) == -2
    assert find_second_largest([-5, -3, -1, -4, -2]) == -2

def test_find_second_largest_mixed_numbers():
    """Test finding second largest with mixed positive and negative numbers."""
    assert find_second_largest([-10, 5, 0, 3, 8]) == 5
    assert find_second_largest([0, -5, 10, 3, -2]) == 3

def test_find_second_largest_error_cases():
    """Test error cases for invalid inputs."""
    # Empty array
    with pytest.raises(ValueError, match="Input array cannot be empty"):
        find_second_largest([])
    
    # Array with only one unique element
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([1, 1, 1, 1])
    with pytest.raises(ValueError, match="Array must contain at least 2 unique elements"):
        find_second_largest([5])