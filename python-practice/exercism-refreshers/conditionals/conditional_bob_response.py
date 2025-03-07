"""
Bob Response System - Conditional Exercise

Context:
This program simulates conversing with Bob, a lackadaisical teenager with limited responses.
Bob has very specific response patterns based on how you talk to him, requiring
multiple conditional checks to determine the appropriate response.

This exercise demonstrates:
1. String processing and pattern recognition
2. Multiple conditional branches with specific string checks
3. Prioritizing conditions to handle overlapping cases
4. Use of Python string methods for clean condition checking

Learning process:
- Needed to look up the isupper() method for checking all-caps statements
- Needed to look up the isspace() method for checking whitespace-only inputs
- Learned to check conditions from most complex to least complex when there are overlapping conditions
- Realized that conditions that could cause syntax errors must be checked first
- Experimented with flattening conditionals for readability
"""

def response(hey_bob: str) -> str:
    """
    Determine how Bob responds to someone based on the input text pattern.
    
    Args:
        hey_bob: str - The text someone says to Bob
        
    Returns:
        str - Bob's response based on the pattern of the input
        
    Purpose:
        Analyze the input text and return one of five possible responses:
        - "Sure." - If someone asks Bob a question (ends with ?)
        - "Whoa, chill out!" - If someone yells at Bob (ALL CAPS)
        - "Calm down, I know what I'm doing!" - If someone yells a question at Bob
        - "Fine. Be that way!" - If someone says nothing (empty or whitespace)
        - "Whatever." - Any other case
        
    Evolution:
        Initially implemented with separate condition checks, then learned
        to organize from most specific/complex conditions to most general.
    """
    # Remove trailing whitespace first
    hey_bob = hey_bob.rstrip()  # Using rstrip() instead of strip() to only remove trailing whitespace
    
    # Check for silence (empty string)
    if not hey_bob:
        return "Fine. Be that way!"
    
    # Check for yelling (uppercase)
    if hey_bob.isupper():  # Had to look up isupper() method
        # Nested check for yelled questions
        if hey_bob.endswith('?'):  # Using endswith() method instead of checking last character
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"
    
    # Check for questions (end with ?)
    if hey_bob.endswith('?'):
        return "Sure."
    
    # Default response for everything else
    return "Whatever."
