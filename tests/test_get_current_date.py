import re
from datetime import date
from src.get_current_date import get_current_date_formatted

def test_get_current_date_formatted():
    """
    Test that the function returns the current date in YYYY-MM-DD format.
    """
    # Get the formatted date
    formatted_date = get_current_date_formatted()
    
    # Check that the returned value is a string
    assert isinstance(formatted_date, str), "Result should be a string"
    
    # Check the format using regex
    # YYYY-MM-DD format: 4 digits, hyphen, 2 digits, hyphen, 2 digits
    assert re.match(r'^\d{4}-\d{2}-\d{2}$', formatted_date), \
        "Date should be in YYYY-MM-DD format"
    
    # Verify the date matches the current date
    current_date = date.today()
    assert formatted_date == current_date.strftime("%Y-%m-%d"), \
        "Formatted date should match current date"