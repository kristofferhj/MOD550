from tools import fridge_management, total_power_usage


def test_fridge_management():
    """Test the fridge power level"""

    assert fridge_management(2, False) == 0
    assert fridge_management(3, False) == 0

    assert fridge_management(4, False) == 1
    assert fridge_management(5, False) == 1

    assert fridge_management(6, False) == 2
    assert fridge_management(8, False) == 2

    assert fridge_management(9, False) == 3

    assert fridge_management(2, True) == 3
    assert fridge_management(5, True) == 3


def test_total_power_usage():
    """Test thetotal power usage."""

    power_values = [0, 1, 3, 2, 3]

    result = total_power_usage(power_values)

    assert result == 9


if __name__ == "__main__":
    test_fridge_management()
    test_total_power_usage()

    print("All tests passed!")