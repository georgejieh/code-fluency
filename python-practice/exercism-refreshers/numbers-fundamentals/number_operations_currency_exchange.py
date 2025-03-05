"""
Currency Exchange Calculator

Context:
This program helps a traveler (Chandler) calculate various aspects of currency exchange
for international travel. It handles common currency conversion operations like:
- Converting between currencies at a given exchange rate
- Calculating remaining money after an exchange
- Working with different denominations of bills
- Accounting for exchange fees/spread

This exercise demonstrates:
1. Basic arithmetic operations in Python
2. Working with floats and integers
3. Using floor division and modulo for calculating with denominations
4. Handling percentage calculations
5. Rounding for financial applications
"""

def exchange_money(budget, exchange_rate):
    """
    Calculate how much foreign currency you get for your money.
    
    Args:
        budget: float - amount of money you are planning to exchange
        exchange_rate: float - unit value of the foreign currency
        
    Returns:
        float - exchanged value of the foreign currency you can receive
        
    Purpose:
        Convert your starting currency to a foreign currency based on
        the exchange rate (how much of your currency equals one unit of foreign currency).
        
    Notes:
        Had to look up the round() method to handle decimal precision.
        
    Examples:
        exchange_money(127.5, 1.2) would return 106.25
        exchange_money(100000, 0.8) would return 125000
    """
    foreign_currency_amount = round(budget / exchange_rate, 2)  # Had to look up the round() method
    return foreign_currency_amount


def get_change(budget, exchanging_value):
    """
    Calculate the amount of money left after exchanging some of it.
    
    Args:
        budget: float - amount of money you own
        exchanging_value: float - amount of your money you want to exchange now
        
    Returns:
        float - amount left of your starting currency after exchanging
        
    Purpose:
        Figure out how much of your original currency remains after
        you've exchanged a portion of it.
        
    Examples:
        get_change(127.5, 120) would return 7.5
        get_change(463000, 5000) would return 458000
    """
    change = budget - exchanging_value
    return change


def get_value_of_bills(denomination, number_of_bills):
    """
    Calculate the total value of bills of a specific denomination.
    
    Args:
        denomination: int - the value of a single bill
        number_of_bills: int - total number of bills
        
    Returns:
        int - calculated value of the bills
        
    Purpose:
        Calculate the total value when you have multiple bills of
        the same denomination (e.g., how much is 128 five-dollar bills worth).
        
    Examples:
        get_value_of_bills(5, 128) would return 640
        get_value_of_bills(10000, 128) would return 1280000
    """
    value_of_bills = denomination * number_of_bills
    return value_of_bills


def get_number_of_bills(amount, denomination):
    """
    Calculate how many whole bills of a certain denomination you can get.
    
    Args:
        amount: float - the total starting value
        denomination: int - the value of a single bill
        
    Returns:
        int - number of bills that can be obtained from the amount
        
    Purpose:
        Determine how many whole bills of a certain value you can receive
        when exchanging your money (ignoring any remainder/fractional amounts).
        
    Notes:
        Had to look up the floor division operator (//) which divides and
        rounds down to the nearest whole number.
        
    Examples:
        get_number_of_bills(127.5, 5) would return 25
        get_number_of_bills(163270, 50000) would return 3
    """
    number_of_bills = amount // denomination  # Had to look up the floor division operator
    return number_of_bills


def get_leftover_of_bills(amount, denomination):
    """
    Calculate the amount that cannot be returned in whole bills.
    
    Args:
        amount: float - the total starting value
        denomination: int - the value of a single bill
        
    Returns:
        float - the amount that is "leftover", given the current denomination
        
    Purpose:
        Find out how much money would be left over after getting the
        maximum number of whole bills of a specific denomination.
        
    Examples:
        get_leftover_of_bills(127.5, 20) would return 7.5
        get_leftover_of_bills(10.1, 10) would return 0.1
    """
    left_over_bills = amount % denomination
    return left_over_bills


def exchangeable_value(budget, exchange_rate, spread, denomination):
    """
    Calculate maximum value in foreign currency accounting for fees and bill denominations.
    
    Args:
        budget: float - the amount of your money you are planning to exchange
        exchange_rate: float - the unit value of the foreign currency
        spread: int - percentage that is taken as an exchange fee
        denomination: int - the value of a single bill
        
    Returns:
        int - maximum value you can get
        
    Purpose:
        Calculate the maximum amount of foreign currency you can get,
        taking into account both the exchange fee (spread) and the
        constraint that you can only receive whole bills of a specific denomination.
        
    Notes:
        This combines multiple concepts: percentage calculation,
        exchange rate with fee, and whole bill denomination constraints.
        
    Examples:
        exchangeable_value(127.25, 1.20, 10, 20) would return 80
        exchangeable_value(127.25, 1.20, 10, 5) would return 95
    """
    percentage_spread = spread / 100
    rate_with_spread = exchange_rate * (1 + percentage_spread)
    total_foreign_currency = budget / rate_with_spread
    number_of_bills = total_foreign_currency // denomination
    max_value = number_of_bills * denomination
    return max_value