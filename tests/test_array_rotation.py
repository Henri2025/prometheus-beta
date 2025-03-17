import pytest
from src.array_rotation import rotate_array_left

def test_basic_rotation():
    """Test basic left rotation of an array"""
    assert rotate_array_left([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]

def test_rotation_zero():
    """Test rotation by zero positions"""
    assert rotate_array_left([1, 2, 3], 0) == [1, 2, 3]

def test_full_rotation():
    """Test rotation by full array length"""
    assert rotate_array_left([1, 2, 3], 3) == [1, 2, 3]

def test_rotation_larger_than_length():
    """Test rotation larger than array length"""
    assert rotate_array_left([1, 2, 3], 4) == [2, 3, 1]

def test_empty_array():
    """Test rotation of an empty array"""
    assert rotate_array_left([], 2) == []

def test_single_element_array():
    """Test rotation of a single-element array"""
    assert rotate_array_left([42], 1) == [42]

def test_invalid_input_types():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_array_left("not a list", 2)
    
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_array_left([1, 2, 3], "2")

def test_negative_rotation():
    """Test error handling for negative rotation"""
    with pytest.raises(ValueError, match="Rotation amount cannot be negative"):
        rotate_array_left([1, 2, 3], -1)