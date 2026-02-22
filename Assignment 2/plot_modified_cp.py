import matplotlib.pyplot as plt
import numpy as np
import os

# Use absolute path to ensure files are found
current_dir = os.path.dirname(os.path.abspath(__file__))

# Function to read Cp data from file
def read_cp_data(filename):
    file_path = os.path.join(current_dir, filename)
    x_values = []
    cp_values = []
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        # Skip header lines (first 3 lines)
        for i in range(3, len(lines)):
            line = lines[i].strip()
            if line:  # Skip empty lines
                data = line.split()
                if len(data) >= 3:
                    try:
                        x = float(data[0])  # x/c value
                        cp = float(data[2])  # Cp value
                        x_values.append(x)
                        cp_values.append(cp)
                    except ValueError:
                        continue
    return x_values, cp_values

# Read data from both files
x_modified, cp_modified = read_cp_data('modifiedcp.txt')
x_original, cp_original = read_cp_data('originalcp.txt')

# Create the plot
plt.figure(figsize=(10, 6))
plt.plot(x_modified, cp_modified, 'b-', linewidth=2, label='Modified Airfoil')
plt.plot(x_original, cp_original, 'r-', linewidth=2, label='NACA 2623')
plt.axhline(y=0, color='k', linestyle='--', linewidth=1.5, label='Cp = 0')
plt.gca().invert_yaxis()  # Invert y-axis (convention: Cp decreases downward)
plt.xlabel('x/c', fontsize=12)
plt.ylabel('Cp', fontsize=12)
plt.title('Cp vs x/c at Re = 0.8 Million', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=11)
plt.tight_layout()

# Display the plot
plt.show()
