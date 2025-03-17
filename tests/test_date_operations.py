import pytest
from datetime import date
from src.date_operations import add_days_to_date

def test_add_days_to_date_basic():
    """Test adding days to a date works correctly."""
    start_date = date(2023, 1, 1)
    result = add_days_to_date(start_date, 5)
    assert result == date(2023, 1, 6)

def test_add_days_to_date_zero():
    """Test adding zero days returns the original date."""
    start_date = date(2023, 1, 1)
    result = add_days_to_date(start_date, 0)
    assert result == start_date

def test_add_days_to_date_year_change():
    """Test adding days that cross year boundary."""
    start_date = date(2023, 12, 28)
    result = add_days_to_date(start_date, 5)
    assert result == date(2024, 1, 2)

def test_add_days_to_date_leap_year():
    """Test adding days in a leap year."""
    start_date = date(2024, 2, 28)
    result = add_days_to_date(start_date, 1)
    assert result == date(2024, 2, 29)

def test_add_days_to_date_invalid_input_type():
    """Test that TypeError is raised for invalid input types."""
    with pytest.raises(TypeError, match="input_date must be a datetime.date object"):
        add_days_to_date("2023-01-01", 5)
    
    with pytest.raises(TypeError, match="days_to_add must be an integer"):
        add_days_to_date(date(2023, 1, 1), "5")

def test_add_days_to_date_negative_days():
    """Test that ValueError is raised for negative days."""
    with pytest.raises(ValueError, match="days_to_add must be a non-negative integer"):
        add_days_to_date(date(2023, 1, 1), -5)