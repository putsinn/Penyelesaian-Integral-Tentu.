# Import needed functions."
import numpy as np
from scipy import integrate
import matplotlib.pyplot as plotlib

# Define parameters.
x_start = 0
x_stop = 12
x_steps_interval = 0.01

# Define an array of data points.
x_values = np.arange(x_start, x_stop, x_steps_interval)
y_values = x_values**3*np.exp(x_values**4)

# Plot the function curve.
plotlib.plot(x_values, y_values)

# Define a lambda function for integration over x values.
integration_function = lambda x: 2 + np.sin(x)

# Calculate the integral.
integral, error = integrate.quad(integration_function, x_start, x_stop)

# Print the integration results.
print("Integral Value:")
print(integral)
print("Integration Error:")
print(error)

# Display the plot.
plotlib.xlabel('x')
plotlib.ylabel('y')
plotlib.show()
