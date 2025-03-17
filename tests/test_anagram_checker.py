import pytest
from src.anagram_checker import are_anagrams

def test_basic_anagrams():
    """Test basic anagram scenarios"""
    assert are_anagrams('listen', 'silent') == True
    assert are_anagrams('triangle', 'integral') == True

def test_non_anagrams():
    """Test strings that are not anagrams"""
    assert are_anagrams('hello', 'world') == False
    assert are_anagrams('python', 'java') == False

def test_case_insensitive():
    """Test that anagram check is case-insensitive"""
    assert are_anagrams('Debit Card', 'Bad Credit') == True
    assert are_anagrams('Astronomer', 'Moon Starer') == True

def test_whitespace_handling():
    """Test that whitespace is ignored"""
    assert are_anagrams('rail safety', 'fairy tales') == True
    assert are_anagrams('  listen  ', 'silent') == True

def test_empty_strings():
    """Test empty string scenarios"""
    assert are_anagrams('', '') == True

def test_different_lengths():
    """Test strings of different lengths"""
    assert are_anagrams('short', 'longer') == False

def test_invalid_inputs():
    """Test error handling for invalid input types"""
    with pytest.raises(TypeError):
        are_anagrams(123, 'abc')
    with pytest.raises(TypeError):
        are_anagrams('abc', None)

def test_unicode_characters():
    """Test anagram check with unicode characters"""
    assert are_anagrams('résumé', 'suméer') == True
    assert are_anagrams('café', 'face') == False

def test_repeated_characters():
    """Test anagram check with repeated characters"""
    assert are_anagrams('aab', 'aba') == True
    assert are_anagrams('aab', 'aaa') == False