import unicodedata

def are_anagrams(str1: str, str2: str) -> bool:
    """
    Check if two strings are anagrams of each other.

    An anagram is a word or phrase formed by rearranging the letters of another word or phrase,
    using all the original letters exactly once. The comparison is case-insensitive and 
    ignores whitespace.

    Args:
        str1 (str): The first string to compare
        str2 (str): The second string to compare

    Returns:
        bool: True if the strings are anagrams, False otherwise

    Raises:
        TypeError: If either input is not a string
    """
    # Validate input types
    if not (isinstance(str1, str) and isinstance(str2, str)):
        raise TypeError("Both inputs must be strings")
    
    # Normalize unicode characters and remove accents
    def normalize(s: str) -> str:
        # Convert to lowercase, remove whitespace, and normalize unicode
        normalized = unicodedata.normalize('NFKD', s.lower())
        # Remove accents and non-spacing marks
        return ''.join(c for c in normalized if not unicodedata.combining(c))
    
    # Remove whitespace and normalize
    cleaned_str1 = normalize(''.join(str1.split()))
    cleaned_str2 = normalize(''.join(str2.split()))
    
    # Quick length check
    if len(cleaned_str1) != len(cleaned_str2):
        return False
    
    # Use character frequency counting
    char_count = {}
    
    # Count characters in first string
    for char in cleaned_str1:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Subtract characters from second string
    for char in cleaned_str2:
        if char not in char_count:
            return False
        char_count[char] -= 1
        if char_count[char] < 0:
            return False
    
    return True