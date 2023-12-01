import matplotlib.pyplot as plt

# Example data (replace with your relay's data)
current_values     = [0,  1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]  # Current in Amperes
time_values_curve1 = [0.1, 0.2, 0.5, 1, 2, 5, 10, 20, 50, 100, 200]  # Time in seconds for Curve 1
time_values_curve2 = [0.2, 0.4, 1, 2, 4, 10, 20, 40, 100, 200, 400]  # Time in seconds for Curve 2

# Plotting
plt.semilogx(current_values, time_values_curve1, label='Curve 1')
plt.semilogx(current_values, time_values_curve2, label='Curve 2')

# Add labels and title
plt.xlabel('Current (A)')
plt.ylabel('Time (s)')
plt.title('Time-Current Characteristic Curve')

# Add legend
plt.legend()

# Show the plot
plt.grid(True)
plt.show()
