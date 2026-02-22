import matplotlib.pyplot as plt
import numpy as np
import os

# Use absolute path to ensure files are found
current_dir = os.path.dirname(os.path.abspath(__file__))

# Function to read transition data from file
def read_transition_data(filename):
    file_path = os.path.join(current_dir, filename)
    cl_values = []
    top_xtr = []
    bot_xtr = []
    
    with open(file_path, 'r') as file:
        lines = file.readlines()
        
        # Skip header lines (first 12 lines)
        for i in range(12, len(lines)):
            line = lines[i].strip()
            if line:  # Skip empty lines
                data = line.split()
                if len(data) >= 7:
                    try:
                        cl = float(data[1])  # CL value
                        top = float(data[5])  # Top_Xtr
                        bot = float(data[6])  # Bot_Xtr
                        cl_values.append(cl)
                        top_xtr.append(top)
                        bot_xtr.append(bot)
                    except ValueError:
                        continue
    return cl_values, top_xtr, bot_xtr

# Read data from both files
cl_orig, top_orig, bot_orig = read_transition_data('original2623.txt')
cl_mod, top_mod, bot_mod = read_transition_data('modsave2.txt')

# Create the plot
plt.figure(figsize=(12, 7))
plt.plot(top_orig, cl_orig, 'b-o', linewidth=2, markersize=6, label='Original - Top Surface')
plt.plot(bot_orig, cl_orig, 'b--s', linewidth=2, markersize=6, label='Original - Bottom Surface')
plt.plot(top_mod, cl_mod, 'r-o', linewidth=2, markersize=6, label='Modified - Top Surface')
plt.plot(bot_mod, cl_mod, 'r--s', linewidth=2, markersize=6, label='Modified - Bottom Surface')

plt.xlabel('Transition Location (x/c)', fontsize=12)
plt.ylabel('Cl', fontsize=12)
plt.title('Airfoil Transition Points', fontsize=14)
plt.grid(True, alpha=0.3)
plt.legend(fontsize=10)
plt.tight_layout()

# Display the plot
plt.show()
