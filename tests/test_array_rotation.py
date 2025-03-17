import pytest
from src.array_rotation import rotate_array_right

def test_basic_rotation():
    """Test basic right rotation of an array"""
    assert rotate_array_right([1, 2, 3, 4, 5], 2) == [4, 5, 1, 2, 3]

def test_rotation_zero():
    """Test rotation by zero positions"""
    assert rotate_array_right([1, 2, 3], 0) == [1, 2, 3]

def test_rotation_full_array_length():
    """Test rotation by full array length"""
    assert rotate_array_right([1, 2, 3, 4], 4) == [1, 2, 3, 4]

def test_rotation_more_than_array_length():
    """Test rotation by more than array length"""
    assert rotate_array_right([1, 2, 3], 5) == [2, 3, 1]

def test_empty_array():
    """Test rotation of an empty array"""
    assert rotate_array_right([], 3) == []

def test_single_element_array():
    """Test rotation of a single-element array"""
    assert rotate_array_right([1], 10) == [1]

def test_negative_rotation_raises_error():
    """Test that negative rotation raises a ValueError"""
    with pytest.raises(ValueError, match="Rotation amount cannot be negative"):
        rotate_array_right([1, 2, 3], -1)

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        rotate_array_right("not a list", 2)

def test_non_integer_rotation_raises_error():
    """Test that non-integer rotation amount raises a TypeError"""
    with pytest.raises(TypeError, match="Rotation amount must be an integer"):
        rotate_array_right([1, 2, 3], "2")