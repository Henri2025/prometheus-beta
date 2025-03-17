import pytest
from src.days_between_dates import calculate_days_between_dates

def test_days_between_dates_same_date():
    """Test calculating days between the same date"""
    assert calculate_days_between_dates('2023-01-01', '2023-01-01') == 0

def test_days_between_dates_different_dates():
    """Test calculating days between different dates"""
    assert calculate_days_between_dates('2023-01-01', '2023-01-10') == 9
    assert calculate_days_between_dates('2023-01-10', '2023-01-01') == 9

def test_days_between_dates_different_years():
    """Test calculating days between dates in different years"""
    assert calculate_days_between_dates('2022-12-31', '2023-01-01') == 1

def test_days_between_dates_leap_year():
    """Test calculation across a leap year"""
    assert calculate_days_between_dates('2020-02-28', '2020-03-01') == 2

def test_invalid_date_format():
    """Test handling of invalid date formats"""
    with pytest.raises(ValueError, match="Invalid date format"):
        calculate_days_between_dates('2023/01/01', '2023-01-10')

def test_invalid_date():
    """Test handling of impossible dates"""
    with pytest.raises(ValueError, match="Invalid date"):
        calculate_days_between_dates('2023-02-30', '2023-01-01')

def test_order_independence():
    """Test that order of dates doesn't matter"""
    date1 = '2023-01-01'
    date2 = '2023-01-10'
    assert calculate_days_between_dates(date1, date2) == calculate_days_between_dates(date2, date1)