"""
Blackjack Game Logic Implementation

Context:
This script implements the core logic for evaluating Blackjack card hands.
It handles card valuation, comparisons, and determines when special game
conditions like blackjack, splitting pairs, or doubling down are possible.

This exercise demonstrates:
1. Using comparison operators in Python
2. Implementing game rule conditionals 
3. Returning multiple values as tuples
4. Using membership testing with the 'in' operator
5. Short-circuiting conditions with logical operators
6. Function composition for code reuse

Resources:
- How to play blackjack: https://bicyclecards.com/how-to-play/blackjack/
- Standard playing cards: https://en.wikipedia.org/wiki/Standard_52-card_deck
"""


def value_of_card(card):
    """
    Determine the scoring value of a card.
    
    Args:
        card: str - given card.
        
    Returns:
        int - value of a given card according to Blackjack rules.
        
    Purpose:
        Convert card representations to their numerical values for scoring.
        Face cards (J, Q, K) are worth 10, Ace is worth 1 by default,
        and number cards are worth their numerical value.
        
    Notes:
        This function handles the basic card valuation, while the ace's
        variable value (1 or 11) is determined in a separate function.
    """
    if card in ('J', 'Q', 'K'):
        return 10
    if card == 'A':
        return 1
    return int(card)


def higher_card(card_one, card_two):
    """
    Determine which card has a higher value in the hand.
    
    Args:
        card_one: str - first card in hand
        card_two: str - second card in hand
        
    Returns:
        str or tuple - the higher card, or a tuple of both cards if equal value
        
    Purpose:
        Compare two cards and determine which has the higher value.
        If both cards have equal value, return both cards as a tuple.
        
    Notes:
        Uses the value_of_card function to avoid duplicating valuation logic.
        When cards are equal, returns a tuple using the comma syntax in the return statement.
    """
    if value_of_card(card_one) > value_of_card(card_two):
        return card_one
    if value_of_card(card_one) < value_of_card(card_two):
        return card_two
    return card_one, card_two


def value_of_ace(card_one, card_two):
    """
    Calculate the most advantageous value for the ace card.
    
    Args:
        card_one: str - first card in hand
        card_two: str - second card in hand
        
    Returns:
        int - either 1 or 11 as the optimal value for an ace
        
    Purpose:
        Determine whether an ace should be counted as 1 or 11 based on
        the other cards in hand, maximizing the total without exceeding 21.
        
    Notes:
        Uses the 'in' operator with a tuple to check if either card is an ace:
        'A' in (card_one, card_two) - this was a new syntax I learned.
    """
    if 'A' in (card_one, card_two):  # New syntax I learned instead of card_one == 'A' or card_two == 'A'
        return 1
    if (value_of_card(card_one) + value_of_card(card_two)) > 10:
        return 1
    return 11


def is_blackjack(card_one, card_two):
    """
    Determine if the hand is a 'natural' or 'blackjack'.
    
    Args:
        card_one: str - first card in hand
        card_two: str - second card in hand
        
    Returns:
        bool - whether the hand constitutes a blackjack
        
    Purpose:
        Check if the initial two-card hand forms a blackjack,
        which requires an ace and a 10-value card (10, J, Q, K).
        
    Notes:
        Uses a combination of conditions with logical operators to determine
        if the hand contains both an ace and a 10-value card.
    """
    return (value_of_card(card_one) == 10 or value_of_card(card_two) == 10) and (card_one == 'A' or card_two == 'A')


def can_split_pairs(card_one, card_two):
    """
    Determine if a player can split their hand into two hands.
    
    Args:
        card_one: str - first card in hand
        card_two: str - second card in hand
        
    Returns:
        bool - whether the hand can be split
        
    Purpose:
        Check if the two cards have equal value, which allows
        the player to split them into two separate hands.
        
    Notes:
        Uses the value_of_card function to determine if both cards
        have the same value, regardless of their face representation.
    """
    return value_of_card(card_one) == value_of_card(card_two)


def can_double_down(card_one, card_two):
    """
    Determine if a blackjack player can place a double down bet.
    
    Args:
        card_one: str - first card in hand
        card_two: str - second card in hand
        
    Returns:
        bool - whether the player can double down
        
    Purpose:
        Check if the initial two-card hand has a total value of 9, 10, or 11,
        which allows the player to double their bet.
        
    Notes:
        Uses chained comparison (9 <= x <= 11) to check if the total is
        between 9 and 11 inclusive.
    """
    return 9 <= (value_of_card(card_one) + value_of_card(card_two)) <= 11