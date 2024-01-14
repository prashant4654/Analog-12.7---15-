import numpy as np
import matplotlib.pyplot as plt
from matplotlib import rc

# Define the frequency range
omega = np.linspace(1, 100, 1000)

# Define the magnitude response function |H(jω)|
H_jomega = np.sqrt((1600 + 1e8) / omega**2)

# Set up LaTeX rendering for matplotlib
rc('text', usetex=True)
rc('font', family='serif')

# Plot the magnitude response
plt.figure(figsize=(8, 6))
plt.plot(omega, H_jomega, label=r'$|H(j\omega)|$')
plt.xlabel(r'$\omega$')
plt.ylabel(r'$|H(j\omega)|$')
plt.title('Impedance vs $\omega$')
plt.legend()
plt.grid(True)

# Save the plot as a PDF file for inclusion in LaTeX
plt.savefig('magnitude_response_plot.pdf')

# Display the plot (optional)
plt.show()
