import pytest
from src.least_common_multiple import find_lcm

def test_lcm_basic_positive_numbers():
    """Test LCM of basic positive numbers"""
    assert find_lcm(4, 6) == 12
    assert find_lcm(21, 6) == 42
    assert find_lcm(17, 5) == 85

def test_lcm_same_numbers():
    """Test LCM when both numbers are the same"""
    assert find_lcm(7, 7) == 7
    assert find_lcm(13, 13) == 13

def test_lcm_one_is_multiple():
    """Test LCM when one number is a multiple of the other"""
    assert find_lcm(4, 8) == 8
    assert find_lcm(15, 5) == 15

def test_lcm_coprime_numbers():
    """Test LCM of coprime numbers"""
    assert find_lcm(7, 11) == 77
    assert find_lcm(13, 17) == 221

def test_invalid_inputs():
    """Test error handling for invalid inputs"""
    # Non-positive inputs
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        find_lcm(0, 5)
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        find_lcm(-3, 4)
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        find_lcm(3, -4)
    with pytest.raises(ValueError, match="Inputs must be positive integers"):
        find_lcm(0, 0)

def test_non_integer_inputs():
    """Test error handling for non-integer inputs"""
    with pytest.raises(ValueError, match="Inputs must be integers"):
        find_lcm(3.5, 4)
    with pytest.raises(ValueError, match="Inputs must be integers"):
        find_lcm(4, "5")
    with pytest.raises(ValueError, match="Inputs must be integers"):
        find_lcm([3], 4)