from datetime import date, timedelta

def add_days_to_date(input_date, days_to_add):
    """
    Add a specified number of days to a given date.

    Args:
        input_date (date): The starting date to add days to.
        days_to_add (int): The number of days to add to the input date.

    Returns:
        date: A new date object representing the result of adding days to the input date.

    Raises:
        TypeError: If input_date is not a datetime.date object or days_to_add is not an integer.
        ValueError: If days_to_add is negative.
    """
    # Type checking
    if not isinstance(input_date, date):
        raise TypeError("input_date must be a datetime.date object")
    
    if not isinstance(days_to_add, int):
        raise TypeError("days_to_add must be an integer")
    
    # Validate days_to_add is non-negative
    if days_to_add < 0:
        raise ValueError("days_to_add must be a non-negative integer")
    
    # Add days using timedelta
    return input_date + timedelta(days=days_to_add)