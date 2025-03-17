import pytest
from src.longest_increasing_subsequence import find_longest_increasing_subsequence

def test_basic_increasing_sequence():
    """Test a basic increasing sequence"""
    arr = [10, 22, 9, 33, 21, 50, 41, 60, 80]
    result = find_longest_increasing_subsequence(arr)
    assert len(result) == 6
    assert all(result[i] < result[i+1] for i in range(len(result)-1))

def test_all_same_elements():
    """Test when all elements are the same"""
    arr = [7, 7, 7, 7, 7]
    assert find_longest_increasing_subsequence(arr) == [7]

def test_already_sorted_ascending():
    """Test an already sorted ascending array"""
    arr = [1, 2, 3, 4, 5]
    assert find_longest_increasing_subsequence(arr) == [1, 2, 3, 4, 5]

def test_already_sorted_descending():
    """Test a descending array"""
    arr = [5, 4, 3, 2, 1]
    assert find_longest_increasing_subsequence(arr) == [5]

def test_single_element():
    """Test a single element array"""
    arr = [42]
    assert find_longest_increasing_subsequence(arr) == [42]

def test_empty_list_raises_error():
    """Test that an empty list raises a ValueError"""
    with pytest.raises(ValueError, match="Input list cannot be empty"):
        find_longest_increasing_subsequence([])

def test_non_list_input_raises_error():
    """Test that non-list input raises a TypeError"""
    with pytest.raises(TypeError, match="Input must be a list"):
        find_longest_increasing_subsequence("not a list")

def test_complex_subsequence():
    """Test a more complex subsequence selection"""
    arr = [0, 8, 4, 12, 2, 10, 6, 14, 1, 9, 5, 13, 3, 11, 7, 15]
    result = find_longest_increasing_subsequence(arr)
    assert len(result) == 6
    assert all(result[i] < result[i+1] for i in range(len(result)-1))

def test_multiple_possible_subsequences():
    """Test when multiple subsequences of the same length exist"""
    arr = [1, 5, 0, 6, 2, 3]
    result = find_longest_increasing_subsequence(arr)
    assert len(result) == 3
    assert all(result[i] < result[i+1] for i in range(len(result)-1))