"""
Grains problem - calculating number of grains on a chessboard
where each square has double the number of grains as the previous square.

Context:
This is based on the classic wheat/chessboard story where:
- A servant asks a king for payment in wheat grains
- The servant requests one grain on the first square
- Then twice that amount on the second square
- Then twice that amount on the third square
- And so on for all 64 squares of a chessboard
- The program calculates both individual square values and the total

This exercise demonstrates:
1. Exponential growth calculations
2. Bitwise operations as an optimization technique
3. Input validation with custom error messages
4. Performance differences between various approaches

The challenge requires two functions:
- square(number): Returns grains on a specific square (1-64)
- total(): Returns the total grains on all squares combined
"""

#############################################
# Initial attempt - before optimization
#############################################

def square_initial(number):
    """
    Calculate the number of grains on a specific square.
    
    Args:
        number: The square number (1-64)
        
    Returns:
        The number of grains on that square
        
    Raises:
        ValueError: If square number is outside the valid range
        
    Purpose:
        This function corresponds to the first wheat/chessboard requirement.
        It needs to return 1 grain for square 1, 2 grains for square 2,
        4 grains for square 3, etc., following the pattern 2^(n-1).
    
    Notes:
    - Had to look up chaining comparisons (1 <= number <= 64)
    - Used 2 ** (number - 1) for exponentiation, had to remember Python uses ** not ^ (like in Excel)
    - Had to look up how to raise a custom ValueError with specific message
    """
    if not 1 <= number <= 64:  # Had to look up this syntax for chaining comparisons
        raise ValueError("square must be between 1 and 64")  # Had to look up how to raise a custom error
    number_of_grains = 1 * (2 ** (number - 1))  # Had to remember Python uses ** for exponents, not ^ like in Excel
    return number_of_grains


def total_initial():
    """
    Calculate the total number of grains on the chessboard.
    
    Returns:
        The sum of grains on all 64 squares
        
    Purpose:
        This function addresses the second part of the wheat/chessboard challenge.
        It needs to calculate the total number of grains across all squares,
        which is the sum of 2^0 + 2^1 + 2^2 + ... + 2^63.
        
    Notes:
    - Had to look up range-based for loop syntax
    - Uses a naive approach of summing each square's value
    - The expected result is 18,446,744,073,709,551,615 (which is 2^64 - 1)
    """
    total_grains = 0
    for square_number in range(1, 65):  # Had to look up the syntax for range-based loops
        total_grains += square_initial(square_number)
    return total_grains


#############################################
# Optimized solutions from Exercism
#############################################

# 1. Using bit-shifting (most efficient for single square)
def square_bitshift(number):
    """
    Calculate grains using bitwise left shift operation.
    
    Args:
        number: The square number (1-64)
        
    Returns:
        The number of grains on that square
        
    Purpose:
        Implements the same functionality as square_initial but uses
        bitwise operations for better performance.
        
    Notes:
        The operation 1 << n is equivalent to 2^n in binary.
        Example values:
        - square(1) = 1
        - square(2) = 2
        - square(3) = 4
        - square(16) = 32768
        - square(64) = 9223372036854775808
    """
    if number < 1 or number > 64:
        raise ValueError('square must be between 1 and 64')
    return 1 << number - 1


def total_bitshift():
    """
    Calculate total using bitwise left shift.
    
    Returns:
        The sum of grains on all 64 squares
        
    Purpose:
        More efficient implementation of the total function.
        
    Notes:
        The sum of powers of 2 from 0 to n-1 equals (2^n - 1).
        This is a mathematical property that allows us to calculate
        the answer in O(1) time instead of iterating through all squares.
        The expected result is 18,446,744,073,709,551,615.
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

Example values:
1. Basic functionality:
   - For square 1: 1 grain
   - For square 2: 2 grains
   - For square 3: 4 grains
   - For square 4: 8 grains
   - For square 16: 32,768 grains
   - For square 32: 2,147,483,648 grains
   - For square 64: 9,223,372,036,854,775,808 grains

2. Error handling:
   - square(0) should raise ValueError with message "square must be between 1 and 64"
   - square(-1) should raise ValueError with message "square must be between 1 and 64"
   - square(65) should raise ValueError with message "square must be between 1 and 64"

3. Total calculation:
   - total() should return 18,446,744,073,709,551,615
"""


#############################################
# Final optimized solution combining personal style with efficiency
#############################################

def square(number):
    """
    Calculate the number of grains on a specific square (optimized).
    
    Args:
        number: The square number (1-64)
        
    Returns:
        The number of grains on that square
        
    Raises:
        ValueError: If square number is outside the valid range
        
    Purpose:
        Final optimized implementation that combines readability with
        performance. This is the function that will be called by the test suite.
        
    Notes:
        Uses my preferred coding style with meaningful variable names
        combined with the more efficient bitshift operation.
    """
    if not 1 <= number <= 64:  # Using my preferred chaining comparison style
        raise ValueError("square must be between 1 and 64")
    number_of_grains = 1 << number - 1  # New learning: bitshift is more efficient than exponentiation
    return number_of_grains


def total():
    """
    Calculate the total number of grains on the chessboard (optimized).
    
    Returns:
        The sum of grains on all 64 squares
        
    Purpose:
        Final optimized implementation that will be called by the test suite.
        
    Notes:
        Uses the mathematical formula for sum of powers of 2 instead of looping.
        The formula 2^n - 1 gives us the sum of 2^0 + 2^1 + ... + 2^(n-1).
        This is a classic computer science optimization for this problem.
    """
    return 2 ** 64 - 1  # Direct formula is much more efficient than iteration