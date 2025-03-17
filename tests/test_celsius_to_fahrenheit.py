import pytest
from src.celsius_to_fahrenheit import celsius_to_fahrenheit

def test_freezing_point():
    """Test conversion of 0°C (freezing point of water)"""
    assert celsius_to_fahrenheit(0) == 32

def test_boiling_point():
    """Test conversion of 100°C (boiling point of water)"""
    assert celsius_to_fahrenheit(100) == 212

def test_negative_temperature():
    """Test conversion of a negative temperature"""
    assert celsius_to_fahrenheit(-40) == -40

def test_decimal_temperature():
    """Test conversion of a decimal temperature"""
    assert round(celsius_to_fahrenheit(37.5), 1) == 99.5

def test_large_positive_temperature():
    """Test conversion of a large positive temperature"""
    assert round(celsius_to_fahrenheit(1000), 1) == 1832

def test_invalid_input_type():
    """Test that TypeError is raised for invalid input types"""
    with pytest.raises(TypeError):
        celsius_to_fahrenheit("not a number")
    
    with pytest.raises(TypeError):
        celsius_to_fahrenheit(None)
    
    with pytest.raises(TypeError):
        celsius_to_fahrenheit([10])