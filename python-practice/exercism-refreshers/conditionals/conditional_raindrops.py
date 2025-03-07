"""
Raindrops - Conditional Sound Generation Based on Factors

Context:
This program converts a number into its corresponding raindrop sounds.
It's a variation of the classic FizzBuzz programming exercise where 
factors determine the output string. Each factor has a specific sound 
associated with it.

This exercise demonstrates:
1. Modulo operations for testing divisibility
2. Conditionals for building a result string based on multiple tests
3. String concatenation within conditionals
4. Use of truthy/falsy values for final result determination
5. Code flattening techniques to increase readability

Learning process:
My initial implementation was straightforward with separate if statements,
but I later refined it to make the code more concise and flatten the 
conditionals where possible.
"""

def convert(number: int) -> str:
    """
    Convert a number to a raindrop sound string based on its factors.
    
    Args:
        number: int - The number to be converted
        
    Returns:
        str - A string representation of the raindrop sounds or the original number
        
    Purpose:
        Apply the following rules to convert a number:
        - Add "Pling" if number is divisible by 3
        - Add "Plang" if number is divisible by 5
        - Add "Plong" if number is divisible by 7
        - Return the number as a string if not divisible by 3, 5, or 7
        
    Evolution:
        I initially wrote this with simple if statements directly checking divisibility.
        Later improved it to use a tuple of vowel-factor pairs for better extensibility.
    """
    sounds = ''
    drops = ("i", 3), ("a", 5), ("o", 7)  # Tuple of (vowel, factor) pairs
    
    # Loop through each vowel-factor pair
    for vowel, factor in drops:
        # If number is divisible by the factor, add corresponding sound
        if number % factor == 0: sounds += f'Pl{vowel}ng'  # Using f-string for string interpolation
    
    # Return either the sound string or the original number as a string
    return sounds or str(number)  # Using Python's "or" with truthy/falsy logic
