from datetime import datetime, timedelta

def calculate_timestamp_difference(timestamp1: str, timestamp2: str, format: str = '%Y-%m-%d %H:%M:%S') -> timedelta:
    """
    Calculate the time difference between two timestamps.

    Args:
        timestamp1 (str): First timestamp in the specified format
        timestamp2 (str): Second timestamp in the specified format
        format (str, optional): Datetime format string. Defaults to '%Y-%m-%d %H:%M:%S'.

    Returns:
        timedelta: Time difference between the two timestamps

    Raises:
        ValueError: If timestamps cannot be parsed or have invalid format
        AttributeError: If input is not a string
    """
    # Validate input type first
    if not isinstance(timestamp1, str) or not isinstance(timestamp2, str):
        raise AttributeError("Timestamps must be strings")
    
    try:
        dt1 = datetime.strptime(timestamp1, format)
        dt2 = datetime.strptime(timestamp2, format)
        return abs(dt2 - dt1)
    except ValueError as e:
        raise ValueError(f"Invalid timestamp format. {str(e)}")