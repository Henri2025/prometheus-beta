import pytest
from src.gcd import calculate_gcd

def test_gcd_positive_numbers():
    """Test GCD of positive numbers"""
    assert calculate_gcd(48, 18) == 6
    assert calculate_gcd(54, 24) == 6
    assert calculate_gcd(17, 23) == 1

def test_gcd_one_zero():
    """Test GCD when one number is zero"""
    assert calculate_gcd(0, 5) == 5
    assert calculate_gcd(5, 0) == 5
    assert calculate_gcd(0, 0) == 0

def test_gcd_equal_numbers():
    """Test GCD of equal numbers"""
    assert calculate_gcd(7, 7) == 7
    assert calculate_gcd(11, 11) == 11

def test_gcd_coprime_numbers():
    """Test GCD of coprime numbers"""
    assert calculate_gcd(17, 23) == 1
    assert calculate_gcd(13, 16) == 1

def test_invalid_input_types():
    """Test handling of invalid input types"""
    with pytest.raises(ValueError, match="Inputs must be integers"):
        calculate_gcd(3.14, 5)
    with pytest.raises(ValueError, match="Inputs must be integers"):
        calculate_gcd("10", 5)
    with pytest.raises(ValueError, match="Inputs must be integers"):
        calculate_gcd([10], 5)

def test_negative_inputs():
    """Test handling of negative inputs"""
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        calculate_gcd(-10, 5)
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        calculate_gcd(10, -5)
    with pytest.raises(ValueError, match="Inputs must be non-negative integers"):
        calculate_gcd(-10, -5)