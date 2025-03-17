import pytest
from src.digit_sum import sum_digits

def test_sum_digits_positive_number():
    """Test sum of digits for a positive number."""
    assert sum_digits(123) == 6  # 1 + 2 + 3 = 6
    assert sum_digits(9876) == 30  # 9 + 8 + 7 + 6 = 30

def test_sum_digits_zero():
    """Test sum of digits for zero."""
    assert sum_digits(0) == 0

def test_sum_digits_single_digit():
    """Test sum of digits for a single-digit number."""
    assert sum_digits(5) == 5

def test_sum_digits_negative_number():
    """Test sum of digits for a negative number."""
    assert sum_digits(-456) == 15  # abs(-456) = 456, 4 + 5 + 6 = 15

def test_sum_digits_invalid_input():
    """Test error handling for invalid input types."""
    with pytest.raises(TypeError):
        sum_digits("123")
    
    with pytest.raises(TypeError):
        sum_digits(3.14)
    
    with pytest.raises(TypeError):
        sum_digits(None)