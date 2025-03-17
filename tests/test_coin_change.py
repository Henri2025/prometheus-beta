import pytest
from src.coin_change import coin_change

def test_basic_coin_change():
    """Test basic coin change scenarios"""
    assert coin_change([1, 2, 5], 11) == 3  # 5 + 5 + 1
    assert coin_change([2], 3) == -1  # Cannot make 3 with only 2-value coins
    assert coin_change([1], 0) == 0  # Zero amount

def test_edge_cases():
    """Test edge case scenarios"""
    # Empty coin list should raise ValueError
    with pytest.raises(ValueError, match="Coins list cannot be empty"):
        coin_change([], 5)
    
    # Negative amount should raise ValueError
    with pytest.raises(ValueError, match="Amount must be non-negative"):
        coin_change([1, 2, 5], -1)

def test_different_coin_sets():
    """Test various coin denomination sets"""
    assert coin_change([1, 5, 10, 25], 30) == 2  # 25 + 5
    assert coin_change([2, 3, 5], 8) == 2  # 3 + 5
    assert coin_change([186, 419, 83, 408], 6249) == 20

def test_impossible_amounts():
    """Test scenarios where exact change is impossible"""
    assert coin_change([2], 3) == -1
    assert coin_change([5, 10], 7) == -1

def test_large_amounts():
    """Test larger amount scenarios"""
    # Ensure function can handle larger inputs without excessive time/memory
    result = coin_change([1, 2, 5, 10, 20, 50, 100], 1000)
    assert result > 0