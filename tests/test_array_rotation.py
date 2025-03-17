import pytest
from src.array_rotation import rotate_array_right

def test_basic_rotation():
    """Test basic right rotation"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_right(arr, 2) == [4, 5, 1, 2, 3]

def test_full_rotation():
    """Test full rotation (same as original array)"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_right(arr, 5) == arr

def test_zero_rotation():
    """Test zero rotation returns a copy of the original array"""
    arr = [1, 2, 3, 4, 5]
    rotated = rotate_array_right(arr, 0)
    assert rotated == arr
    assert rotated is not arr  # Ensure it's a new list

def test_large_rotation():
    """Test rotation larger than array length"""
    arr = [1, 2, 3, 4, 5]
    assert rotate_array_right(arr, 7) == [4, 5, 1, 2, 3]

def test_empty_array():
    """Test rotation of empty array"""
    assert rotate_array_right([], 3) == []

def test_single_element_array():
    """Test rotation of single-element array"""
    arr = [42]
    assert rotate_array_right(arr, 1) == [42]

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_array_right("not a list", 2)
    
    with pytest.raises(TypeError, match="Rotation positions must be an integer"):
        rotate_array_right([1, 2, 3], "2")

def test_negative_rotation():
    """Test error handling for negative rotation"""
    with pytest.raises(ValueError, match="Rotation positions cannot be negative"):
        rotate_array_right([1, 2, 3], -1)