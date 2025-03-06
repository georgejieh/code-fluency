"""
Leap Year Calculator

Context:
This program determines whether a given year is a leap year according to the Gregorian calendar rules.
In the Gregorian calendar, leap years occur:
- In every year that is evenly divisible by 4
- Unless the year is evenly divisible by 100, in which case it's only a leap year if also evenly divisible by 400

This exercise demonstrates:
1. Boolean expressions and logical operators in Python
2. Handling mathematical rules with boolean logic
3. Different approaches to solving the same logical problem
4. Efficient expression of complex conditional logic

My Learning Process:
I initially approached this by thinking through the problem step by step, talking through 
the solution logic. I had to reason through the conditions carefully to ensure correct implementation
of the leap year rules. I explored different ways to structure the boolean expression before
settling on a concise solution using boolean chaining.
"""

def leap_year(year: int) -> bool:
    """
    Determine whether a given year is a leap year according to Gregorian calendar rules.
    
    Args:
        year: int - the year to check
        
    Returns:
        bool - True if the year is a leap year, False otherwise
        
    Purpose:
        Apply the Gregorian calendar leap year rules to determine if a given year is a leap year.
        
    Notes:
        Alternative implementations I considered:
        
        1. Using separate if-else statements:
            if year % 100 == 0:
                return year % 400 == 0
            return year % 4 == 0
            
        2. Using a ternary operator (as noted in the dig deeper lesson):
            return not year % 400 if not year % 100 else not year % 4
            
        The 'not' operator before modulo expressions is an alternative to '== 0' comparisons
        that I learned about but didn't initially use in my solution.
    """
    return (year % 100 == 0 and year % 400 == 0) or (year % 4 == 0 and year % 100 != 0)