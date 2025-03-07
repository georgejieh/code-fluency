"""
Isogram Validator - Detecting words with no repeating letters

Context:
An isogram is a word or phrase where no letter appears more than once.
This exercise involves determining if a given string is an isogram.
Spaces and hyphens can appear multiple times.

This exercise demonstrates:
1. Character tracking in strings
2. Using dictionary comprehension to set up letter tracking
3. Handling non-alphabetic characters in validation
4. Comparing sets and lists for character uniqueness

The challenge requires determining if a given text is an isogram - a word
or phrase without a repeating letter, allowing spaces and hyphens.
"""


def is_isogram(string: str) -> bool:
    """
    Determine if a string is an isogram (has no repeating letters).
    
    Args:
        string: A string to check
        
    Returns:
        True if the string is an isogram, False otherwise
        
    Purpose:
        Validates whether a given text contains any repeated letters.
        Spaces and hyphens are allowed to appear multiple times.
        
    Notes:
        My initial solution used a dictionary to track letter counts:
        ```
        letter_counts = {chr(letter): 0 for letter in range(ord('a'), ord('z') + 1)}
        for char_position, char in enumerate(string.lower()):
            if not char.isalpha():
                continue
            if char in letter_counts:
                letter_counts[char] += 1
        return all(count < 2 for count in letter_counts.values())
        ```
        
        After reading "Dig Deeper" about set operations, learned a more elegant solution
        by comparing the length of a set (unique letters) with the original list length.
    """
    letters = [char for char in string.lower() if char.isalpha()]
    return len(set(letters)) == len(letters)