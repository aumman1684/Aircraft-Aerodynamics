import numpy as np
import matplotlib.pyplot as plt
import os

# Set the absolute paths to the data files
data_path_alpha0 = os.path.join(os.path.dirname(__file__), 'cf_alpha0_dump.txt')
data_path_alpha4 = os.path.join(os.path.dirname(__file__), 'cf_alpha4_dump.txt')

# Read the data from both files
data_alpha0 = np.loadtxt(data_path_alpha0, skiprows=1)
data_alpha4 = np.loadtxt(data_path_alpha4, skiprows=1)

# Extract x and Cf columns for alpha = 0
x0 = data_alpha0[:, 1]      # x values
y0 = data_alpha0[:, 2]      # y values
cf0 = data_alpha0[:, 6]     # Cf values

# Extract x and Cf columns for alpha = 4
x4 = data_alpha4[:, 1]      # x values
y4 = data_alpha4[:, 2]      # y values
cf4 = data_alpha4[:, 6]     # Cf values

# Filter to keep only upper surface (where y >= 0) and x <= 1
mask0 = (y0 >= 0) & (x0 <= 1.0)
x0_filtered = x0[mask0]
cf0_filtered = cf0[mask0]

mask4 = (y4 >= 0) & (x4 <= 1.0)
x4_filtered = x4[mask4]
cf4_filtered = cf4[mask4]

# Create the plot with both datasets
plt.figure(figsize=(10, 6))
plt.plot(x0_filtered, cf0_filtered, 'b-', linewidth=2, label='alpha = 0°')
plt.plot(x4_filtered, cf4_filtered, 'r-', linewidth=2, label='alpha = 4°')
plt.xlabel('x/c (Upper Surface)', fontsize=12)
plt.ylabel('Friction Coefficient (Cf)', fontsize=12)
plt.title('Cf vs x/c (Upper Surface)', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=11)
plt.tight_layout()

# Show the plot
plt.show()
