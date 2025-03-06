"""
Collatz Conjecture Calculator

Context:
The Collatz Conjecture is a famous mathematical conjecture that remains unproven.
It states that for any positive integer, applying a specific sequence of operations
will always eventually reach the number 1.

The operations are:
- If the number is even, divide it by 2
- If the number is odd, multiply it by 3 and add 1
- Repeat until you reach 1

This exercise demonstrates:
1. Implementing a mathematical algorithm with conditional logic
2. Working with control flow (loops and conditionals)
3. Error handling with custom exceptions
4. Exploring different implementation approaches (iterative vs. recursive)
5. Optimizing code for readability and performance
"""

def steps(number: int) -> int:
    """
    Calculate the number of steps to reach 1 using the Collatz Conjecture algorithm.
    
    Args:
        number: int - the starting positive integer
        
    Returns:
        int - the number of steps required to reach 1
        
    Raises:
        ValueError: If the input is not a positive integer
        
    Purpose:
        Determine how many iterations of the Collatz Conjecture operations
        are required for a given starting number to reach 1.
        
    Notes:
        This implementation uses the ternary operator approach, which I found
        to be more concise than if/else blocks while still maintaining readability.
        The if/else approach is slightly faster in benchmarks, but the ternary
        operator is preferred by style guides for simple conditions like this.
        
        I had to look up while loop syntax as I was more familiar with for loops,
        and I learned about using function type hints (number: int) -> int, which
        is considered best practice in production environments.
        
    Alternative Approaches:
        
        1. Using if/else statements (fastest in benchmarks):
        ```
        def steps(number: int) -> int:
            if number <= 0:
                raise ValueError("Only positive integers are allowed")
            step_number = 0
            while number > 1:
                if number % 2 == 0:
                    number /= 2
                else:
                    number = number * 3 + 1
                step_number += 1
            return step_number
        ```
        
        2. Using recursion (elegant but limited by Python's recursion depth of 1000):
        ```
        def steps(number: int) -> int:
            if number <= 0:
                raise ValueError("Only positive integers are allowed")
            if number == 1:
                return 0
            number = number / 2 if number % 2 == 0 else number * 3 + 1
            return 1 + steps(number)
        ```
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")
    
    step_number = 0
    while number > 1:  # Had to look up while loop syntax
        number = number / 2 if number % 2 == 0 else number * 3 + 1  # Ternary operator for conciseness
        step_number += 1
    
    return step_number