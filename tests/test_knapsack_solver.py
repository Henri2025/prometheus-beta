import pytest
from src.knapsack_solver import knapsack

def test_basic_knapsack():
    """Test a basic knapsack scenario"""
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    max_value, selected_items = knapsack(weights, values, capacity)
    
    assert max_value == 220
    assert set(selected_items) == {1, 2}

def test_empty_input():
    """Test with empty input lists"""
    max_value, selected_items = knapsack([], [], 100)
    
    assert max_value == 0
    assert selected_items == []

def test_zero_capacity():
    """Test with zero capacity"""
    weights = [10, 20, 30]
    values = [60, 100, 120]
    max_value, selected_items = knapsack(weights, values, 0)
    
    assert max_value == 0
    assert selected_items == []

def test_all_items_fit():
    """Test when all items can fit in the knapsack"""
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 100
    max_value, selected_items = knapsack(weights, values, 100)
    
    assert max_value == 280
    assert set(selected_items) == {0, 1, 2}

def test_no_items_fit():
    """Test when no items can fit in the knapsack"""
    weights = [50, 60, 70]
    values = [60, 100, 120]
    capacity = 40
    max_value, selected_items = knapsack(weights, values, 40)
    
    assert max_value == 0
    assert selected_items == []

def test_mismatched_input_lengths():
    """Test with mismatched weights and values lengths"""
    with pytest.raises(ValueError, match="Weights and values lists must have the same length"):
        knapsack([10, 20], [60, 100, 120], 50)

def test_negative_capacity():
    """Test with negative capacity"""
    with pytest.raises(ValueError, match="Capacity must be non-negative"):
        knapsack([10, 20, 30], [60, 100, 120], -10)

def test_invalid_input_types():
    """Test with invalid input types"""
    with pytest.raises(ValueError, match="Invalid input types"):
        knapsack("not a list", "also not a list", "not an int")