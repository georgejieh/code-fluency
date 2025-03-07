"""
Rotational Cipher - Implementing the Caesar cipher encryption technique

Context:
The rotational cipher, also known as the Caesar cipher, is a simple encryption
technique that shifts letters in the alphabet by a fixed number of positions.
This is one of the simplest encryption techniques and has historical significance.

This exercise demonstrates:
1. Character-by-character string transformation
2. Unicode code point manipulation with ord() and chr()
3. Modular arithmetic for alphabet wrapping
4. Preserving non-alphabetic characters in transformations

The challenge requires implementing a function that can encrypt text by
rotating each letter by a specified number of positions in the alphabet,
while preserving case, punctuation, and spacing.
"""


def rotate(text: str, key: int) -> str:
    """
    Encrypt text using a rotational (Caesar) cipher.
    
    Args:
        text: The string to encrypt
        key: The number of positions to shift each letter (0-26)
        
    Returns:
        The encrypted string with each letter shifted by the key value
        
    Purpose:
        Implements a Caesar cipher encryption by shifting each letter in the
        input text by the specified number of positions in the alphabet.
        Non-alphabetic characters remain unchanged.
        
    Notes:
        I went through several iterations to get the logic right:
        
        First attempt: Used char_position in the loop unnecessarily and had complex
        offset calculations for the wraparound:
        ```
        for char_position, char in enumerate(text):
            ...
            if code_point > 90:
                code_point = (code_point - 90) + 65
                encoded += chr(code_point)
        ```
        
        Second attempt: Removed char_position from the loop but still used the same
        complex offset calculations.
        
        Third attempt: Simplified the wraparound logic to just subtract 26:
        ```
        if code_point > 90:
            code_point = code_point - 26
        ```
        
        Final attempt before reading Dig Deeper: Combined conditions and used a more
        concise expression for handling alphabet boundaries:
        ```
        if (code_point > 90 and ord(char) <= 90) or (code_point > 122): 
            code_point -= 26
        ```
        
        After reading Dig Deeper: Discovered the elegant mathematical approach using 
        modular arithmetic with proper ASCII offsets. I had to learn to normalize character 
        values by subtracting the ASCII value (65 for uppercase, 97 for lowercase), apply the 
        rotation with the modulo operator to handle the wraparound, and then convert back by 
        adding the ASCII offset again.
    """
    encoded = ""
    for char in text:
        if not char.isalpha(): 
            encoded += char
        else:
            if char.isupper(): 
                encoded += chr((ord(char) - 65 + key) % 26 + 65)
            else: 
                encoded += chr((ord(char) - 97 + key) % 26 + 97)
    return encoded