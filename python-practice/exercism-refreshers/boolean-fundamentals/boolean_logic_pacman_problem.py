"""
Pac-Man Game Logic Implementation

Context:
This script implements the core boolean logic for the classic arcade game Pac-Man.
It models key game mechanics using boolean operations to determine game states
such as when Pac-Man can eat ghosts, score points, lose, or win the game.

This exercise demonstrates:
1. Boolean operations (and, or, not) in Python
2. Function composition where one function uses another
3. Writing clean, simplified boolean expressions
4. Modeling game rules with boolean logic

The challenge required implementing four core functions for the game:
- eat_ghost(): Determine if Pac-Man can eat a ghost
- score(): Check if Pac-Man scores points
- lose(): Detect if Pac-Man loses
- win(): Determine if Pac-Man wins the game

My Learning Process:
During development, I encountered several pylint warnings that taught me important Python concepts:

1. Simplifiable if-statements (R1703) - I learned to eliminate redundant conditional 
   structures and directly return boolean expressions. For example, replacing:
   ```
   if condition:
       return True
   else:
       return False
   ```
   with the cleaner:
   ```
   return condition
   ```

2. Unnecessary else after return (R1705) - I discovered that when a return statement 
   is inside an if block, the else becomes redundant since the function would already 
   have exited if the if condition was true.

3. Singleton comparisons with True/False (C0121) - I learned it's not Pythonic to 
   compare variables directly to True/False using operators. Instead, we should leverage 
   the boolean value directly.

4. My initial versions of these functions had if/else statements, but I progressively 
   refactored them to the cleaner, more direct boolean expressions shown in this 
   final version.
"""


def eat_ghost(power_pellet_active, touching_ghost):
    """
    Determine if Pac-Man can eat a ghost.
    
    Args:
        power_pellet_active: bool - does the player have an active power pellet?
        touching_ghost: bool - is the player touching a ghost?
        
    Returns:
        bool - can the ghost be eaten?
        
    Purpose:
        Determine if Pac-Man can eat a ghost. A ghost can only be eaten
        if Pac-Man has an active power pellet AND is touching the ghost.
    
    Notes:
        Direct boolean expression eliminates the need for if/else statements.
        My initial implementation was more verbose:
        
        ```
        if power_pellet_active and touching_ghost:
            return True
        else:
            return False
        ```
        
        The pylint error R1703 (simplifiable-if-statement) helped me realize
        I could simplify this pattern tremendously.
    
    Examples:
        eat_ghost(False, True) -> False
        eat_ghost(True, False) -> False
        eat_ghost(True, True) -> True
    """
    # Had to wrap my mind around the idea that since comparison operators
    # directly output a boolean value, I don't need to use if/else statements
    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    """
    Check if Pac-Man scores points.
    
    Args:
        touching_power_pellet: bool - is the player touching a power pellet?
        touching_dot: bool - is the player touching a dot?
        
    Returns:
        bool - has the player scored points?
        
    Purpose:
        Determine if Pac-Man scores points. Points are scored
        if Pac-Man touches EITHER a power pellet OR a dot.
    
    Examples:
        score(False, False) -> False
        score(False, True) -> True
        score(True, False) -> True
        score(True, True) -> True
    """
    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    """
    Check if Pac-Man loses the game.
    
    Args:
        power_pellet_active: bool - does the player have an active power pellet?
        touching_ghost: bool - is the player touching a ghost?
        
    Returns:
        bool - has the player lost the game?
        
    Purpose:
        Determine if Pac-Man loses the game. The game is lost if
        Pac-Man touches a ghost WITHOUT having an active power pellet.
    
    Examples:
        lose(True, False) -> False
        lose(True, True) -> False
        lose(False, True) -> True
        lose(False, False) -> False
    """
    return not power_pellet_active and touching_ghost


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """
    Check if Pac-Man wins the game.
    
    Args:
        has_eaten_all_dots: bool - has the player eaten all dots?
        power_pellet_active: bool - does the player have an active power pellet?
        touching_ghost: bool - is the player touching a ghost?
        
    Returns:
        bool - has the player won the game?
        
    Purpose:
        Determine if Pac-Man wins the game. The game is won if
        Pac-Man has eaten all dots AND has not lost the game
        (by touching a ghost without an active power pellet).
    
    Notes:
        This function reuses the lose() function to avoid duplicating logic.
        
        I initially wrote this with nested if-statements:
        ```
        if has_eaten_all_dots:
            if lose(power_pellet_active, touching_ghost):
                return False
            else:
                return True
        else:
            return False
        ```
        
        The pylint error R1705 (unnecessary-else-after-return) helped me 
        realize I could simplify this pattern. Also, I learned about function 
        composition - using one function inside another to build more complex logic
        while keeping the code clean.
    
    Examples:
        win(True, False, True) -> False
        win(False, True, True) -> False
        win(True, True, True) -> True
        win(True, False, False) -> True
    """
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)