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
x_sepbub, cp_sepbub = read_cp_data('naca2623_sepbub.txt')
x_inviscid, cp_inviscid = read_cp_data('naca2623_invsicid_cp.txt')

# Create the plot
plt.figure(figsize=(11, 7))
plt.plot(x_sepbub, cp_sepbub, 'b-', linewidth=2.5, label='Viscous flow with separation bubble, Re = 0.3M')
plt.plot(x_inviscid, cp_inviscid, 'r-', linewidth=2.5, label='Inviscid flow')
plt.axhline(y=0, color='k', linestyle='--', linewidth=1, alpha=0.5)
plt.gca().invert_yaxis()  # Invert y-axis (convention: Cp decreases downward)
plt.xlabel('x/c', fontsize=12)
plt.ylabel('Cp', fontsize=12)
plt.title('Cp Distribution - NACA 2623', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=11)
plt.tight_layout()

# Display the plot
plt.show()
