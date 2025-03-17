import pytest
from datetime import timedelta
from src.timestamp_difference import calculate_timestamp_difference

def test_calculate_timestamp_difference_same_time():
    """Test time difference when timestamps are identical"""
    timestamp = '2023-01-01 12:00:00'
    result = calculate_timestamp_difference(timestamp, timestamp)
    assert result == timedelta(0)

def test_calculate_timestamp_difference_hours():
    """Test time difference in hours"""
    timestamp1 = '2023-01-01 10:00:00'
    timestamp2 = '2023-01-01 14:30:00'
    result = calculate_timestamp_difference(timestamp1, timestamp2)
    assert result == timedelta(hours=4, minutes=30)

def test_calculate_timestamp_difference_days():
    """Test time difference across multiple days"""
    timestamp1 = '2023-01-01 12:00:00'
    timestamp2 = '2023-01-03 12:00:00'
    result = calculate_timestamp_difference(timestamp1, timestamp2)
    assert result == timedelta(days=2)

def test_calculate_timestamp_difference_order_independent():
    """Test that order of timestamps doesn't matter"""
    timestamp1 = '2023-01-01 14:30:00'
    timestamp2 = '2023-01-01 10:00:00'
    result = calculate_timestamp_difference(timestamp1, timestamp2)
    assert result == timedelta(hours=4, minutes=30)

def test_calculate_timestamp_difference_custom_format():
    """Test timestamp difference with a custom format"""
    timestamp1 = '01/01/2023 12:00:00'
    timestamp2 = '01/02/2023 12:00:00'
    result = calculate_timestamp_difference(timestamp1, timestamp2, format='%m/%d/%Y %H:%M:%S')
    assert result == timedelta(days=1)

def test_calculate_timestamp_difference_invalid_format():
    """Test error handling for invalid timestamp format"""
    with pytest.raises(ValueError, match="Invalid timestamp format"):
        calculate_timestamp_difference('invalid', 'timestamps', format='%Y-%m-%d')

def test_calculate_timestamp_difference_type_error():
    """Test error handling for non-string inputs"""
    with pytest.raises(AttributeError):
        calculate_timestamp_difference(123, 456)