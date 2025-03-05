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
- The modulo operator (`%`) came in handy for calculating remainders in `get_leftover_of_bills`
- I practiced converting between types using `int()` and `float()`

### Techniques I Used
- I had to look up the `round(value, decimal_places)` method as I couldn't remember the syntax for rounding
- I got to practice chaining comparisons (`1 <= number <= 64`) which made my code cleaner
- I had to remind myself that Python uses `**` for exponentiation instead of `^` (which I'm used to from Excel/Google Sheets) when calculating `2 ** (number - 1)` for the grains problem

### Python Syntax I Had To Review
- I needed to refresh my memory on the syntax for range-based for loops: `for square_number in range(1, 65):`
- I had to look up how to raise an error with a custom condition (`raise ValueError("message")`), which is different from my usual approach of using try/except blocks to catch exceptions

### Practical Applications
The exercises gave me real-world contexts for these operations:
- Currency exchange calculations with different rates and fees
- The classic wheat and chessboard problem showing exponential growth

## Skills I've Improved
- Breaking down mathematical problems into discrete functions
- Handling edge cases (like input validation in the grains problem)
- Working with financial calculations and appropriate rounding

## Exercises Completed So Far
1. Currency Exchange Calculator - which taught me about handling percentages and financial calculations
2. Grains/Chessboard Problem - which was great practice for working with exponential growth

## Key Takeaways
- I'm more comfortable now with when to use integer vs float operations
- I have a better understanding of how to handle division operations depending on whether I need decimals or whole numbers
- These fundamentals are essential building blocks for more complex numerical work in Python