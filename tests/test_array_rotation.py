import pytest
from src.array_rotation import rotate_array_left

def test_rotate_array_left_basic():
    """Test basic left rotation"""
    assert rotate_array_left([1, 2, 3, 4, 5], 2) == [3, 4, 5, 1, 2]

def test_rotate_array_left_zero():
    """Test rotation by 0 positions"""
    assert rotate_array_left([1, 2, 3, 4, 5], 0) == [1, 2, 3, 4, 5]

def test_rotate_array_left_full_rotation():
    """Test full rotation (same as original array)"""
    assert rotate_array_left([1, 2, 3, 4, 5], 5) == [1, 2, 3, 4, 5]

def test_rotate_array_left_multiple_rotations():
    """Test rotation more than array length"""
    assert rotate_array_left([1, 2, 3, 4, 5], 7) == [3, 4, 5, 1, 2]

def test_rotate_array_left_empty():
    """Test empty array"""
    assert rotate_array_left([], 3) == []

def test_rotate_array_left_single_element():
    """Test single element array"""
    assert rotate_array_left([42], 1) == [42]

def test_rotate_array_left_invalid_input_type():
    """Test invalid input type"""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_array_left("not a list", 2)

def test_rotate_array_left_invalid_rotation_type():
    """Test invalid rotation type"""
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_array_left([1, 2, 3], "2")

def test_rotate_array_left_negative_rotation():
    """Test negative rotation amount"""
    with pytest.raises(ValueError, match="Rotation amount cannot be negative"):
        rotate_array_left([1, 2, 3], -1)