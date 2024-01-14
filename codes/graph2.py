import numpy as np
import matplotlib.pyplot as plt

# Define the formula
def impedance(omega):
    return 110 / np.sqrt(1600 + (1e8 / omega**2))

# Generate values for omega
omega_values = np.linspace(1, 1000, 1000)

# Calculate corresponding impedance values
impedance_values = impedance(omega_values)

# Plot the graph
plt.figure(figsize=(8, 6))
plt.plot(omega_values, impedance_values, label=r'$\frac{110}{\sqrt{1600 + \frac{10^8}{\omega^2}}}$')
plt.title('Current vs $\omega$')
plt.xlabel('$\omega$')
plt.ylabel('$|I(j\omega)|$')
plt.grid(True)
plt.legend()
plt.show()
