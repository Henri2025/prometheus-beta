import pytest
from src.merge_sorted_arrays import merge_sorted_arrays, is_sorted

def test_merge_sorted_arrays_basic():
    """Test merging two basic sorted arrays"""
    arr1 = [1, 3, 5]
    arr2 = [2, 4, 6]
    expected = [1, 2, 3, 4, 5, 6]
    assert merge_sorted_arrays(arr1, arr2) == expected

def test_merge_sorted_arrays_with_duplicates():
    """Test merging arrays with duplicate values"""
    arr1 = [1, 2, 3, 3]
    arr2 = [2, 3, 4, 5]
    expected = [1, 2, 2, 3, 3, 3, 4, 5]
    assert merge_sorted_arrays(arr1, arr2) == expected

def test_merge_sorted_arrays_empty_arrays():
    """Test merging with empty arrays"""
    arr1 = []
    arr2 = []
    expected = []
    assert merge_sorted_arrays(arr1, arr2) == expected

def test_merge_sorted_arrays_one_empty():
    """Test merging when one array is empty"""
    arr1 = [1, 2, 3]
    arr2 = []
    expected = [1, 2, 3]
    assert merge_sorted_arrays(arr1, arr2) == expected

def test_merge_sorted_arrays_different_lengths():
    """Test merging arrays of different lengths"""
    arr1 = [1, 4, 6]
    arr2 = [2, 3, 5, 7, 8]
    expected = [1, 2, 3, 4, 5, 6, 7, 8]
    assert merge_sorted_arrays(arr1, arr2) == expected

def test_merge_sorted_arrays_type_error():
    """Test raising TypeError for non-list inputs"""
    with pytest.raises(TypeError):
        merge_sorted_arrays(123, [])
    with pytest.raises(TypeError):
        merge_sorted_arrays([], "not a list")

def test_merge_sorted_arrays_unsorted_error():
    """Test raising ValueError for unsorted arrays"""
    with pytest.raises(ValueError):
        merge_sorted_arrays([3, 1, 2], [1, 2, 3])
    with pytest.raises(ValueError):
        merge_sorted_arrays([1, 2, 3], [3, 1, 2])

def test_is_sorted():
    """Test is_sorted helper function"""
    assert is_sorted([]) == True
    assert is_sorted([1]) == True
    assert is_sorted([1, 1, 2, 3]) == True
    assert is_sorted([1, 2, 3, 4]) == True
    assert is_sorted([4, 3, 2, 1]) == False