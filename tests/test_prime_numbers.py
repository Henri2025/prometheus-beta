import pytest
from src.prime_numbers import get_primes_to_n

def test_primes_to_100():
    """Test that primes to 100 are correctly identified."""
    expected_primes = [
        2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
        43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97
    ]
    assert get_primes_to_n(100) == expected_primes

def test_small_primes():
    """Test handling of small input values."""
    assert get_primes_to_n(10) == [2, 3, 5, 7]
    assert get_primes_to_n(2) == [2]
    assert get_primes_to_n(1) == []

def test_edge_cases():
    """Test edge cases and error handling."""
    # Test invalid input types
    with pytest.raises(TypeError):
        get_primes_to_n("100")
    with pytest.raises(TypeError):
        get_primes_to_n(3.14)
    
    # Test negative input
    with pytest.raises(ValueError):
        get_primes_to_n(0)
    with pytest.raises(ValueError):
        get_primes_to_n(-10)

def test_large_input():
    """Test handling of a larger input."""
    primes = get_primes_to_n(1000)
    # Check first few and last few primes
    assert primes[:5] == [2, 3, 5, 7, 11]
    assert primes[-5:] == [937, 941, 947, 953, 967]
    assert len(primes) == 168  # Number of primes <= 1000