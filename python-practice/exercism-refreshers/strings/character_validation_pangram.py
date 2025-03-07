"""
Pangram Detector - Identifying if a sentence contains all letters of the alphabet

Context:
This exercise simulates working for a company that sells fonts through their website.
They want to show different sentences that use all 26 letters of the English alphabet
to display font characteristics completely.

This exercise demonstrates:
1. Character-level string validation
2. Set operations for efficient character checking
3. Case insensitivity in string processing
4. Dictionary comprehension for character tracking

The challenge requires determining if a given text is a pangram - a sentence
that contains every letter of the alphabet at least once, regardless of case.
"""


def is_pangram(sentence: str) -> bool:
    """
    Determine if a sentence is a pangram (contains every letter of the alphabet).
    
    Args:
        sentence: A string to check
        
    Returns:
        True if the sentence is a pangram, False otherwise
        
    Purpose:
        Validates whether a given text contains all 26 letters of the English
        alphabet, ignoring case sensitivity.
    
    Notes:
        Initially approached with a dictionary to track occurrence of each letter:
        ```
        letter_counts = {chr(letter): 0 for letter in range(ord('a'), ord('z') + 1)} # Had to look up the method of making a dictionary that lists out all the alphabet. Didn't know what ord() and chr() is.
        for char in sentence.lower():
            if not char.isalpha():
                continue
            if char in letter_counts:
                letter_counts[char] += 1
        return all(count > 0 for count in letter_counts.values())
        ```
        
        After learning about sets, discovered a much more elegant solution.
    """
    # After reading "Dig Deeper" and learning about sets and the issubset method
    return set('abcdefghijklmnopqrstuvwxyz').issubset(set(sentence.lower()))