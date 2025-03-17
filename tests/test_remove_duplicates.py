import pytest
from src.remove_duplicates import remove_duplicates

def test_remove_duplicates_basic():
    """Test basic functionality of removing duplicates"""
    assert remove_duplicates([1, 2, 3, 2, 4, 1]) == [1, 2, 3, 4]

def test_remove_duplicates_strings():
    """Test removing duplicates from a list of strings"""
    assert remove_duplicates(['a', 'b', 'a', 'c']) == ['a', 'b', 'c']

def test_remove_duplicates_order_preservation():
    """Ensure original order of first occurrence is maintained"""
    input_list = [5, 2, 5, 3, 1, 2, 4]
    assert remove_duplicates(input_list) == [5, 2, 3, 1, 4]

def test_remove_duplicates_empty_list():
    """Test behavior with an empty list"""
    assert remove_duplicates([]) == []

def test_remove_duplicates_no_duplicates():
    """Test list with no duplicates"""
    input_list = [1, 2, 3, 4, 5]
    assert remove_duplicates(input_list) == input_list

def test_remove_duplicates_all_duplicates():
    """Test list where all elements are duplicates"""
    assert remove_duplicates([1, 1, 1, 1]) == [1]

def test_remove_duplicates_mixed_types():
    """Test list with mixed types of elements"""
    input_list = [1, '1', 2, '2', 1, '1']
    assert remove_duplicates(input_list) == [1, '1', 2, '2']

def test_remove_duplicates_invalid_input():
    """Test that TypeError is raised for non-list inputs"""
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates("not a list")
    
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates(123)
    
    with pytest.raises(TypeError, match="Input must be a list"):
        remove_duplicates(None)