import re
from datetime import datetime
import pytest
from src.current_time import get_current_time_formatted

def test_current_time_format():
    """
    Test that the function returns a time string in the correct format.
    """
    time_str = get_current_time_formatted()
    
    # Check the format matches HH:MM:SS
    assert re.match(r'^\d{2}:\d{2}:\d{2}$', time_str), "Time format should be HH:MM:SS"

def test_current_time_hours():
    """
    Test that hours are in 24-hour format (00-23).
    """
    time_str = get_current_time_formatted()
    hours = int(time_str.split(':')[0])
    
    assert 0 <= hours < 24, "Hours should be between 00 and 23"

def test_current_time_minutes_seconds():
    """
    Test that minutes and seconds are between 00-59.
    """
    time_str = get_current_time_formatted()
    minutes = int(time_str.split(':')[1])
    seconds = int(time_str.split(':')[2])
    
    assert 0 <= minutes < 60, "Minutes should be between 00 and 59"
    assert 0 <= seconds < 60, "Seconds should be between 00 and 59"

def test_multiple_calls_consistency():
    """
    Verify that the function can be called multiple times 
    without raising any exceptions.
    """
    for _ in range(5):
        time_str = get_current_time_formatted()
        assert isinstance(time_str, str), "Should always return a string"