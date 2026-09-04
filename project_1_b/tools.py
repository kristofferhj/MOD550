def fridge_management(temperature, door_open):
    """
    Determine the instantaneous power usage of the fridge.

    Assumptions:
    - Level 0 means no cooling power.
    - Level 1 means low cooling power.
    - Level 2 means medium cooling power.
    - Level 3 means high cooling power.
    - If the fridge door is open, the fridge uses level 3.
    - If the door is closed:
        temperature <= 3 degrees C -> power level 0
        temperature > 3 and <= 5 degrees C -> power level 1
        temperature > 5 and <= 8 degrees C -> power level 2
        temperature > 8 degrees C -> power level 3

    Args:
        temperature (float): Current fridge temperature in degrees Celsius.
        door_open (bool): True if the fridge door is open,
                          False if the fridge door is closed.

    Returns:
        int: Power usage level from 0 to 3.
    """
    if door_open:
        return 3

    if temperature <= 3:
        return 0

    if temperature <= 5:
        return 1

    if temperature <= 8:
        return 2

    return 3


def total_power_usage(power_values):
    """
    Args:
        power_values: List of instantaneous power usage values.

    Returns:
        Sum of all power usage values.
    """
    return sum(power_values)