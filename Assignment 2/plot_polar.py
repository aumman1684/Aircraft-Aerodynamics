import matplotlib.pyplot as plt
import numpy as np
import os

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, 'polar_results.txt')

print(f"Looking for file at: {file_path}")
print(f"File exists: {os.path.exists(file_path)}")

# Lists to store alpha, Cl, Cm, Cd, Top_Xtr, and Bot_Xtr values
alpha_values = []
cl_values = []
cm_values = []
cd_values = []
top_xtr_values = []
bot_xtr_values = []

# Read the file
try:
    with open(file_path, 'r') as file:
        lines = file.readlines()
    print(f"Successfully read file. Total lines: {len(lines)}")
except FileNotFoundError:
    print(f"Error: File not found at {file_path}")
    exit()

# Parse the data (skip header lines until we find the data)
data_started = False
for line in lines:
    # Look for the header line with column names
    if 'alpha' in line.lower() and 'cl' in line.lower():
        data_started = True
        print("Found header line, starting to parse data...")
        continue
    
    # Skip the separator line
    if '----' in line:
        continue
    
    # Parse data lines
    if data_started and line.strip():
        try:
            values = line.split()
            if len(values) >= 7:
                alpha = float(values[0])
                cl = float(values[1])
                cd = float(values[2])
                cm = float(values[4])
                top_xtr = float(values[5])
                bot_xtr = float(values[6])
                alpha_values.append(alpha)
                cl_values.append(cl)
                cd_values.append(cd)
                cm_values.append(cm)
                top_xtr_values.append(top_xtr)
                bot_xtr_values.append(bot_xtr)
        except ValueError:
            # Skip lines that can't be converted to float
            pass

print(f"Parsed {len(alpha_values)} data points")

# Print first few values to verify
print("\nFirst 5 data points:")
print("Alpha\t\tCl\t\tCd\t\tCm\t\tTop_Xtr\t\tBot_Xtr")
for i in range(min(5, len(alpha_values))):
    print(f"{alpha_values[i]}\t\t{cl_values[i]}\t\t{cd_values[i]}\t\t{cm_values[i]}\t\t{top_xtr_values[i]}\t\t{bot_xtr_values[i]}")

# Create the first plot: Cl and Cm vs Alpha
from matplotlib.ticker import MultipleLocator

fig1, ax1 = plt.subplots(figsize=(9, 8))

ax1.set_xlabel('Alpha (degrees)', fontsize=14, fontweight='bold')
ax1.set_ylabel('Coefficients', fontsize=14, fontweight='bold')
ax1.plot(alpha_values, cl_values, 'b-o', linewidth=2.5, markersize=8, label='Cl')
ax1.plot(alpha_values, cm_values, 'r-s', linewidth=2.5, markersize=8, label='Cm')

# Add gridlines for first plot
ax1.xaxis.set_major_locator(MultipleLocator(1))
ax1.xaxis.set_minor_locator(MultipleLocator(0.2))
ax1.yaxis.set_major_locator(MultipleLocator(0.1))
ax1.yaxis.set_minor_locator(MultipleLocator(0.02))

ax1.grid(True, which='major', alpha=0.5, linewidth=0.8)
ax1.grid(True, which='minor', alpha=0.2, linewidth=0.4)
ax1.legend(fontsize=13, loc='best')
ax1.set_aspect('auto', adjustable='box')
ax1.tick_params(axis='both', which='major', labelsize=11)
ax1.set_title('Lift and Moment Coefficients vs Angle of Attack - NACA 2623', fontsize=14, fontweight='bold')

fig1.tight_layout()
plt.show()

# Create the second plot: Cl vs Cd*10^4 (Polar Curve)
fig2, ax2 = plt.subplots(figsize=(9, 8))

# Scale Cd by 10^4
cd_scaled = [cd * 10000 for cd in cd_values]

