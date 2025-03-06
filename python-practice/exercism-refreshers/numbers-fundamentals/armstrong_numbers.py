"""
Armstrong Number Validator

Context:
An Armstrong number is a special type of number where the sum of each digit raised
to the power of the total number of digits equals the original number itself.
This exercise tests digit manipulation, exponentiation, and validation logic.

For example:
- 9 is an Armstrong number because: 9 = 9^1 = 9
- 153 is an Armstrong number because: 153 = 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153
- 154 is NOT an Armstrong number because: 154 != 1^3 + 5^3 + 4^3 = 1 + 125 + 64 = 190

This exercise demonstrates:
1. Converting between different types (int to str and back)
2. String indexing and iteration
3. Using exponentiation to calculate powers
4. Accumulating sums using proper operators
"""

def is_armstrong_number(number):
    """
    Determine if a number is an Armstrong number.
    
    An Armstrong number is a number that is the sum of its own digits 
    each raised to the power of the number of digits.
    
    Args:
        number: int - the number to check
        
    Returns:
        bool - True if the number is an Armstrong number, False otherwise
        
    Purpose:
        Validate if a given number has the Armstrong property where the sum of each digit
        raised to the power of the number of digits equals the original number.
        
    Notes:
        I initially wrote the += operator incorrectly as =+, which is a common mistake.
        The += operator adds the right operand to the left operand and assigns the result
        to the left operand.
    """
    stringified_number = str(number)
    value = 0
    for digit_position in range(0, len(stringified_number)):
        value += int(stringified_number[digit_position]) ** len(stringified_number)  # Initially wrote =+ incorrectly
    return value == number