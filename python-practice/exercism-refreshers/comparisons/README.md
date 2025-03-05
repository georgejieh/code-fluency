# Python Comparisons Fundamentals

This directory contains my exercises focused on refreshing my knowledge of comparison operators and conditionals in Python.

## What I've Learned

### Comparison Operations Refresher
Working through these exercises helped me revisit the comparison operators in Python:
- I practiced using equality and inequality operators (`==`, `!=`)
- I got to implement value comparison operators (`>`, `<`, `>=`, `<=`)
- I used identity operators (`is`, `is not`) to check if variables reference the same object

### Logical Operators and Techniques
- I practiced using the logical `or` operator for alternative conditions
- I learned a new syntax for checking if a value is in a collection: `value in (item1, item2)` instead of the lengthier `value == item1 or value == item2`
- I practiced returning early from functions instead of using complex if-else chains

### Membership and Containment Operations
- I practiced using the `in` operator to check for item presence in tuples
- I used membership testing for streamlining comparison logic in functions

### Chaining Comparisons
- I got to refresh my understanding of chained comparisons like `9 <= x <= 11` which reads naturally like mathematical notation
- I practiced using comparison chaining to make my code more readable and concise

### Tuple Return Values
- I practiced returning multiple items as a tuple when appropriate (when cards were equal in value)
- I refreshed my memory on the syntax for returning multiple values using a comma in the return statement

### Function Design Patterns
- I practiced writing clear, focused functions with a single responsibility
- I used function composition, where one function calls another, to avoid duplicating logic
- I implemented helper functions that can be reused across multiple game features

## Exercises Completed
1. Blackjack Card Value System - which required implementing multiple comparison operations for:
   - Determining card values
   - Comparing card values
   - Checking for special game conditions like "blackjack", "split pairs", and "double down"

## Key Takeaways
- I'm more comfortable now with alternative syntax for common operations (like using `in` with a tuple of values)
- I have a better understanding of when to return early from functions instead of using complex conditionals
- These comparison fundamentals provide a solid foundation for implementing game logic and other conditional structures in Python