"""
Triangle Classification

Context:
This program classifies triangles into three types based on their side lengths:
- Equilateral: All three sides have equal length
- Isosceles: At least two sides have equal length
- Scalene: All sides have different lengths

For a shape to be a valid triangle, it must satisfy certain constraints:
- All sides must have length > 0
- The sum of the lengths of any two sides must be greater than the length of the third side

This exercise demonstrates:
1. Boolean expressions for geometric validation
2. Breaking down complex logic into separate boolean checks
3. Using boolean operators to combine validation rules
4. Multiple approaches to structuring boolean logic for readability

My Learning Process:
I initially created a more verbose implementation with nested functions, but then
learned I could use tuple unpacking (a, b, c = sides) to make the code more concise
while still maintaining readability. I focused on writing code that would be
understandable even to people with minimal programming knowledge.
"""

def equilateral(sides: list[int]) -> bool:
    """
    Determine if a triangle is equilateral (all three sides of equal length).
    
    Args:
        sides: list[int] - a list of three side lengths
        
    Returns:
        bool - True if the triangle is equilateral, False otherwise
        
    Purpose:
        Check if a triangle with the given side lengths is both valid and equilateral.
        
    Notes:
        I could have used a nested function for triangle validation, but decided
        to use separate boolean variables for improved readability.
        
        Initial attempt with nested function:
        
        def equilateral(sides: list[int]) -> bool:
            a = sides[0]
            b = sides[1]
            c = sides[2]
            def istriange(a: int, b: int, c: int) -> bool:
                return a > 0 and b > 0 and c > 0 and a + b >= c and b + c >= a and a + c >= b
            return istriange(a, b, c) and a == b == c
    """
    a, b, c = sides  # Using tuple unpacking to assign list elements to individual variables
    is_valid = len(sides) == 3 and a > 0 and b > 0 and c > 0 and a + b > c and b + c > a and a + c > b
    is_equilateral = a == b == c
    return is_valid and is_equilateral


def isosceles(sides: list[int]) -> bool:
    """
    Determine if a triangle is isosceles (at least two sides of equal length).
    
    Args:
        sides: list[int] - a list of three side lengths
        
    Returns:
        bool - True if the triangle is isosceles, False otherwise
        
    Purpose:
        Check if a triangle with the given side lengths is both valid and isosceles.
        
    Notes:
        An equilateral triangle is also considered isosceles since all its sides are equal.
    """
    a, b, c = sides
    is_valid = len(sides) == 3 and a > 0 and b > 0 and c > 0 and a + b > c and b + c > a and a + c > b
    is_isosceles = a == b or a == c or b == c or a == b == c
    return is_valid and is_isosceles


def scalene(sides: list[int]) -> bool:
    """
    Determine if a triangle is scalene (all sides of different lengths).
    
    Args:
        sides: list[int] - a list of three side lengths
        
    Returns:
        bool - True if the triangle is scalene, False otherwise
        
    Purpose:
        Check if a triangle with the given side lengths is both valid and scalene.
    """
    a, b, c = sides
    is_valid = len(sides) == 3 and a > 0 and b > 0 and c > 0 and a + b > c and b + c > a and a + c > b
    is_scalene = a != b and b != c and a != c
    return is_valid and is_scalene