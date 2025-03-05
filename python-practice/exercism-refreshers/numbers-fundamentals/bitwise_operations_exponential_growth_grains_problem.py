"""
Grains problem - calculating number of grains on a chessboard
where each square has double the number of grains as the previous square.

This exercise demonstrates:
1. Exponential growth calculations
2. Bitwise operations as an optimization technique
3. Input validation with custom error messages
4. Performance differences between various approaches
"""

#############################################
# Initial attempt - before optimization
#############################################

def square_initial(number):
    """
    Calculate the number of grains on a specific square.
    
    Notes:
    - Had to look up chaining comparisons (1 <= number <= 64)
    - Used 2 ** (number - 1) for exponentiation, had to remember Python uses ** not ^ (like in Excel)
    - Had to look up how to raise a custom ValueError with specific message
    """
    if not 1 <= number <= 64:  # Chained comparison
        raise ValueError("square must be between 1 and 64")
    number_of_grains = 1 * (2 ** (number - 1))  # Exponential calculation
    return number_of_grains


def total_initial():
    """
    Calculate the total number of grains on the chessboard.
    
    Notes:
    - Had to look up range-based for loop syntax
    - Uses a naive approach of summing each square's value
    """
    total_grains = 0
    for square_number in range(1, 65):  # Range-based for loop (1 to 64 inclusive)
        total_grains += square_initial(square_number)
    return total_grains


#############################################
# Optimized solutions from Exercism
#############################################

# 1. Using bit-shifting (most efficient for single square)
def square_bitshift(number):
    """
    Calculate grains using bitwise left shift operation.
    The operation 1 << n is equivalent to 2^n in binary.
    """
    if number < 1 or number > 64:
        raise ValueError('square must be between 1 and 64')
    return 1 << number - 1  # Bitwise left shift is more efficient than exponentiation


def total_bitshift():
    """
    Calculate total using bitwise left shift.
    The sum of powers of 2 from 0 to n-1 equals (2^n - 1).
    """
    return (1 << 64) - 1  # Equals 2^64 - 1, the sum of all squares


# 2. Using standard exponentiation
def square_exponentiation(number):
    """Calculate grains using Python's exponentiation operator."""
    if number < 1 or number > 64:
        raise ValueError('square must be between 1 and 64')
    return 2 ** (number - 1)  # Standard exponentiation


def total_exponentiation():
    """Calculate total using the formula for sum of geometric series."""
    return 2 ** 64 - 1  # Mathematical formula for sum of powers of 2


# 3. Using pow() function
def square_pow(number):
    """Calculate grains using Python's pow() function."""
    if number < 1 or number > 64:
        raise ValueError('square must be between 1 and 64')
    return pow(2, number - 1)  # Built-in power function


def total_pow():
    """Calculate total using pow() function."""
    return pow(2, 64) - 1  # Slower for this specific use case


#############################################
# Performance notes from testing
#############################################
"""
Performance comparison:
- Bit shifting is the fastest for square calculations
- Bit shifting and exponentiation are about the same for total
- Exponentiation and pow() are about the same for square
- pow() is significantly the slowest for total
"""


#############################################
# Final optimized solution combining personal style with efficiency
#############################################

def square(number):
    """
    Calculate the number of grains on a specific square (optimized).
    Uses my preferred coding style with meaningful variable names
    combined with the more efficient bitshift operation.
    """
    if not 1 <= number <= 64:  # My preferred chained comparison style
        raise ValueError("square must be between 1 and 64")
    number_of_grains = 1 << number - 1  # Efficient bitshift operation
    return number_of_grains


def total():
    """
    Calculate the total number of grains on the chessboard (optimized).
    Uses the mathematical formula for sum of powers of 2 instead of looping.
    """
    return 2 ** 64 - 1  # Direct formula is much more efficient than iteration