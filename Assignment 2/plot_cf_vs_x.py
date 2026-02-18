import numpy as np
import matplotlib.pyplot as plt
import os

# Set the absolute path to the data file
data_path = os.path.join(os.path.dirname(__file__), 'cf_alpha0_dump.txt')

# Read the data from the file
data = np.loadtxt(data_path, skiprows=1)

# Extract x and Cf columns
x = data[:, 1]      # x values (column 2, index 1)
y = data[:, 2]      # y values (column 3, index 2)
cf = data[:, 6]     # Cf values (column 7, index 6)

# Filter to keep only upper surface (where y >= 0) and x <= 1
mask = (y >= 0) & (x <= 1.0)
x = x[mask]
cf = cf[mask]

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x, cf, 'b-', linewidth=2)
plt.xlabel('x/c, upper surface', fontsize=12)
plt.ylabel('Friction Coefficient (Cf)', fontsize=12)
plt.title('Cf vs x/c at alpha = 0 degrees', fontsize=14)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Show the plot
plt.show()
