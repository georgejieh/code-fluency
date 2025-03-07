"""
ISBN-10 Validator - Checking book identification numbers

Context:
ISBN-10 is a standard for book identification numbers. This program
validates if a given string is a valid ISBN-10 number according to
its checksum algorithm.

This exercise demonstrates:
1. String preprocessing (removing hyphens)
2. Validation of string format and content
3. Implementation of a checksum algorithm
4. Handling special character cases (X as a check digit)

The ISBN-10 format contains 9 digits plus a check character (a digit or 'X').
The check character is calculated using a weighted sum formula followed by
modulo 11 division.
"""


def is_valid(isbn: str) -> bool:
    """
    Determine if a string is a valid ISBN-10 number.
    
    Args:
        isbn: A string containing a potential ISBN-10 number
        
    Returns:
        True if the string is a valid ISBN-10 number, False otherwise
        
    Purpose:
        Validates a string against the ISBN-10 standard, which requires:
        1. 10 characters (after removing hyphens)
        2. First 9 characters must be digits
        3. Last character must be a digit or 'X' (representing 10)
        4. The weighted sum formula (d₁*10 + d₂*9 + ... + d₁₀*1) must be divisible by 11
        
    Notes:
        My challenge with this exercise wasn't implementing the code, but figuring out
        the right approach to handle ISBN validation. My first attempt was overly complex:
        ```
        def is_valid(isbn: string) -> bool:
            total = 0
            if len(isbn) != 13 or len(isbn) != 10:
                return False
            else:
                for digit_position, digit in enumerate(isbn.lower()):
                    if not digit.isnumeric():
                        if digit == 'x' and digit_position == 12:
                            total += 10 * 1
                        continue
                    else:
                        total +=  ...
        ```
        
        I hesitated to remove hyphens from the string before processing. I thought I needed 
        to account for both formatted ISBNs (with hyphens, total length 13) and unformatted 
        ones (length 10). This made the loop logic much more complicated.
        
        If I had simply removed the hyphens first, the validation would have been simpler:
        ```
        else:
            total += int(digit) * (digit_position + 1)
        ```
        
        After running the unit tests, I realized that any non-standard formatting should 
        simply be considered invalid - a much cleaner approach than trying to accommodate
        all possible formats.
    """
    isbn = isbn.replace('-', '')
    if len(isbn) != 10: return False
    for i in range(9):
        if not isbn[i].isdigit(): return False
    if not isbn[9].isdigit() and isbn[9].upper() != 'X': return False
    total = 0
    for i in range(9):
        total += int(isbn[i]) * (10 - i)
    if isbn[9].upper() == 'X': total += 10
    else: total += int(isbn[9])
    return total % 11 == 0