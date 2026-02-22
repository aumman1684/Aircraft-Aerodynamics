import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os


xtr = [0.1, 0.2, 0.25, 0.28, 0.3, 0.31, 0.32, 0.33, 0.34, 0.35, 0.36, 0.37, 0.38, 0.39, 0.4, 0.41, 0.5, 0.6, 0.7, 0.8, 0.9]
cd = [0.03, 0.02185, 0.02098, 0.02087, 0.02026 , 0.01970, 0.01947, 0.01932, 0.01912, 0.01897, 0.01880, 0.01865, 0.01852, 0.01838, 0.01825, 0.01812, 0.01865, 0.01865, 0.01865, 0.01865, 0.01865]

# Write data to Excel file
current_dir = os.path.dirname(os.path.abspath(__file__))
output_file = os.path.join(current_dir, 'cd_vs_transition.xlsx')

df = pd.DataFrame({'xtr': xtr, 'cd': cd})
df.to_excel(output_file, index=False)
print(f"Data written to {output_file}")

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(xtr, cd, 'b-', linewidth=2)
plt.xlabel('Transition Location (xtr/c)', fontsize=12)
plt.ylabel('Drag Coefficient (Cd)', fontsize=12)
plt.title('Cd vs Transition Location for NACA 2623 at Re = 0.5M and Cl = 0.8', fontsize=14)
plt.grid(True, alpha=0.3)
plt.tight_layout()

# Display the plot
plt.show()
