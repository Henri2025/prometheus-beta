def sum_digits(number):
    """
    Calculate the sum of digits for a given integer.

    Args:
        number (int): The input number whose digits will be summed.

    Returns:
        int: The sum of all digits in the input number.

    Raises:
        TypeError: If the input is not an integer.
    """
    # Validate input is an integer
    if not isinstance(number, int):
        raise TypeError("Input must be an integer")
    
    # Handle negative numbers by converting to absolute value
    number = abs(number)
    
    # If number is 0, return 0
    if number == 0:
        return 0
    
    # Sum the digits
    digit_sum = 0
    while number > 0:
        digit_sum += number % 10  # Get the last digit
        number //= 10  # Remove the last digit
    
    return digit_sum