ax2.set_xlabel('Cd × 10^4 ', fontsize=14, fontweight='bold')
ax2.set_ylabel('Cl', fontsize=14, fontweight='bold')
ax2.plot(cd_scaled, cl_values, 'b-o', linewidth=2.5, markersize=8)

# Set x-axis limits and locators (0 to 200, increment by 50)
ax2.set_xlim(50, 150)
ax2.xaxis.set_major_locator(MultipleLocator(10))
ax2.xaxis.set_minor_locator(MultipleLocator(10))

# Set y-axis locators (back to original: 0.1 increment)
ax2.yaxis.set_major_locator(MultipleLocator(0.1))
ax2.yaxis.set_minor_locator(MultipleLocator(0.02))

ax2.grid(True, which='major', alpha=0.5, linewidth=0.8)
ax2.grid(True, which='minor', alpha=0.2, linewidth=0.4)
ax2.set_aspect('auto', adjustable='box')
ax2.tick_params(axis='both', which='major', labelsize=11)
ax2.set_title('Polar Curve: Cl vs Cd - NACA 2623', fontsize=14, fontweight='bold')

fig2.tight_layout()
plt.show()

# Create the third plot: Cl vs Top_Xtr and Bot_Xtr
fig3, ax3 = plt.subplots(figsize=(9, 8))

ax3.set_xlabel('Transition Location (Xtr/c)', fontsize=14, fontweight='bold')
ax3.set_ylabel('Cl', fontsize=14, fontweight='bold')
ax3.plot(top_xtr_values, cl_values, 'b-o', linewidth=2.5, markersize=8, label='Upper surface')
ax3.plot(bot_xtr_values, cl_values, 'r-s', linewidth=2.5, markersize=8, label='Lower surface')

# Add gridlines for third plot
ax3.xaxis.set_major_locator(MultipleLocator(0.1))
ax3.xaxis.set_minor_locator(MultipleLocator(0.02))
ax3.yaxis.set_major_locator(MultipleLocator(0.1))
ax3.yaxis.set_minor_locator(MultipleLocator(0.02))

ax3.grid(True, which='major', alpha=0.5, linewidth=0.8)
ax3.grid(True, which='minor', alpha=0.2, linewidth=0.4)
ax3.legend(fontsize=13, loc='best')
ax3.set_aspect('auto', adjustable='box')
ax3.tick_params(axis='both', which='major', labelsize=11)
ax3.set_title('Cl vs Transition Location over the chord - NACA 2623', fontsize=14, fontweight='bold')

fig3.tight_layout()
plt.show()

# 4th plot alpha vs transition points
fig4, ax4 = plt.subplots(figsize=(9, 8))

ax4.set_xlabel('Transition Location (Xtr/c)', fontsize=14, fontweight='bold')
ax4.set_ylabel('alpha (degrees)', fontsize=14, fontweight='bold')
ax4.plot(top_xtr_values, alpha_values, 'b-o', linewidth=2.5, markersize=8, label='Upper surface')
ax4.plot(bot_xtr_values, alpha_values, 'r-s', linewidth=2.5, markersize=8, label='Lower surface')

# Add gridlines for fourth plot
ax4.xaxis.set_major_locator(MultipleLocator(0.1))
ax4.xaxis.set_minor_locator(MultipleLocator(0.02))
ax4.yaxis.set_major_locator(MultipleLocator(1))
ax4.yaxis.set_minor_locator(MultipleLocator(0.2))

ax4.grid(True, which='major', alpha=0.5, linewidth=0.8)
ax4.grid(True, which='minor', alpha=0.2, linewidth=0.4)
ax4.legend(fontsize=13, loc='best')
ax4.set_aspect('auto', adjustable='box')
ax4.tick_params(axis='both', which='major', labelsize=11)
ax4.set_title('Alpha vs Transition Location over the chord - NACA 2623', fontsize=14, fontweight='bold')

fig4.tight_layout()
plt.show()

