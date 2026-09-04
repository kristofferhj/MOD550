import matplotlib.pyplot as plt

from tools import fridge_management, total_power_usage

# Temperature measurements
temperatures = [3,4,5,6,9,7,4,3,6,8]

# Door open/closed
# True = open
# False = closed
door_states = [
    False,
    False,
    True,
    False,
    False,
    False,
    True,
    False,
    False,
    False
]


power_values = []

for temperature, door_open in zip(temperatures, door_states):
    power = fridge_management(temperature, door_open)
    power_values.append(power)


# Cumulative power usage
cumulative_power = []

running_total = 0

for power in power_values:
    running_total += power
    cumulative_power.append(running_total)


# Calculate total power usage
total_power = total_power_usage(power_values)


print(f"Temperatures: {temperatures}")
print(f"Door states: {door_states}")
print(f"Instantaneous power usage: {power_values}")
print(f"Total power used: {total_power}")


# Create time values
time = list(range(len(power_values)))


# Plot instantaneous power usage
plt.plot(time,power_values,marker="o",label="Instantaneous power")

# Plot cumulative power usage
plt.plot(time,cumulative_power,marker="o",label="Cumulative power"
)

plt.xlabel("Time")
plt.ylabel("Power usage")
plt.title("Fridge Power Usage")
plt.legend()
plt.grid()

plt.show()