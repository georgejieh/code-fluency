"""
Nuclear Reactor Control System - Conditional Logic Exercise

Context:
This script implements a control system for a nuclear reactor using conditional statements.
The exercise demonstrates how boolean logic and conditionals can be applied in safety-critical
systems to ensure proper reactor operation and prevent dangerous conditions.

This exercise demonstrates:
1. Boolean expressions and compound conditions
2. Multiple branching logic patterns 
3. Threshold-based categorization
4. Practical application of numerical comparisons
5. Evolution of code styles from verbose to concise

Learning Focus:
- Refreshing Python conditional statements (if/elif/else)
- Practice with boolean expressions and comparison operators
- Demonstrating "flat is better than nested" principle
- Evolution of code from standard if/elif/else to cleaner early-return pattern

Author's Notes:
This exercise helped me refresh my understanding of Python conditionals and
boolean expressions. I was able to practice and improve my code by moving from
traditional if/elif/else patterns to cleaner structures with early returns, which
reduced indentation and improved readability.
"""


def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify if reactor criticality is balanced within safe parameters.

    Args:
        temperature: int or float - temperature value in kelvin.
        neutrons_emitted: int or float - number of neutrons emitted per second.

    Returns:
        bool - True if criticality is balanced, False otherwise.

    Purpose:
        Determines if a reactor is in a state of criticality by checking multiple
        safety conditions simultaneously. All conditions must be met for criticality
        to be considered balanced.
        
    Notes:
        The boolean expression directly returns the result of the compound condition,
        demonstrating that explicit True/False returns aren't necessary when the
        expression itself evaluates to a boolean.

    Examples:
        >>> is_criticality_balanced(750, 650)
        True
        >>> is_criticality_balanced(800, 500)
        False
    """
    return (temperature < 800 and
           neutrons_emitted > 500 and
           temperature * neutrons_emitted < 500000)


def reactor_efficiency(voltage, current, theoretical_max_power):
    """Assess the reactor's efficiency level and categorize it into color-coded bands.

    Args:
        voltage: int or float - voltage value.
        current: int or float - current value.
        theoretical_max_power: int or float - power that corresponds to 100% efficiency.

    Returns:
        str - efficiency band: 'green', 'orange', 'red', or 'black'.

    Purpose:
        Calculates the reactor's efficiency as a percentage of theoretical maximum
        and categorizes it into one of four bands for quick assessment.
        
    Notes:
        This function demonstrates the evolution of my code style. Initially implemented
        with if/elif/else, I refactored to use early returns which flattened the structure.
        This takes advantage of the fact that Python evaluates conditions sequentially,
        so we don't need to specify ranges that were already excluded by previous conditions.
        
        Initial implementation:
        ```python
        if efficiency >= 80:
            return 'green'
        elif efficiency >= 60:
            return 'orange'
        elif efficiency >= 30:
            return 'red'
        else:
            return 'black'
        ```

    Examples:
        >>> reactor_efficiency(10, 1000, 10000)  # 100% efficiency
        'green'
        >>> reactor_efficiency(10, 700, 10000)   # 70% efficiency
        'orange'
        >>> reactor_efficiency(10, 400, 10000)   # 40% efficiency
        'red'
        >>> reactor_efficiency(10, 200, 10000)   # 20% efficiency
        'black'
    """
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100
    
    # Early returns create a flatter structure than if/elif/else
    if efficiency >= 80:
        return 'green'
    if efficiency >= 60:
        return 'orange'
    if efficiency >= 30:
        return 'red'
    return 'black'


def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Assess reactor status and return appropriate safety action code.

    Args:
        temperature: int or float - value of the temperature in kelvin.
        neutrons_produced_per_second: int or float - neutron flux.
        threshold: int or float - threshold for safety categories.

    Returns:
        str - one of ('LOW', 'NORMAL', 'DANGER') indicating required action.

    Purpose:
        Determines the reactor's status based on the thermal neutron production rate
        relative to a threshold value. This helps operators quickly identify if
        control rods should be adjusted or emergency procedures activated.
        
    Notes:
        Uses chained comparison syntax (a <= b <= c) which is a Python-specific feature
        that provides a more readable way to express range comparisons. This initially
        triggered a Pylint warning (R1716) that led me to learn more about this feature.

    Examples:
        >>> fail_safe(10, 1000, 10000)  # 10000 threshold, actual: 10000
        'NORMAL'
        >>> fail_safe(10, 700, 10000)   # 10000 threshold, actual: 7000
        'LOW'
        >>> fail_safe(10, 1200, 10000)  # 10000 threshold, actual: 12000
        'DANGER'
    """
    thermal_neutron_production_rate = temperature * neutrons_produced_per_second
    upper_threshold = threshold * 1.1
    lower_threshold = threshold * 0.9
    
    # Chained comparison is more readable than separate AND conditions
    if lower_threshold <= thermal_neutron_production_rate <= upper_threshold:
        return 'NORMAL'
    if thermal_neutron_production_rate < lower_threshold:
        return 'LOW'
    return 'DANGER'