# Python Numbers Fundamentals

This directory contains my exercises focused on refreshing my knowledge of working with numbers in Python.

## What I've Learned

### Number Types Refresher
Working through these exercises helped me revisit the two main number types in Python:
- **Integers (int)**: I was reminded that Python integers have arbitrary precision, meaning they can be as large as needed (limited only by my system's memory)
- **Floats**: I recalled that floats in Python can sometimes have precision issues - a good reminder of why we need to be careful with financial calculations

### Operations I Refreshed On
- I got to practice using the standard arithmetic operators (`+`, `-`, `*`, `/`)
- I had to look up the floor division operator (`//`) for the `get_number_of_bills` function, which was helpful for getting whole number results
- The modulo operator (`%`) came in handy for calculating remainders in `get_leftover_of_bills` and checking for even/odd numbers
- I practiced converting between types using `int()` and `float()`
- The `+=` operator was an important reminder - I initially wrote it incorrectly as `=+` in the Armstrong number exercise

### New Operations I Learned
- **Bitwise operators**: I discovered how to use the left shift operator (`<<`) for efficient exponential calculations
  - `1 << n` is equivalent to `2 ** n` but executes at the bit level, which is more efficient
  - The formula `(1 << 64) - 1` efficiently calculates the sum of all powers of 2 from 2⁰ to 2⁶³
- **Ternary operator**: I learned about using Python's ternary operator syntax: `value_if_true if condition else value_if_false` as a more concise alternative to if/else statements

### Control Flow Techniques I Used
- I had to look up the `round(value, decimal_places)` method as I couldn't remember the syntax for rounding
- I got to practice chaining comparisons (`1 <= number <= 64`) which made my code cleaner
- I had to remind myself that Python uses `**` for exponentiation instead of `^` (which I'm used to from Excel/Google Sheets) when calculating `2 ** (number - 1)` for the grains problem
- I had to look up the syntax for "while" loops, as I was more familiar with "for" loops
- I explored different approaches for solving problems: if/else statements, ternary operators, and recursion

### Python Syntax I Had To Review
- I needed to refresh my memory on the syntax for range-based for loops: `for square_number in range(1, 65):`
- I had to look up how to raise an error with a custom condition (`raise ValueError("message")`), which is different from my usual approach of using try/except blocks to catch exceptions
- I practiced using function type hints and signatures (`def steps(number: int) -> int:`) and learned this is considered best practice in production environments

### Algorithm Patterns
- I learned about handling exponential calculations via different methods (exponentiation vs. bitwise operations)
- I implemented the Collatz Conjecture algorithm using various approaches and understood their performance differences
- I practiced working with digit-based calculations in the Armstrong number exercise

### Practical Applications
The exercises gave me real-world contexts for these operations:
- Currency exchange calculations with different rates and fees
- The classic wheat and chessboard problem showing exponential growth
- Mathematical sequences and conjectures (Collatz)
- Number validation and classification (Armstrong numbers)

## Skills I've Improved
- Breaking down mathematical problems into discrete functions
- Handling edge cases (like input validation in the grains problem)
- Working with financial calculations and appropriate rounding
- Implementing multiple solutions to the same problem and evaluating their efficiency
- Using more elegant and efficient code constructs like ternary operators where appropriate

## Exercises Completed So Far
1. Currency Exchange Calculator - which taught me about handling percentages and financial calculations
2. Grains/Chessboard Problem - which was great practice for working with exponential growth
3. Armstrong Numbers - which helped me practice working with digits and powers
4. Collatz Conjecture - which taught me about implementing algorithms with different approaches (if/else, ternary, recursion)

## Key Takeaways
- I'm more comfortable now with when to use integer vs float operations
- I have a better understanding of how to handle division operations depending on whether I need decimals or whole numbers
- These fundamentals are essential building blocks for more complex numerical work in Python
- I've learned about code style preferences (ternary operators for simple conditions, function type hints)
- I better understand the performance implications of different approaches (recursion vs. iteration, if/else vs. ternary)